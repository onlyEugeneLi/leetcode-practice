import argparse
import sys
import logging
from typing import Any, Dict

class CustomError(Exception):
    pass

class ValidationError(Exception):
    def __init__(self, **kwargs):
        self.message = kwargs.get("message", "Default validation error")
        self.code = kwargs.get("code", "500")

        super().__init__(self.message)

def parse_cli_to_kwargs() -> Dict[str, Any]:
    parser = argparse.ArgumentParser(
        description="Process infra validation flags"
    )

    parser.add_argument("-m", "--message", type=str, help="The error message string")
    parser.add_argument("-c", "--code", type=str, help="The HTTP or internal error code")

    parsed_args = parser.parse_args()

    return vars(parsed_args)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
_handler = logging.FileHandler("argparse.log")
_handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))
logger.addHandler(_handler)


VALID_CODES = {"200", "400", "404", "500"}

def validate_inputs(kwargs: Dict[str, Any]) -> None:
    errors = []

    if not kwargs.get("message"):
        errors.append("--message is required or cannot be empty")

    if kwargs.get("code") not in VALID_CODES:
        errors.append(f"Invalid code '{kwargs.get('code')}', must be one of {VALID_CODES}")

    if errors:
        raise ValidationError(message=";\n".join(errors), code="400")

def main():
    cli_kwarg = parse_cli_to_kwargs()
    clean_kwargs = {k: v for k, v in cli_kwarg.items() if v is not None}

    try:
        validate_inputs(clean_kwargs)
        logger.info(f"Inputs valid: {clean_kwargs}")
    except ValidationError as e:
        logger.error(f"Caught ValidationError!")
        logger.error(f"-> Code Attribute:    {e.code}")
        logger.error(f"-> Message Attribute: {e.message}", exc_info=True)
        raise
    finally:
        logger.info(f"Shutting down the process...")

if __name__ == "__main__":
    main()
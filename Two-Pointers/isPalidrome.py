"""
This is a coding exercise I encountered in an interview for a Site Reliability Engineer position at a large tech company. The task was to implement a function that checks if a given string is a palindrome, meaning it reads the same forwards and backwards, factoring in case sensitivity.
"""

# Question: The task of checking if a string is a palindrome in Python involves determining whether a string reads the same forward as it does backward. For example, the string "madam" is a palindrome because it is identical when reversed, whereas "hello" is not.

## Make use of .lower() to ignore case sensitivity

def is_palindrome(s: str) -> bool:

    left, right = 0, len(s) - 1  # two pointers

    s = s.lower()  # convert to lowercase

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    return True


if __name__ == "__main__":
    test_cases = [
        "Hannah",
        "racecar",
        "malayalam"
    ]
    print("Test cases:")
    for test in test_cases:
        print(f"{test} is palindrome: {is_palindrome(test)}")  
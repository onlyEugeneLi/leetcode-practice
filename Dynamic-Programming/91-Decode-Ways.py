class Solution:
    def numDecodings(self, s: str) -> int:
        # Dynamic programming
        # Tabulation (Bottom-up)
        # Table of ways of decoding
        # Edge case: 
            # 1. first digit is 0, no way to encode
            # 2. empty string
        if not s or s[0] == '0':
            return 0

        num_digits = len(s)
        decoding_ways = [0] * (num_digits + 1)
        # 0 digit: 1 way
        decoding_ways[0] = 1
        # 1 digits: 1 way
        decoding_ways[1] = 1
        # 2+ digits: 
        for i in range(2, num_digits + 1):
            # Convert string digits to integers
            single_digit = int(s[i - 1 : i]) # Single digit number
            two_digits = int(s[i - 2 : i]) # Two-digit number
            # if single digit not '0': continue count from previous single digit
            if single_digit != 0:
                decoding_ways[i] += decoding_ways[i - 1]
            # else: must be two-digit number (10, 20)--continue count from previous two-digit count
            if 10 <= two_digits <= 26:
                decoding_ways[i] += decoding_ways[i - 2]
        
        return decoding_ways[-1]
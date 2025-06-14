# Combination function `product()` method: https://leetcode.com/problems/letter-combinations-of-a-phone-number/solutions/6235314/no-backtracking-6-lines-easy

# Backtracking solution: https://leetcode.com/problems/letter-combinations-of-a-phone-number/solutions/6817604/letter-combinations-of-a-phone-number-clean-recursive-solution-with-tree-beats-100

from typing import List

'''
                    ""
        _____________|______________
       |             |             |
      "a"           "b"           "c"
     / | \         / | \         / | \
 "ad""ae""af"  "bd""be""bf"  "cd""ce""cf"

'''

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        '''
        Intuition:

        Digits-to-letters-map
        - dictionary {'2':'abc', ...}

        Read digits
        Permutation of all combinations
        '''

        # Base case
        if not digits:
            return []

        buttons = {
            "2": ("a", "b", "c"),
            "3": ("d", "e", "f"),
            "4": ("g", "h", "i"),
            "5": ("j", "k", "l"),
            "6": ("m", "n", "o"),
            "7": ("p", "q", "r", "s"),
            "8": ("t", "u", "v"),
            "9": ("w", "x", "y", "z")
        }

        num_of_digits = len(digits)

        combinations = []

        def backtrack(letters, index):
            if len(letters) == num_of_digits: # Reach the end of the digits
                # Append the a complete combination to the result
                combinations.append(letters)
                return
            
            for char in buttons[digits[index]]:
                backtrack(letters + char, index + 1)
        
        backtrack("", 0)

        return combinations

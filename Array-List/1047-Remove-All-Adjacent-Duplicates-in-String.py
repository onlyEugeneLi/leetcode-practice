# test cases:
# aab --> b
# abb --> a
# aba --> aba
# aa --> ''
# a --> a

# Approach: 
# 1. Hash map, index, flag to confirm adjacency
# 2. 
class Solution_brute_force:
    def removeDuplicates(self, s: str) -> str:
        # Base case
        if len(s) == 1:
            return s
        
        # string immutable -- convert to list so to remove elements | could also use slicing
        s_array = list(s)
        i = 0 # Index

        # Loop to traverse the list
        while i < len(s_array) - 1:
            # Look for adjacent duplicates: check or flag
            if s[i + 1] == s[i]:
                del s_array # Remove them
                i = max(i - 1, 0) # Size of array changed, move one step back or back to beginning
            else: 
                i += 1

            # How to verify no more adjacent duplicates left? 
        return ''.join(s_array)


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

class Solution_slicing:
    def removeDuplicates(self, s: str) -> str:
        # Base case
        if len(s) == 1:
            return s
        
        # string immutable -- convert to list so to remove elements | could also use slicing
        
        i = 0
        while i < len(s) - 1: # Avoid 'out-of-bound' situation
            # Identify duplicates and make sure index is within range
            if i >= 0 and s[i] == s[i + 1]: 
                # Remove duplicates
                s = s[: i] + s[i + 2 : ]
                i -= 1 # original index i character is removed so move back
            else: 
                # No duplicate identified, move to next
                i += 1 

        return s

class Solution_stack:
    def removeDuplicates(self, s: str) -> str:

        string_stack = []

        for char in s:
            if string_stack and string_stack[-1] == char:
                string_stack.pop() # Next one is duplicate, remove existing one
            else:
                string_stack.append(char)

        return ''.join(string_stack)
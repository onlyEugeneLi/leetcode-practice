class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # counter k 
        # stack (character, count)
        # recreate a string based on the stack information

        # Edge cases
        # k > len(s), k == 0
        if k > len(s) or k == 0 or not s:
            return s
        # k == 1, eliminate all letters
        if k == 1:
            return ''
        
        # Stack: (char, duplicate)
        string_stack = []

        for i in s:
            # Check if current letter equal to previous one
            if string_stack and i == string_stack[-1][0]:
                # Occurence + 1
                string_stack[-1][1] += 1
                # Check if latest letter has over k occurrences
                if string_stack[-1][1] >= k:
                    string_stack.pop()
            # If curent letter not same as previous letter, record it in the stack
            else:
                string_stack.append([i, 1])
            
        # Recreate new string after duplicate removal
        result = ''
        for char, occurrence in string_stack:
            result += char * occurrence

        # Return answer
        return result

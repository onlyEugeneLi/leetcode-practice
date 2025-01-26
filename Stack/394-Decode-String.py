class Solution:
    def decodeString(self, s: str) -> str:
        # # Method 1: yet to understand
        # substring = ""
        # stack = []
        # num = ""

        # for c in s:
        #     # Check if it's digit
        #     if c.isdigit():
        #         # Build the repeat count number
        #         num += c
        #     # Start of substring
        #     elif c == "[":
        #         # Push current context to stack
        #         stack.append((substring, int(num)))
        #         # Offset
        #         substring = ""
        #         num = ""
        #     # End of substring
        #     elif c == "]":
        #         # Pop and combine the repeated substrings
        #         last_string, repeat_count = stack.pop()
        #         substring = last_string + substring * repeat_count
        #     else:
        #         # Append character to the current string
        #         substring += c
        # return substring

        # Method 2:
        stack = []

        for c in s:
            # Keep stacking the characters until ']'
            if c != ']':
                stack.append(c)
            
            else:
                subString = ""
                # Extract current substring
                while stack[-1] != '[':
                    subString = stack.pop() + subString
                stack.pop() # Remove '['

                num = ""
                # Extract repeat number
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num

                # stack[-1] += int(num) * subString # Error: list index out of range
                                                    # When back at the first digit, stack is empty.
                subString = int(num) * subString
                stack.append(subString)
        return ''.join(stack)



print(Solution().decodeString('3[a2[c]]'))
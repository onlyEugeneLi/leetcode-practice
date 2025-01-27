class Solution:
    def compress(self, chars: list[str]) -> int:
        # # Self attempt: Brute force
        # idx = 0
        # begin_of_group = 0
        # res = ""
        # # Traverse the list
        # while begin_of_group < len(chars):
        #     count = 0
        #     res += chars[begin_of_group] # Log the character
        #     # Count the character group
        #     # Check if each char after the first one is the same as the first one
        #     while chars[idx] == chars[begin_of_group]:
        #         count += 1
        #         idx += 1
        #     # Log the count
        #     if count > 1:
        #         res += str(count)
        #     begin_of_group += count
        # print(f"The compressed string --> {res}")
        # return len(res)

        # Solution
        # Only use constant extra space:
        # -- Operating the list **in place**
        n = len(chars)
        idx = 0
        i = 0
        while i < n:
            c = chars[i]
            count = 0
            while i < n and chars[i] == c:
                count += 1
                i += 1
            # Use "i" to traverse the list
            # Use "idx" to point where to modify
            if count == 1:
                chars[idx] = c # count == 1 : no need to attach count
                idx += 1
            else:
                chars[idx] = c
                idx += 1
                for digit in str(count):
                    chars[idx] = digit
                    idx += 1
        
        chars[:] = chars[:idx] # Replace the entire list with first "idx" elements
        '''
        chars[:] = chars[:idx]:
        - This syntax modifies the contents of the existing list chars in place.
        - It replaces all elements of chars with the elements from chars[:idx].
        - The original list object remains the same, but its contents are updated.
        '''
        print(f"\n{'Compressed string':<28}{'-->':^5}{str(chars)}")
        return idx
    
chars = ["a","a","b","b","c","c","c"]
print(f"{'Length of compressed string':<28}{'-->':^5}{Solution().compress(chars)}\n")
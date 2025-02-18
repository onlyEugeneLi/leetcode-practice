class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # Solution
        vowels = set('aeiou')
        max_vowels = 0
        count = 0
        for i in range(k):
            if s[i] in vowels:
                count += 1
        
        max_vowels = count 

        for i in range(k, len(s)):
            # Count -1 if the left most value is vowel,
            # as the sliding window moves to right and leaves it out.
            if s[i - k] in vowels:
                count -= 1
            # Count +1 if the next value is vowel,
            # as the sliding window moves to right and includes it in. 
            if s[i] in vowels:
                count += 1
            
            max_vowels = max(max_vowels, count)
        
        return max_vowels

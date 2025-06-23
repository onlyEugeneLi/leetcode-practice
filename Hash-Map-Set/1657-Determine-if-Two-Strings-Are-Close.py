class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        freq1 = [0] * 26
        freq2 = [0] * 26

        # 26 letters -> their order as index 
        # Store the number of ocurrence of each letter
        for ch in word1:
            freq1[ord(ch) - ord('a')] += 1

        for ch in word2:
            freq2[ord(ch) - ord('a')] += 1

        # Check if two 
        # for i in range(26):
        #     if (freq1[i] == 0 and freq2[i] != 0) or (freq1[i] != 0 and freq2[i] == 0):
        #         return False
        
        if set(word1) != set(word2):
            return False

        freq1.sort()
        freq2.sort()

        for i in range(26):
            if freq1[i] != freq2[i]:
                return False
            
        return True

from collections import Counter
class Solution_built_in_hash:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # 2 strings
        # All lowercase
        # Length can be same or different
        # Edge case
        # Not same length, impossible to be close
        if len(word1) != len(word2):
            return False
        # Same words
        if word1 == word2:
            return True
        # Approach: Hash index map
        # Requirement for close words:
        # 1. Contain same characters
        # 2. Contain same occurrence distribution

        # Hashing
        occurrence_word1 = Counter(word1) # {'a': occurrences, ...}
        occurrence_word2 = Counter(word2)

        # Number of occurences for each characters in both words
        occurrence_value_word1 = sorted(occurrence_word1.values())
        occurrence_value_word2 = sorted(occurrence_word2.values())
        same_occurrence = occurrence_value_word1 == occurrence_value_word2

        # Characters in both words: Are they same
        same_character = occurrence_word1.keys() == occurrence_word2.keys()

        return same_occurrence and same_character

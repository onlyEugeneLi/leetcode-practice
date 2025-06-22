class Solution_brute_force:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Edge cases: 
        # s and t same length? 
        if len(s) != len(t):
            return False

        # Hash table: mapping letter from s to t and vice versa
        map_s, map_t = {}, {}

        for char_s, char_t in zip(s, t):
            if char_s not in map_s:
                map_s[char_s] = char_t
            else: 
                if map_s[char_s] != char_t:
                    return False
            
            if char_t not in map_t:
                map_t[char_t] = char_s
            else:
                if map_t[char_t] != char_s:
                    return False
        
        return True

class Solution_hash_map_index:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Edge cases: 
        # s and t same length? 
        if len(s) != len(t):
            return False

        # Hash table: mapping letter from s to t and vice versa
        map_s, map_t = {}, {}

        for i in range(len(s)):
            char_s, char_t = s[i], t[i]
            # If character not seen before, store
            # its first occurrence index
            if char_s not in map_s:
                map_s[char_s] = i
            if char_t not in map_t:
                map_t[char_t] = i
            # Check if the first occurrence indices match
            if map_s[char_s] != map_t[char_t]:
                return False
        
        return True
    
class Solution_set:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Edge cases: 
        # s and t same length? 
        if len(s) != len(t):
            return False

        # Set to track unique characters
        map_s = dict()
        set_t = set()

        for char_s, char_t in zip(s, t):
            if char_s in map_s:
                # If character already mapped, check if it maps to the same character
                if map_s[char_s] != char_t:
                    return False
            else:
                if char_t in set_t:
                    # If the character is already mapped to another character, return False
                    return False
            
            # Not mapped yet, map character s to t
            map_s[char_s] = char_t
            # Add to used characters set
            set_t.add(char_t)

        return True
class Solution:
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
class Solution:
    # # Method 1: Hash map
    # def singleNumber(self, nums: list[int]) -> int:
    #     hashmap = {}
    #     for n in nums:
    #         if n not in hashmap:
    #             hashmap[n] = 1
    #         else:
    #             hashmap[n] += 1
        
    #     return list(hashmap.keys())[list(hashmap.values()).index(1)]
    
    # Method 2: Bitwise XOR
    # XOR: same -> 0, different -> 1
    # 0 remains 0, 1 stands out.
    # 去同存异
    def singleNumber(self, nums: list[int]) -> int:
        xor = 0
        for n in nums:
            # Two same numbers cancel out each out, only the single number will be retained by XOR operation
            xor = xor ^ n

        return xor
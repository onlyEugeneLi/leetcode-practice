'''
                 null
                   |
     -------------------------------
    |            |          |       |
    1            2         ...      9
  / | \ \       /|\ \              /|\ \
 2  3  4 ...   1 3 4 ...         ...6 7 8

'''
from typing import List

class Solution_backtrack:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # Initialisation
        combinations = []
        curr_comb = []

        # Explore combinations
        # Traverse number list
        # Backtrack to rest of options
        def backtrack(index):
            if len(curr_comb) == k and sum(curr_comb) == n:
                combinations.append(curr_comb[:])
                return
            
            for num in range(index, 10):
                curr_comb.append(num)
                backtrack(num + 1)
                curr_comb.pop()

        backtrack(1)

        return combinations
    
class Solution_dp: # Faster runtime than backtracking 
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        result = []
        def dp(i, asum, alist) :

            if asum == n and len(alist) == k : 
                result.append(alist[:])
                return 

            if asum > n or len(alist) > k or i >= len(nums) : return  

            # Dont take ith element
            dp(i + 1, asum, alist)

            # Take ith element 
            alist.append(nums[i])
            dp(i + 1, asum + nums[i], alist)
            alist.pop()

        dp(0, 0, [])
        return result
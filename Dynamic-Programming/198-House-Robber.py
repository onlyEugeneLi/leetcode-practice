class Solution:
    def rob(self, nums: list[int]) -> int:
        
        hcount = len(nums) # House count

        #Base case
        if hcount == 1:
            return nums[0]
        # if hcount == 2:
        #     return max(nums[1], nums[0])
        
        # recursive memo: saves local optimum at every step
        dp = [0] * hcount

        # Base case: house count = 2
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, hcount):
            # Greedy algorithm
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])
                    # [x, y, z]
                    # max(
                    #  option 1: skip house x, 
                    #            as house y has more money.,
                    #  option 2: skip house y,
                    #            as house x + z have more money.
                    # )

        return dp[-1]
    
algo = Solution().rob
# nums = [1,2,3,1]
nums = [2,7,9,3,1]
print(f"Total amount: {algo(nums)}")
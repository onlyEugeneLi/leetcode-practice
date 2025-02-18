class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        # # Self attempt
        # # While to traverse the list and search for 1s
        # i = 0
        # count = 0
        # flip = 0
        # n = len(nums)
        # cons_ones = 0
        # while i < n:
        #     count = 0
        #     flip = 0
            
        #     # Inner while to count number of consecutive 1s
        #     # Flip k 0s
        #     # Gap 0 > k or <= k
        #     while i < n:
        #         if nums[i] == 1:
        #             count += 1
        #             i += 1
        #         if i + 1 < n and nums[i + 1] == 0 and flip < k:
        #             nums[i + 1] = 1
        #             flip += 1
        #             i += 1
        #         if i + 1 < n and nums[i + 1] == 0 and flip >= k:
        #             break 
            
        #     cons_ones = max(count, cons_ones)
                
        # Solution
        left = right = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                k -= 1
            
            if k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
        return right -left + 1
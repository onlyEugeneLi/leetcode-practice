class Solution:
    def longgestSubarray(self, nums: list[int]) -> int:
        # Delete one element from the subarray to have max number of consecutive 1s

        n = len(nums)
        left = 0
        zeros = 0
        ans = 0

        # Rules on when to move left and right pointer.
        for right in range(n):
            if nums[right] == 0:
                zeros += 1
            
            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            
            ans = max(ans, right - left + 1 - zeros)

        return ans - 1 if ans == n else ans

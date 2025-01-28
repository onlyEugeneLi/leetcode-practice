class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        # Set up two pointers: right and left on both ends of the list
        right = len(nums) - 1
        left  = 0
        # Counter
        count = 0
        # Sort the list so we can determine set up if-statements
        nums.sort() # ascending order
        # Check the list step by step
        while left < right and nums:
            # Check that sum == k
            if nums[right] + nums[left] == k:
                count += 1
                left += 1
                right -= 1
            # Don't have to pop the pair as it's not assessed
            elif nums[right] + nums[left] < k: # pre-requisite: sorted list
                left += 1
            else:
                right -= 1
                
        return count
    
k = 4
nlist = [1,2,3,4]
print(f"Operation count: {Solution().maxOperations(nlist, k)}")
class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        # # First attempt
        # # Base case
        # if len(nums) < 3:
        #     return False
        # left, mid, right = 0, 1, 2
        # # for i in range(len(nums) - 2):
        # while nums[left] >= nums[mid] and right < len(nums) - 1:
        #     left += 1
        #     mid += 1
        #     right += 1
            
        # while nums[mid] >= nums[right] and right < len(nums) - 1:
        #     right += 1

        # while nums[left] >= nums[mid] and mid < right:
        #     mid += 1

        # if nums[left] < nums[mid] < nums[right]:
        #     return True
        
        # return False

        # # Solution
        left = float('inf')
        mid = float('inf')
        for n in nums:
            if n <= left:
                left = n
            elif n <= mid:
                mid = n 
            else:
                return True
        return False
    
        # # Doubao - AI solution
        # # Can't resolve testcases [20,100,10,12,5,13] and [1, 1, -1, 6]
        # import sys
        # first = sys.maxsize
        # second = sys.maxsize
        # first_index = -1
        # second_index = -1
        # for index, num in enumerate(nums):
        #     if num < first:
        #         first = num
        #         first_index = index
        #     elif num > first and num < second:
        #         second = num 
        #         second_index = index
        #     elif num > second and second_index > first_index:
        #         return True
        # return False


# nums = [1,2,3,4,5]
# nums = [5,4,3,2,1]
# nums = [2,1,5,0,4,6]
nums = [20,100,10,12,5,13]
print(Solution().increasingTriplet(nums))
from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # left, mid, right pointers converge to the peak 

        # Step 1: feel the slope -- peak on the left side or right side of mid pointer -- compare mid ? mid + 1

        # Step 2: narrow search down to one side
        # if mid > mid + 1 ==> peak on the left side
        #   right = mid
        #   mid = (left + right) // 2
        # Vice versa 

        # Step 3: when all left and right pointers meet ==> return peak index (left pointer)

        left, right = 0, len(nums) - 1
        mid = (left + right) // 2

        while left < right:
            if nums[mid] > nums[mid + 1]:
                right = mid
                mid = (left + right) // 2
            else:
                left = mid + 1 # Narrow the range to the right side of 
                mid = (left + right) // 2
            
        return left
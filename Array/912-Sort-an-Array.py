from typing import List

# Sorting in place -- space complexity O(1)
class Solution_quick_sort_TLE:
    def sortArray(self, nums: List[int]) -> List[int]:
        ''' Sorting function '''
        def quick_sort(arr, low, high):
            # Only proceed when more than one element is present
            if low < high:
                # Rearrange array as per pivot and return pivot index
                pivot_pointer = partition(arr, low, high)

                # Repeat above processes in partitions
                quick_sort(arr, low, pivot_pointer - 1)
                quick_sort(arr, pivot_pointer + 1, high) # Don't include last element as it's the pivot

            return arr

        def partition(arr, low, high):
            pivot = arr[high] # Always select last element as pivot

            # Move all numbers smaller than pivot to the left side
            pivot_pointer = low - 1 # Virtually move pivot across array to find the correct position

            for i in range(low, high):
                if arr[i] < pivot:
                    pivot_pointer += 1
                    arr[i], arr[pivot_pointer] = arr[pivot_pointer], arr[i]
            # End of for loop: pivot_pointer sits on the right-most smaller-than-pivot element
            arr[pivot_pointer + 1], arr[high] = arr[high], arr[pivot_pointer + 1]
            
            return pivot_pointer + 1 # Point to the actual pivot element
        
        ''' Main function '''
        # Base case
        if len(nums) <= 1:
            return nums

        return quick_sort(nums, 0, len(nums) - 1)

# No TLE error: Sorting with extra space -- space complexity O(n), time complexity O(n log n)
from random import randint
class Solution_quick_sort:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Base case: empy or single element array
        if len(nums) <= 1:
            return nums
        
        '''
        Justification for using random pivot:

        (Won't work if not using random pivot)

        By choosing a random pivot, the chance of worst-case recursion (deep call stack and large intermediate lists) is greatly reduced.

        The recursion tree is more balanced on average, so the maximum recursion depth and memory usage are much lower.
        '''
        pivot = nums[randint(0, len(nums) - 1)]  
        
        # Sorting and partitioning
        less = [n for n in nums if n < pivot]
        equal = [n for n in nums if n == pivot]
        greater = [n for n in nums if n > pivot]

        return self.sortArray(less) + equal + self.sortArray(greater)

class Solution_merge_sort:
    def sortArray(self, nums: List[int]) -> List[int]:
        ''' Sorting function '''
        def merge_sort(arr):
            # Base case: when array is split to a single element left
            if len(arr) <= 1:
                return arr
            
            # Split array into half
            left_sub_array = merge_sort(arr[ : len(arr) // 2])
            right_sub_array = merge_sort(arr[len(arr) // 2 : ])

            return merge(left_sub_array, right_sub_array)
        
        def merge(left_array, right_array):
            merged_sorted_array = []
            i, j = 0, 0
            while i < len(left_array) and j < len(right_array):
                # Sort: Small --> Large
                if left_array[i] < right_array[j]:
                    merged_sorted_array.append(left_array[i])
                    i += 1
                else:
                    merged_sorted_array.append(right_array[j])
                    j += 1
            
            # When one array is exhausted, append residual elements (all bigger ones)
            if i < len(left_array):
                merged_sorted_array += left_array[i : ]
            
            if j < len(right_array):
                merged_sorted_array += right_array[j : ]

            # Or replace above code with below:
            # merged_sorted_array.extend(left_array[i:])
            # merged_sorted_array.extend(right_array[j:])

            return merged_sorted_array
        
        ''' Main function '''

        return merge_sort(nums)
        
if __name__== "__main__":
    nums = [5, 2, 3, 1]
    # print(Solution_quick_sort().sortArray(nums))  # Output: [1, 2, 3, 5]
    
    # nums = [5, 1, 1, 2, 0, 0]
    # print(Solution_quick_sort().sortArray(nums))  # Output: [0, 0, 1, 1, 2, 5]
    # Solution_quick_sort().sortArray(nums)
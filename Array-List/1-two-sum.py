from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # input data type: array & int
        # data: array of numbers & target
        # objective: function returns indices of 2 elements in the array that add up to target
        # output data type: array containing the 2 indices

        # case 1 -- exist: nums = [1, 2]; target = 3 --> answer = [0, 1]
        # input guarantees there will be answer and only one answer

        # Solution 1: Add up combination of 2 numbers in the array and compare the result with target, store index in the iterators
        # Solution 2: Hashmap to store traversed values and indices and check if difference of target and current value is in the hashmap -- if yes, return the answer

        checked_values = dict() # Initiate the hashmap for value and index -- value: index
        for index, val in enumerate(nums):
            diff = target - val
            # If difference exists in the checked value list, return answer
            if diff in checked_values:
                return [checked_values[diff], index]
            # If not, append current value to the checked value list
            checked_values[val] = index

        return 

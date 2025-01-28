class Solution:
    def maxArea(self, height: list[int]) -> int:
        # # Method 1: Brute force
        # # Update max area as it goes
        # _area = float('-inf')
        # # Base case [1, 2]
        # # idx_1, idx_2: iterators, calculate width of container
        # # for loop and enclosed loop to traverse all combinations
        
        # # Time O(n^2)
        # num_lines = len(height)
        # for idx1 in range(num_lines):
        #     for idx2 in range(idx1 + 1, num_lines):
        #         # Determines height upper limit of container
        #         h = min(height[idx1], height[idx2])
        #         # Calculate width
        #         w = idx2 - idx1
        #         # Calculate the area
        #         _area = max(_area, h * w)
        # return _area
        # # Time O(n^2)

        # Solution: Two pointers
        _area = 0
        left = 0
        right = len(height) - 1
        while left < right:
            _area = max(_area, 
                        (right - left) * min(height[left], height[right]))
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return _area


hlist = [1,8,6,2,5,4,8,3,7]
print(f"\nMax area of container: {Solution().maxArea(hlist)}\n")
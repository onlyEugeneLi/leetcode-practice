from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # Sort balloons based on the end position
        points.sort(key = lambda x: x[1])

        boundary = float('-inf')
        count = 0
        for start, end in points:
            if boundary < start:
                boundary = end
                count += 1
        return count

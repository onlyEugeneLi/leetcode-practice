from typing import List
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Sort intervals based on end elements

        # Check for non-overlapping
        # Non-overlapping condition:
        # end_(i) < start_(i+1)

        # Count overlapping intervals

        intervals.sort(key = lambda x: x[1])

        count = 0
        end = float('-inf')

        for start, finish in intervals:
            # Non-overlapping: end_(i) < start_(i+1)
            if end <= start:
                end = finish # Update new interval end
            else: # Overlapped 
                count += 1

        return count
import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # k-th Largest -- 从小到大，倒数第k的数

        min_heap = []

        for num in nums:
            # heappush: makes sure the smallest element is always at the root (index 0)
            heapq.heappush(min_heap, num)

            # 
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        return min_heap[0]
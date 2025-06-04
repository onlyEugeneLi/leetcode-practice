import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # k-th Largest -- 从小到大，倒数第k的数

        # Take first k numbers in the list
        heap = nums[:k]

        # Convert the k-length list into Heap
        heapq.heapify(heap)
        
        # Start comparing from the index k number
        for num in nums[k:]:
            # Replace the smallest number in the heap with next larger number
            if num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, num)
        
        return heap[0]
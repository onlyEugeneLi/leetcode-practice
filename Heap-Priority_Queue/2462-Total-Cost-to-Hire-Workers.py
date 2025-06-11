from typing import List
import heapq

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        # Initialisation
        front_ptr = 0
        back_ptr = len(costs) - 1
        front = []
        back = []
        total_cost = 0
        
        # Loop while hiring_season < k: 
        while k > 0:
        # Return min from heads and tails of costs array and sum up the cost every iteration
        # Maintain original cost array for consistent indexing
            while len(front) < candidates and front_ptr <= back_ptr:
                # front_ptr <= back_ptr -- when candiates > length of costs array, to prevent repeatition and clash
                heapq.heappush(front, costs[front_ptr])
                front_ptr += 1
            while len(back) < candidates and front_ptr <= back_ptr:
                heapq.heappush(back, costs[back_ptr])
                back_ptr -= 1
            
            worker_front = front[0] if front else float('inf')
            worker_back = back[0] if back else float('inf')

            # if both costs are equal, use the smaller index to break the tie
            if worker_front <= worker_back:
                total_cost += worker_front
                heapq.heappop(front)
            else:
                total_cost += worker_back
                heapq.heappop(back)
            
            k -= 1

        return total_cost
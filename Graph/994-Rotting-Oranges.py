from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
        Initialisation
        '''
        row, column = len(grid), len(grid[0])
        number_of_fresh_oranges = 0 # Tracks number of fresh oranges real-time during the spread, and to confirm whether all fresh oranges were reached

        # next_to_visit queue to implement BFS - (x, y)
        next_step_guide = deque()

        # Scan the map
        # Locate all the rotten orange(s) -- starting point
        for i in range(row):
            for j in range(column):
                if grid[i][j] == 2:
                    next_step_guide.append((i, j))
                elif grid[i][j] == 1:
                    number_of_fresh_oranges += 1
        # Base cases:
        # 1. When there's no fresh oranges to begin with
        if number_of_fresh_oranges == 0:
            return 0
        # 2. When there's no rotten oranges to begin with
        if not next_step_guide:
            return -1

        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)] # [UP, DOWN, LEFT, RIGHT]
        # Count steps
        minutes_taken = -1 # Start with the original rotten oranges, it counts as the 0 minute

        '''
        BFS
        '''
        while next_step_guide:

            for _ in range(len(next_step_guide)):
                x, y = next_step_guide.popleft()
                # Explore 4 adjacent directions: UP, DOWN, LEFT, RIGHT
                for move_x, move_y in directions:
                    i, j = x + move_x, y + move_y
                    # Move the adjacent oranges
                    # MAKE SURE it's within boundary
                    if 0 <= i < row and 0 <= j < column and grid[i][j] == 1:
                        grid[i][j] = 2 # Spread the infection
                        next_step_guide.append((i, j))
                        number_of_fresh_oranges -= 1 # Update oranges status
            # Count the time
            minutes_taken += 1

        # Only return time taken when All oranges are rotten (no fresh oranges left) 
        return minutes_taken if number_of_fresh_oranges == 0 else -1
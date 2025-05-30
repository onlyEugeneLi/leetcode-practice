from typing import List
from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        '''
        Intitial intuition (not used in the solution)

        ##### Moves #####

        Up: maze[i - 1][j]
        Down: maze[i + 1][j]
        Left: maze[i][j - 1]
        Right: maze[i][j + 1]

        ##### Border #####

        only if maze[i][j] != '+' (not wall), append the next step

        if i == 0 or j == 0

        '''

        # Directions for moving in 4 possile ways: down, right, up, left
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        rows, cols = len(maze), len(maze[0])
        x0, y0 = entrance # Retrieve starting point coordiantes

        # Use a queue for BFS with (row, col, steps)
        next_moves = deque([(x0, y0)]) # Starting point: first cell to visit
        maze[x0][y0] = '+'  # Mark entrance as visited to prevent re-visiting

        steps_to_exit = 0

        while next_moves:

            for _ in range(len(next_moves)):
                x, y = next_moves.popleft()
                # Explore all four directions
                for dx, dy in directions:
                    new_x, new_y = x + dx, y + dy

                    if 0 <= new_x < rows and 0 <= new_y < cols and maze[new_x][new_y] == '.':
                        # If we reach an exit that is not the entrance
                        if new_x in [0, rows - 1] or new_y in [0, cols - 1]:
                            return steps_to_exit + 1  
                        
                        # Mark cell as visited and add to queue
                        maze[new_x][new_y] = '+'
                        next_moves.append((new_x, new_y))

            steps_to_exit += 1

        return -1
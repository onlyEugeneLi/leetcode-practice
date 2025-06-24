from collections import deque

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        # m x n size
        # Edge case
        # only land or water
        # 0 -- Number of lands or water == total number of nodes 
        row_length = len(grid)
        column_length = len(grid[0])


        # BFS
        # if "1" exists in any of direction --> more lands
        # To check if lands form an island -- explore until bfs_queue empty, count + 1
        def bfs(explored_grid: set[tuple[int, int]], row: int, column: int):
            next_to_explore = deque([(row, column)])
            while next_to_explore:
                x, y = next_to_explore.popleft()
                # detect boundary -- valid coordinates
                # detect land
                if 0 <= x < row_length and 0 <= y < column_length \
                    and grid[x][y] == '1' (i, j) not in explored_nodes:
                    # and grid[x][y] == '1' and explored_grid[x][y] == False:
                    
                    explored_grid.add((x, y))
                    # explored_grid[x][y] = True  # 2nd way to store explored nodes -- Mark as explored
                    next_to_explore.extend([(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)])

        
        # explored_node array to store explored lands
        # Node (row, column)
        explored_nodes = set()

        # 2nd way to store explored nodes: boolean 2D array
        # explored_nodes = [
        #     [False for _ in range(len(grid[0]))] 
        #     for _ in range(len(grid))
        #     ]
        
        if not grid:
            return 0
        
        count = 0
        for i in range(row_length):
            for j in range(column_length):
                if grid[i][j] == '1' and (i, j) not in explored_nodes:
                # if grid[i][j] == '1' and explored_nodes[i][j] == False:
                    count += 1
                    bfs(explored_nodes, i, j) # Cover all lands on current island and make sure we don't revisit

        return count
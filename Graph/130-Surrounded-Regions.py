from collections import deque

class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Initialisation
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)] # RIGHT, LEFT, UP, DOWN
        ROWS, COLS = len(board), len(board[0]) # Num of rows, num of columns

        # Cover all vertices connected to boundary
        self.bfs(ROWS, COLS, board, directions)

        for i in range(ROWS):
            for j in range(COLS):
                # Still 'O' -- Not reached by BFS -- not connected to boundary -- can be surrounded
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                # 'V' -- connected to boundary -- -- cannot be surrounded
                if board[i][j] == 'V':
                    board[i][j] = 'O'

    def bfs(self, ROWS: int, COLS: int, board: list[list[str]], directions: list[tuple]) -> None:
        # next_cell_queue = deque([(coord_row, coord_col)]) # Start from one of cells in the region and then expand
        # Mark 'O' vertices on on the boundary as 'V' (visited)
        vertices_connected_to_boundary = deque([])

        # Mark all boundary 'O' vertices as 'V' as visited
        # To convert back to 'O' at the of processes 
        # Due to being unable to be surrounded
        # left and right boundary
        for r in range(ROWS):
            if board[r][0] == 'O':
                board[r][0] = 'V'
                vertices_connected_to_boundary.append((r, 0))
            if board[r][COLS - 1] == 'O':
                board[r][COLS - 1] = 'V'
                vertices_connected_to_boundary.append((r, COLS - 1))
        # top and bottom boundary
        for c in range(COLS):
            if board[0][c] == 'O':
                board[0][c] = 'V'
                vertices_connected_to_boundary.append((0, c))
            if board[ROWS - 1][c] == 'O':
                board[ROWS - 1][c] = 'V'
                vertices_connected_to_boundary.append((ROWS - 1, c))

        # Breadth-first-search (BFS) all boundary connected vertices and mark them as 'V'
        while vertices_connected_to_boundary:
            x, y = vertices_connected_to_boundary.popleft() # Start checking 1st cell, extracting coordinates
            # if 1 <= x < boundary[0] and 1 <= y < boundary[1] and board[x][y] == 'O':
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < ROWS and 0 <= new_y < COLS and board[new_x][new_y] == 'O': # Debugging line
                    # Change cell from '0' to 'X' in place
                    # board[x][y] = 'O'
                    board[new_x][new_y] = 'V' # Debugging line
                    vertices_connected_to_boundary.append((new_x, new_y))

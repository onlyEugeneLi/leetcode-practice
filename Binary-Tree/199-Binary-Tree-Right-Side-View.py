# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque
from typing import Optional, List
class Solution:
    def rightSideView_1_bfs(self, root: Optional[TreeNode]) -> List[int]:
        # Base case
        if not root:
            return []

        # Variables declaration
        right_side_view = [] # result variable
        children = deque([root]) # next generation from parents; Reset to empty for next level children in every iteration
        parents = deque([]) # Children from previous generation become parents and are used to index to their children 

        while children:
            right_side_view.append(children[0].val)
            parents = children.copy()
            children = deque([])
            while parents:
                node = parents.popleft()
                if node.right:
                    children.append(node.right)
                if node.left:
                    children.append(node.left)


        return right_side_view
    
    def rightSideView_2_bfs(self, root: Optional[TreeNode]) -> List[int]:
        # Base case
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()
                if i == level_size - 1:
                    result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result
    
    def rightSideView_dfs(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(node, depth):
            if not node:
                return

            if depth == len(res):
                res.append(node.val)

            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)

        dfs(root, 0)
        return res
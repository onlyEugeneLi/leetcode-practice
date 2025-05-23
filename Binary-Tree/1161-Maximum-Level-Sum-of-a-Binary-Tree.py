# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
from collections import deque

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        # Initiate variables
        max_sum, level, max_level = -float('inf'), 0, 0
        nodes_on_the_same_level = deque([root])

        while nodes_on_the_same_level:
            level += 1
            sum_nodes_value = 0

            # Sum and compare at each level
            for _ in range(len(nodes_on_the_same_level)): 
                '''
                For-loop cleverly remembers how many nodes each level contains
                '''
                node = nodes_on_the_same_level.popleft()
                sum_nodes_value += node.val
                if node.left:
                    nodes_on_the_same_level.append(node.left)
                if node.right:
                    nodes_on_the_same_level.append(node.right)
            
            # Compare sum of each level
            if max_sum < sum_nodes_value:
                max_level = level
                max_sum = sum_nodes_value

        return max_level
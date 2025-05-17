from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque 

class Solution:
    def longestZigZag_bfs(self, root: Optional[TreeNode]) -> int:
        '''
        BFS method
        Composite queue node: [curr_node, direction, longestdistance]
        '''

        zigzag_length = 0
        bfs_list = deque([[root, 'root', 0]])
        while (len(bfs_list) != 0):
            parent, direction, length = bfs_list.popleft()
            zigzag_length = max(zigzag_length, length)

            if direction == 'root':
                if parent.left:
                    bfs_list.append([parent.left, 'L', 1])
                if parent.right:
                    bfs_list.append([parent.right, 'R', 1])
            else:
                if direction == 'L':
                    if parent.left:
                        bfs_list.append([parent.left, 'L', 1]) # Left -> left ==> reset count
                    if parent.right:
                        bfs_list.append([parent.right, 'R', length + 1]) # Left -> right [ZigZag] ==> count + 1
                if direction == 'R':
                    if parent.left:
                        bfs_list.append([parent.left, 'L', length + 1])
                    if parent.right:
                        bfs_list.append([parent.right, 'R', 1])
        return zigzag_length
    
    def longestZigZag_dfs_1(self, root: Optional[TreeNode]) -> int:
        '''
        DFS method
        Recursive function
        '''
        def dfs(node: TreeNode, left_len: int, right_len: int, max_len: int) -> int:
            if not node:
                return max_len
            max_len = max(max_len, left_len, right_len)
            return max(
                dfs(node.left, 0, left_len + 1, max_len),
                dfs(node.right, right_len + 1, 0, max_len),
            )
        return dfs(root, 0, 0, 0)

    def longestZigZag_dfs_2(self, root: Optional[TreeNode]) -> int:
        # Helper function for DFS traversal
        def dfs(node, curLen, goLeft): 
            '''
            ### Solution link ###
            https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/solutions/6180389/easy-o-n-dfs-python-solution-dfs-direction-toggling

            ### Parameters ###

            goLeft: next step direction signal, gives sign on previous step direction 
                - True (go left now): last step was RIGHT
                - False (go right now): last step was LEFT

            curLen: number of sections

            node: current node
            '''
            if not node:
                return curLen 
            
            if goLeft:
                # If moving left, increment length and toggle to right; reset length if moving right
                return max(dfs(node.left, curLen + 1, False), dfs(node.right, 0, True))
            else: # This step goes RIGHT, because last step was LEFT
                # If moving right, increment length and toggle to left; reset length if moving left
                return max(dfs(node.left, 0, False), dfs(node.right, curLen + 1, True))

        # Start DFS from both left and right subtrees of the root, toggling directions
        return max(dfs(root.left, 0, False), dfs(root.right, 0, True))

'''
Test cases
'''

# The tree structure is now:
#     0
#       \
#        0 (curLen = 0)
#       /
#      0 (curLen = 1)
#       \
#       None (curLen = 2)

root = TreeNode()
root.right = TreeNode()
root.right.left = TreeNode()

# Remember to create an instance of a class before calling its method
# YES: solution = Solution()
# NO: Solution.longestZigZag(root) # TypeError

print(Solution().longestZigZag_dfs_2(root=root))
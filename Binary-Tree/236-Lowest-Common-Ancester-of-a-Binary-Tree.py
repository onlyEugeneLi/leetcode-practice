# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor_1(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Give node a general name node
        node = root 

        '''
        ### Purpose ###

        Pass __None__ or __target node__ to previous tree level (parent resursion call)

        ### Case interpretation ###

        not node: 
            - True(None): return None back to previous tree level
            - False(Not empty): keep checking p & q
        
        node == p / node == q:
            - True(Found input node!): Pass __target node__ back to parent tree level
            - False(Not the one that we're looking for): Keep digging deeper
        '''
        if not node or node == p or node == q:
            return node
         
        '''
        ### Recursion calls ###

        '''
        left_branch_search_result = self.lowestCommonAncestor(node.left, p, q)
        right_branch_search_result = self.lowestCommonAncestor(node.right, p, q)
        
        # Current level search result analysis
        # True: both branches contain the target nodes, this is the LCA
        if left_branch_search_result and right_branch_search_result:
            return node

        # Source back to preivous tiers of the tree with the target node 
        return left_branch_search_result or right_branch_search_result

    '''
    More runtime efficient
    '''
    def lowestCommonAncestor_2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            # Base case: null node
            if not node:
                return None
            
            # If the current node is either p or q, return it
            if node == p or node == q:
                return node
            
            # Recur for left and right children
            left = dfs(node.left)
            right = dfs(node.right)
            
            # If both left and right return a non-null value, current node is LCA
            if left and right:
                return node
            
            # Otherwise, return the non-null child (or null if both are null)
            return left if left else right
        
        # Start the DFS from the root
        return dfs(root)
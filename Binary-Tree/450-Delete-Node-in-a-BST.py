class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        
        if key < root.val: # Key must be on left subtree
            root.left = self.deleteNode(root.left, key) # Jump to next left child
        elif key > root.val: # Key must be on right subtree
            root.right = self.deleteNode(root.right, key) # Jump to next right child
        else: # Current node value == key
            # Case 1: No either of child nodes
            if not root.left and not root.right:
                return None
            # Case 2: No left child
            if not root.left:
                return root.right
            # Case 3: No right child
            if not root.right:
                return root.left
            # Case 4: Both child nodes exist
            # On right subtree, find its bottom left value 
            # to replace current value. 
            # (Thus, Original deletion target is eliminated.)
            root.val = self.findMin(root.right)
            # Delete the duplicate of bottom left node. 
            root.right = self.deleteNode(root.right, root.val)
        
        return root

    def findMin(self, root: TreeNode) -> int:
        # findMin(root.right, root.right.bottom_left.val)
        # CurrNode = bottom_left: 
        # bottom_left value > all values on left subtree
        # bottom_left value < all values on right subtree
        # -> Binary search tree structure is still valid. 
        while root.left:
            root = root.left
        return root.val
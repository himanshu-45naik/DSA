# Print Root to node path
from typing import Optional

# Definition of Tree
class TreeNode:
    def __init__(self, val= 0, left=None, right= None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def root_2_node_path(self, root: Optional[TreeNode], node: int):

        res = []

        def inorder(root: Optional[TreeNode], res, node: int):

            if not root:
                return False

            res.append(root.val) # Add current to potential path

            if root.val == node:
                return True      # If the given node is equal to target then return

            if inorder(root.left, res, node) or inorder(root.right, res, node):
                return True      # Check if left and right subtree exits, if yes traverse them
            
            # Backtrack -> If the node wasn't found in either child path, 
            # remove the current node from the path and signal failure
            res.pop()
            return False

        inorder(root, res, node)
        return res
    
if __name__ == "__main__":
    s = Solution()

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.right.left = TreeNode(6)
    root.left.right.right = TreeNode(7)

    node = 7

    print(s.root_2_node_path(root, node))
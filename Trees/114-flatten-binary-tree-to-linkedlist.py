# 114. Flatten Binary Tree to Linkedlist

# Definition for a binary tree node.

from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        # Recursion solution
        # We will move subtree of the tree in this order -> right -> left -> root
        # Visualizeing -> We are flattening the tree inplace from the bottom of 
        # This will ensure that the prev is always has the right side of the tree and when we make changes it the left the right will be added acccordingly

        self.prev = None

        def tree_2_linkedlist(node):
            if not node:
                return None

            tree_2_linkedlist(node.right)
            tree_2_linkedlist(node.left)

            node.right = self.prev
            node.left = None
            self.prev = node


        
        return root
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.left.right = TreeNode(5)
    root.right = TreeNode(3)
    root.right.left = TreeNode(9)
    root.right.right = TreeNode(11)
    root.right.right.left = TreeNode(10)

    s = Solution()
    print(s.flatten(root))
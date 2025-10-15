# 110 Balanced Binary Tree

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """Returns true if the given tree is balanced otherwise false.

        Args:
            root (Optional[TreeNode]): ROot of the given tree.

        Returns:
            bool: Returns true if the tree is balanced otherwise false.
        """

        # Approach
        # Iterative -- We will find rh and lh        
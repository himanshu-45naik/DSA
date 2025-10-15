# 104. Maximum Depth of Binary Tree

from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """The goal is to find the height/dept of the tree.

        Args:
            root (Optional[TreeNode]): The root of the given tree.

        Returns:
            int: The height of the tree.
        """
        
        if root == None:
            return 0
        
        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)
        
        return 1 + max(left_height, right_height)
# 101 Symmetric Tree

from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """Returns true if the the tree is symmetric otherwise False.

        Args:
            root (Optional[TreeNode]): Root of the given tree.

        Returns:
            bool: True if symmetric otherwise False.
        """
        
        def check_symmetry(curr_root1, curr_root2):
            
            if curr_root1 == None or curr_root2 == None:
                return curr_root1 == curr_root2
            
            return (curr_root1.val == curr_root2.val) and check_symmetry(curr_root1.right, curr_root2.left) and check_symmetry(curr_root1.left, curr_root2.right)

        return check_symmetry(root.left, root.right)
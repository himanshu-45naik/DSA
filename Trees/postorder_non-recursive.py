# 145. Binary Tree Postorder Traversal

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        """Postorder traversal of binary tree.

        Args:
            root (Optional[TreeNode]): The root of the tree.

        Returns:
            list[int]: List of  traversed node.
        """
        
        # Approach-
        # Traversal in postorder tree - Left-> Right -> Root
        # We will use 2 stacks -
        # In one stack we will push the 
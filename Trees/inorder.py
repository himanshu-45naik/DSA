# Binary Tree inorder Traversal

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        """Implementing inorder traversal of the binary tree.

        Args:
            root (Optional[TreeNode]): The root of the binary tree.

        Returns:
            list[int]: List of traversed nodes.
        """

        # Approach
        # Left -> Root -> Right

        def traverse(arr, curr_node):

            if curr_node.left:
                traverse(arr, curr_node.left)

            arr.append(curr_node.val)

            if curr_node.right:
                traverse(arr, curr_node.right)

            return arr

        arr = []
        return traverse(arr, root)

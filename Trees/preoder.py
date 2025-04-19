# Binary Tree Preorder Traversal
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        """Given the root of a binary tree, return the preorder traversal of its nodes' values.

        Args:
            root (Optional[TreeNode]): The root of the tree.

        Returns:
            list[int]: The list of preoder traversed nodes.
        """

        # Preorder Traversal --> Root Left Right
        # We will first add the root to the node then the Left node and then the right node.

        if root == None:
            return None

        curr_root = root
        result = []

        while curr_root:

            result.append(curr_root.val)

            if curr_root.left:
                self.preorderTraversal(curr_root.left)
            if curr_root.right:
                self.preorderTraversal(curr_root.right)

        return result

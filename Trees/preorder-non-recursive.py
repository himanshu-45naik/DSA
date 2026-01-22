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

        res = []
        if not root:
            return res
            
        stk = []
        stk.append(root)
        
        while stk:
            node = stk.pop(-1)
            res.append(node.val)
            if node.right:
                stk.append(node.right)
            if node.left:
                stk.append(node.left)

        return res


if __name__ == "__main__":

    s = Solution()

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.right.right = TreeNode(6)
    root.right = TreeNode(3)

    print(s.preorderTraversal(root))
    
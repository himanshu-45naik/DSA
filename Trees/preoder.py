# Binary Tree Preorder Traversal
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        res = []

        if not root:
            return res
        
        def preorder(node, res):
            if not root:
                return None

            res.append(node.val)
            if node.left:
                preorder(node.left, res)
            if node.right:
                preorder(node.right, res)

            return res

        return preorder(root, res)

if __name__ == "__main__":

    s = Solution()

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.right.right = TreeNode(6)
    root.right = TreeNode(3)

    print(s.preorderTraversal(root))
    
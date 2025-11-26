# Binary Tree inorder Traversal

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    # Main function to call
    def maxPathSum(self, root):
        self.max_sum = float('-inf')
        self.dfs(root)
        return self.max_sum

    # Recursive DFS helper
    def dfs(self, node):
        if not node:
            return 0

        # Recursively find left and right max path sum
        left = max(0, self.dfs(node.left))
        right = max(0, self.dfs(node.right))

        # Update max sum if path through node is better
        self.max_sum = max(
            self.max_sum,
            left + right + node.val
        )

        # Return one-sided path
        return max(left, right) + node.val
    
if __name__ == "__main__":
    root = TreeNode(-10)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    s = Solution()
    print(s.maxPathSum(root))
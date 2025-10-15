# 104. Maximum Depth of Binary Tree

from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """The goal is to find the height/dept of the tree.

        Args:
            root (Optional[TreeNode]): The root of the given tree.

        Returns:
            int: The height of the tree.
        """
        if not root:
            return 0
        
        depth = 0
        queue = deque([root])
        
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth += 1
        
        return depth

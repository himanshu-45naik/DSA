# 102. Binary Tree Level Order Traversal

from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        """Implement level order traversal.

        Args:
            root (Optional[TreeNode]): The root of the tree.

        Returns:
            list[list[int]]: The list of traversed nodes.
        """
        
        # Approach-
        # As we know we have to traverse the tree breadth wise.
        # We will use the queue data structure.
        # We will push the root node onto the queue, lets say the root is 3.  queue = [3]
        # Now for this node, if there is a right or left node then push it into the queue and pop 3, lets say 3.left=9 and 3.right=20. queue = [9,20]
        # Similaarly now chech if there is right and left node for 9 and 20, lets say 9 has none and 20.left = 15 & 20.right = 7. queue = [15, 7]
        # The final output is ==> [[3],[9,20],[15,7]]
        
        res = []
        q = deque([root])
        
        while q:
            level = [] # Here we will store nodes for each level
            for i in range(0, len(q)):
                node = q.popleft()
                level.append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
            res.append(level)
            
        return res
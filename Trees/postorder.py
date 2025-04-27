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
        
        curr_node = root
        traversed = []
        
        def traversal(curr_node: TreeNode, traversed: list):
            
            if curr_node.left:
                traversal(curr_node.left, traversed) 
            if curr_node.right:
                traversal(curr_node.right, traversed)
            
            traversed.append(curr_node.val)
            
        traversal(curr_node,traversed)
        
   
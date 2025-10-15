# Definition for a binary tree node.

from typing import Optional

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
       
        curr_node = root
        result = []
        stk = []
        
        while curr_node or stk:
            while curr_node:
                stk.append(curr_node)
                curr_node = curr_node.left
            
            curr_node = stk.pop()
            result.append(curr_node.val)
            
            curr_node = curr_node.right
        
        return result
                
        
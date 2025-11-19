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
        # We will follow to approach similar to  Preorder traversal here. Remember preorder is Root-Left-Right
        # We will use modified preorder : Root-Right-Left
        # In reverse it is a Postorder traversal.
        # We will use 2 stacks - Stk1 is the modified preorder traversal tool
        # Stk2 is used to store history for keeping track of nodes already visited.
        # In one stack we will push the 

        stk1 = []
        stk2 = []

        if not root:
            return stk2
        
        stk1.append(root)

        while stk1:
            root = stk1.pop()
            stk2.append(root)

            if root.left:
                stk1.append(root.left)
            if root.right:
                stk1.append(root.right)
            
        return stk2[::-1]

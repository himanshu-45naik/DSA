# 543. Diameter of binary tree

from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """Return length of diameter of binary tree.
        Here diameter stands for the longhest lenght of the two distant node.
        Path does not necessarily has to pass via root.
        
        Args:
            root (Optional[TreeNode]): The root of the given binary tree.

        Returns:
            int: The diameter of the binary tree.
        """
            
        # Approach
        # We will find the left height and right height for each node.
        # Then out of this we will select the maximum left height and right height
        # Return the sum of this maximum left height and right height.
        
        def findmax(root, maxi):
            if root == None:
                return 0
            
            lh = findmax(root.left, maxi)
            rh = findmax(root.right, maxi)
            
            maxi = max(maxi, lh + rh)
            
            return 1 + max(rh, lh)
        diameter = 0
        diameter = findmax(root, diameter)
        
        return diameter
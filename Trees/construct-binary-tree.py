# 106. Construct Binary Tree from Inorder and Postorder Traversal

from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> Optional[TreeNode]:
        """Construct a binary tree using given preorder and postorder traversal.

        Args:
            inorder (list[int]): Given inoder traversal.
            postorder (list[int]): Given preorder traversal.

        Returns:
            Optional[TreeNode]: The onstructed binary tree.
        """
        
        # Approach
        # We will first find the root with the postorder traversal. Here it is 10. -> postorder = [40, 50, 20, 60, 30, 10]
        # Now we will check this root node in the inorder traversal, so that the left part is the left subtree and right elements are the 
        # Basically the idea is that the node at right of the root is the left subtree and at right is the right subtree.
        # Recursively we will call the buildtrree function to ultimately build the binary tree.
        
        # Create a map to quickly find root index in the inorder traversal
        inorder_index_map = {val: idx for idx, val in enumerate(inorder)}
        
        def helper(inleft, inright):
            # Base case: no elements to construct subtrees
            if inleft > inright:
                return None
            
            # Step 2: Pick the last element in postorder as the root
            root_val = postorder.pop()
            root = TreeNode(root_val)
            
            # Step 3: Root splits inorder into left and right subtrees
            index = inorder_index_map[root_val]
            
            # Step 4: Build right subtree first (since we're popping from end)
            root.right = helper(index + 1, inright)
            # Step 5: Then build left subtree
            root.left = helper(inleft, index - 1)

            return root

        return helper(0, len(inorder) - 1)
    
        
# Example input lists
inorder = [40, 20, 50, 10, 60, 30]
postorder = [40, 50, 20, 60, 30, 10]

s = Solution()
s.buildTree(inorder, postorder)
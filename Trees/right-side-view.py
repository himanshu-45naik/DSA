# Definition for a binary tree node.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        """Implement a program which returns the nodes of the tree which are visible from the right side.

        Args:
            root (Optional[TreeNode]): The root of the tree.

        Returns:
            list[int]: The list of nodes that are visible from the right side.
        """
        
        # If we traverse from right to left at each level than the first node  will be our answer.
        # We wont do level order traversal because
        # We can't implement the iterative (level order traversal) approach becoz it will take  most of the nodes
        # space cpmplexity will be high for iterative approach
        # while for iterative approach the space complexity will be O(H).
        # We will follow the path --> Root - Right - Left
        # We will also store the level - each time we will access new level we will store the element.
        # As the first element is the one we see from the right. We will push this node to the queue.
        # As we are filling the queue, the length we also go on increasing.
        # The length of the queue will be equal to the level for the right-most node.
        
        def visible_nodes(curr_node, level, right_side):
            if curr_node == None:
                return []
            
            if level == len(right_side):
                right_side.append(curr_node.val)
            
            visible_nodes(curr_node.right, level+1, right_side)
            visible_nodes(curr_node.left, level+1, right_side)
            
            return right_side
        
        return visible_nodes(root, 0, [])
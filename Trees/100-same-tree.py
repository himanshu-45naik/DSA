# 100. Same Tree

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        
        # Use a traversal and compare the nodes of each tree at the same time
        # If different then return True
        # Else false

        if not p and not q:
            return True

        if not p or not q or p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)



if __name__ == "__main__":

    s = Solution()

    p = TreeNode(1)
    p.right = TreeNode(3)
    p.left = TreeNode(2)

    q = TreeNode(1)
    q.right = TreeNode(3)
    q.left = TreeNode(2) 

    print(s.isSameTree(p, q))
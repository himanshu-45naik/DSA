# Definition for a binary tree node.

from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if not root:
            return None
        curr = root

        while curr:
            
            if val == curr.val:
                return curr

            if val < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        
        return None

if __name__ == "__main__":
        
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(13)
    root.left.left = TreeNode(3)
    root.left.left.left = TreeNode(2)
    root.left.left.right = TreeNode(4)
    root.left.right = TreeNode(6)
    root.left.right.right = TreeNode(9)
    root.right.left = TreeNode(11)
    root.right.right = TreeNode(14)
    val = 3

    s = Solution()
    print(s.searchBST(root, val))
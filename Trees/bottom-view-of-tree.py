# Bottom view of the Tree

from collections import defaultdict
from queue import Queue

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bottom_view_of_tree(self, root: TreeNode)-> list:

        # We will use the concept of line of order
        # We will map each line a node, the node at the bottom of the line  is our result.
        # Logic:
        # Follow level order traversal -> thus use a queue
        # Using a map data structure, map each node to a line, such that the bottom most appeats in the final output
        
        mapped = defaultdict(int)
        result = []
 
        if not root:
            return result
        
        q = Queue()
        q.put((root, 0))

        while not q.empty():
            node , line = q.get()

            mapped[line] = node.val
            if node.left:
                q.put((node.left, line-1))
            if node.right:
                q.put((node.right, line+1))

        for key, value in sorted(mapped.items()):
            result.append(value) 
        
    

        return result

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.left.right = TreeNode(5)
    root.right = TreeNode(3)
    root.right.left = TreeNode(9)
    root.right.right = TreeNode(11)
    root.right.right.left = TreeNode(10)

    s = Solution()
    print(s.bottom_view_of_tree(root))
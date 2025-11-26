from collections import defaultdict, deque
from queue import Queue
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> list[list[int]]:

        # Lets say 2 elements are just below line 0 and has the same column.
        # In this case we wont add left subtrees node first and right subtrees node next
        # Instead we will add it in sorted order. Thus store node, row, columns
        node_list = defaultdict(list)
        
        queue = Queue()
        # Queue stores: (node, row, col)
        queue = deque([(root, 0, 0)])
        
        while queue:
            node, row, col = queue.popleft()
            
            node_list[col].append((row, node.val))
            
            if node.left:
                queue.append((node.left, row + 1, col - 1))
            if node.right:
                queue.append((node.right, row + 1, col + 1))
        
        # - When we sort arrays like → list[list], list[tuple]
        # - Example → list = [(1, 2), (1, 3), (0, 4)]
        # - list.sort() ⇒ [(0, 4), (1, 2), (1,3)]
        # - When sorting the list checks the first element of the tuple for sorting.
        # - If the first element is same for one or more elements, 2nd element of the tuple is checked.
        sorted_keys = sorted(node_list.keys())
        
        res = []
        for col in sorted_keys:
            
            node_list[col].sort()
            
            
            col_values = [val for row, val in node_list[col]]
            res.append(col_values)
            
        return res
    
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
    print(s.verticalTraversal(root))
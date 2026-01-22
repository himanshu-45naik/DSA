# 589. N-ary Tree Preorder Traversal


# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        # --------------------- iterative approach ------------------- #
        # res = []

        # if not root:
        #     return res
            
        # stk = []
        # stk.append(root)

        # while stk:
        #     node = stk.pop(-1)
        #     res.append(node.val)

        #     if node.children:
        #         n = len(node.children) - 1
        #         for i in range(n, -1, -1):
        #             stk.append(node.children[i])

        # return res

        # --------------------- recursive approach ------------------- #

        res = []

        def preorder(node):
            if not node:
                return None
            
            res.append(node.val)
            
            if node.children:
                n = len(node.children) - 1
                for i in range(n, -1, -1):
                    preorder(node.children[i])
            return res
    

        return preorder(root)
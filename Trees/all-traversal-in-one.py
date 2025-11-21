# Implementing All Traversal using One Stack.

class Node:
    # Constructor to initialize the node with a value
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def all_travarsal(self, root: Node)-> tuple[list,list,list]:
        preorder = []
        inorder = []
        postorder = []

        stk = []
        stk.append([root, 1])

        while stk:
            top = stk.pop()

            if top[1] == 1:
                preorder.append(top[0].val)
                top[1] = 2
                stk.append(top)
                if top[0].left: 
                    stk.append([top[0].left, 1])
            elif top[1] == 2:
                inorder.append(top[0].val)
                top[1] = 3
                stk.append(top)
                if top[0].right:
                    stk.append([top[0].right, 1])
            else:
                postorder.append(top[0].val)

        return preorder, inorder, postorder

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(4)
    root.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    s = Solution()
    print(s.all_travarsal(root))
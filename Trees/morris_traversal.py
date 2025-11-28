# Morris Traversal

from collections import deque

class TreeNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def morris_inorder_traversal(self, root):

        # Left -> Root -> Right

        inorder = deque()
        curr = root
        while curr != None:
                
            # If there is no left, then push root onto stack.
            if curr.left == None:
                inorder.append(curr.val)
                curr = curr.right
            else:       # If left exists, make threaded connection of the subtree to the curr
                # Find the right most node to create a threaded connection with the root (curr)
                prev = curr.left
                # Find the right most node
                while prev.right and prev.right != curr:
                    prev = prev.right
                    
                # Make the connection with the rightmost node found in the last while loop
                if prev.right == None:
                    prev.right = curr
                    # Now move to left from the curr node (root)
                    curr = curr.left
                else:   # Meaning this prev.right (threaded connection) is used and now we have to remove it -> dry run and understand
                    prev.right = None
                    inorder.append(curr.val)    # This is the curr(root) we reached using the threaded connection
                    curr = curr.right   # Since we reached the curr from the left subtree,now we traverse the right subtree.

        print("Inorder: ")  
        return list(inorder)

    def morris_preorder_traversal(self, root):

        # Left -> Root -> Right

        preorder = deque()
        curr = root
        while curr != None:
                
            # If there is no left, then push root onto stack.
            if curr.left == None:
                preorder.append(curr.val)
                curr = curr.right
            else:       # If left exists, make threaded connection of the subtree to the curr
                # Find the right most node to create a threaded connection with the root (curr)
                prev = curr.left
                # Find the right most node
                while prev.right and prev.right != curr:
                    prev = prev.right
                    
                # Make the connection with the rightmost node found in the last while loop
                if prev.right == None:
                    prev.right = curr
                    preorder.append(curr.val)    # This is the curr(root) we reached using the threaded connection
                    # Now move to left from the curr node (root)
                    curr = curr.left
                else:   # Meaning this prev.right (threaded connection) is used and now we have to remove it -> dry run and understand
                    prev.right = None
                    curr = curr.right   # Since we reached the curr from the left subtree,now we traverse the right subtree.
        print("Preorder: ")
        return list(preorder) 

        
if __name__ == "__main__":

    s = Solution()

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.right.right = TreeNode(6)
    root.right = TreeNode(3)

    print(s.morris_inorder_traversal(root))
    print(s.morris_preorder_traversal(root))


# Find Ceil in binary search tree

# Definition of TreeNode structure
# for a binary tree node
class TreeNode:
    # Constructor to initialize the node with a
    # value and set left and right pointers to null
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # Function to find the ceiling of
    # a key in a Binary Search Tree (BST)
    def findCeil(self, root, key):
        # Initialize the variable
        # to store the ceiling value
        ceil = -1
        
        # Traverse the BST until reaching
        # the end or finding the key
        while root:
            # If the key is found, assign it
            # as the ceiling and return
            if root.val == key:
                ceil = root.val
                return ceil
            
            # If the key is greater,
            # move to the right subtree
            if key > root.val:
                root = root.right
            else:
                # If the key is smaller, update ceil
                # and move to the left subtree
                ceil = root.val
                root = root.left
        
        # Return the computed ceiling value
        return ceil

# Function to perform an in-order traversal
# of a binary tree and print its nodes
def printInOrder(root):
    # Check if the current node
    # is null (base case for recursion)
    if not root:
        # If null, return and
        # terminate the function
        return
    
    # Recursively call printInOrder
    # for the left subtree
    printInOrder(root.left)
    
    # Print the value of the current node
    print(root.val, end=" ")
    
    # Recursively call printInOrder
    # for the right subtree
    printInOrder(root.right)

# Creating a BST
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

print("Binary Search Tree:")
printInOrder(root)
print()

solution = Solution()

# Searching for a value in the BST
target = 8
ceil = solution.findCeil(root, target)

if ceil != -1:
    print(f"Ceiling of {target} is: {ceil}")
else:
    print("No ceiling found!")
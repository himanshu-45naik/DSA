# 297. Serialize and Deserialize Binary Tree

from queue import Queue

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = ""

        # If there is no tree
        if not root:
            return res

        # For level order traversal use queue
        queue = Queue()
        queue.put(root)

        # Add the root's value to the resulting string.
        res += str(root.val) + ","

        # Implementing level order traversal
        while not queue.empty():
            curr_node = queue.get()
        
            if curr_node.left:
                res += str(curr_node.left.val) + ","
                queue.put(curr_node.left)
            else:   # If the child node is Null, the result will hold # in place of the node (coded)
                res += "#,"
            
            if curr_node.right:
                res += str(curr_node.right.val) + ","
                queue.put(curr_node.right)
            else:   # If the child node is Null, the result will hold # in place of the node (coded)
                res += "#,"

        return res        
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # Edge case if empty tree
        if not data:
            return None

        # Split the data wrt to , and turn it into a list.
        ls = data.split(",")
        
        # Create the tree root using first node.
        root = TreeNode(int(ls[0]))

        # A queue data structure to store the curr_node
        q = Queue()
        q.put(root)

        i = 1
        while not q.empty() and i < len(ls) - 1:
            curr_node = q.get()

            if ls[i] != "#":
                curr_node.left = TreeNode(int(ls[i]))
                q.put(curr_node.left)
            i += 1
            if ls[i] != "#":
                curr_node.right = TreeNode(int(ls[i]))
                q.put(curr_node.right)
            i += 1
            
        return root

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)

    ser = Codec()
    deser = Codec()
    ans = deser.deserialize(ser.serialize(root))
    print("Serialized: ",ser.serialize(root))
    print(ans)
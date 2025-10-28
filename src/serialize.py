# serialize.py

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
    """Serialize a binary tree into a string using pre-order traversal."""
    if root is None:
        return '#'
    return f"{root.val} {serialize(root.left)} {serialize(root.right)}"

def deserialize(data):
    """Deserialize a string into a binary tree."""
    tokens = data.split()
    
    def helper(it):
        try:
            val = next(it)
        except StopIteration:
            return None
        if val == '#':
            return None
        # Try to convert to int if possible
        try:
            val_cast = int(val)
        except ValueError:
            val_cast = val
        node = Node(val_cast)
        node.left = helper(it)
        node.right = helper(it)
        return node
    
    return helper(iter(tokens))

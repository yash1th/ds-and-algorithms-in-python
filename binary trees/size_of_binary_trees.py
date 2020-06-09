class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)
    
    def size_recursive_approach(self, node):
        if node is None:
            return 0
        return 1 + self.size_recursive_approach(node.left) + self.size_recursive_approach(node.right)
    

    def size_iterative_approach(self, start):
        queue = []
        size = 0
        
        if start is None:
            return 0
        queue.append(start)
        size += 1

        while len(queue) > 0:
            node = queue.pop()

            if node.left:
                size += 1
                queue.append(node.left)
            
            if node.right:
                size += 1
                queue.append(node.right)
        
        return size

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

print(tree.size_recursive_approach(tree.root))
print(tree.size_iterative_approach(tree.root))
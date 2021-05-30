class Node:

    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class BinaryTree:

    def __init__(self):
        self.root = None

    def preOrder(self):
        if not self.root:
            return 'no data '
        res = []
        def _walk(node):
            res.append(node.value)
            if node.left:
                _walk(node.left)
            if node.right:
                _walk(node.right)
        _walk(self.root)
        return res

    def inOrder(self):
        if not self.root:
            return 'no data'
        res = []
        def _walk(node):           
            if node.left:
                _walk(node.left)
            res.append(node.value)
            if node.right:
                _walk(node.right)
        _walk(self.root)
        return res        

    def postOrder(self):
        if not self.root:
            return 'No data'
        res = []
        def _walk(node):            
            if node.left:
                _walk(node.left)
            if node.right:
                _walk(node.right)
            res.append(node.value)
        _walk(self.root)
        return res
    
    def find_maximum_value(self):
        if not self.root:
            return 'No data'
        max=self.root.value
        def _walk(node):
            nonlocal max
            if node.value>max:
                max=node.value
            if node.left:
                _walk(node.left)
            if node.right:
                _walk(node.right)
            return max
        return _walk(self.root)
         

class BinarySearchTree(BinaryTree):

    def add(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            def _walk(node):
                if value < node.value:
                    if not node.left:
                        node.left = Node(value)
                        return
                    else:
                        _walk(node.left)
                else:
                    if not node.right:
                        node.right = Node(value)
                        return
                    else:
                        _walk(node.right)
            _walk(self.root)

    def contains(self, value):
        if not self.root:
            return False
        def _walk(node):
            if node:
                if node.value==value:
                    return True
                elif value<node.value:
                    return _walk(node.left)
                elif value>node.value:
                    return _walk(node.right) 
            return False           
        return _walk(self.root)
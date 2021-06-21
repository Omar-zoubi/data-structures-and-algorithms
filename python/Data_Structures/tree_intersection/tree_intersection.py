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
def tree_intersection(t_one,t_tow):
    result=[]
    if t_one.root and t_tow.root:
        first_tree=t_one.preOrder()
        second_tree=t_tow.preOrder()       
        for i in first_tree:
            if i in second_tree:
                result.append(i)
    if result :
        return result
    else:
        return "No Mach Found"


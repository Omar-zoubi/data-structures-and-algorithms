import pytest
from code_challenges.Data_Structures.Tree.tree_all import Tree_Node,BinaryTree,EmptyTreeException
def test_breadth_first_one():
    expected = [2,7,5,2,6,9,5,11,4]
    node1 = Tree_Node(2) 
    node1.left = Tree_Node(7) 
    node1.right = Tree_Node(5) 
    node1.left.left = Tree_Node(2) 
    node1.left.right = Tree_Node(6) 
    node1.right.right = Tree_Node(9) 
    node1.left.right.left = Tree_Node(5) 
    node1.left.right.right = Tree_Node(11)
    node1.right.right.left = Tree_Node(4) 
    binary_tree = BinaryTree(node1)
    actual = binary_tree.breadth_first(binary_tree)
    assert actual == expected
def test_breadth_first_two():
    expected = [3,8,5,2,6,10,9,24,34,5,11,4,16]
    node1 = Tree_Node(3) 
    node1.left = Tree_Node(8) 
    node1.right = Tree_Node(5)
    node1.left.left = Tree_Node(2) 
    node1.left.right = Tree_Node(6) 
    node1.right.left = Tree_Node(10) 
    node1.right.right = Tree_Node(9) 
    node1.left.left.left = Tree_Node(24) 
    node1.left.left.right = Tree_Node(34) 
    node1.left.right.left = Tree_Node(5) 
    node1.left.right.right = Tree_Node(11)
    node1.right.right.left = Tree_Node(4) 
    node1.right.right.right = Tree_Node(16) 
    binary_tree = BinaryTree(node1)
    actual = binary_tree.breadth_first(binary_tree)
    assert actual == expected
def test_breadth_first_empty():
    with pytest.raises(EmptyTreeException):
        binary_tree = BinaryTree()
        binary_tree.breadth_first(binary_tree)






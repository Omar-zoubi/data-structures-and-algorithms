from code_challenges.Data_Structures.BinaryTree.BinaryTree import *

def test_single_tree():
    obj1 = BinarySearchTree()
    obj1.add(10)
    expected = 10
    actual = obj1.root.value
    assert actual == expected

def test_add_tree():
    bst = BinarySearchTree()
    bst.add(5)
    expected = 5
    actual = bst.root.value
    assert actual == expected

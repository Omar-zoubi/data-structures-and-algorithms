from code_challenges.Data_Structures.BinaryTree.BinaryTree import *
def test_init_tree():
    obj1 = BinarySearchTree()
    obj1.add(5)
    obj1.add(11)
    obj1.add(1)
    obj1.add(4)
    obj1.add(3)
    obj1.add(6)
    obj1.add(2)
    actual = obj1.root.value
    expected = 5 
    assert actual==expected

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


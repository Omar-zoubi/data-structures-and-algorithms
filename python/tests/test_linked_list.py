# import pytest
# from Data_Structures.linked_list.linked_list import *

# def test_insert(testing_fun):
#     excpected = "{'Al-zoubi'} -> {'Mohammad'} -> {'Omar'} -> NULL"
#     # actual = f'{testing_fun}'
#     actual = testing_fun.__str__()
#     assert excpected == actual

# def test_include(testing_fun):
#     actual = [testing_fun.include('Omar'),testing_fun.include('mohaaa')]
#     excpected = [True, False]
#     assert excpected == actual
# def test_magic(testing_fun):
#     actual = testing_fun.__str__()
#     excpected = "{'Al-zoubi'} -> {'Mohammad'} -> {'Omar'} -> NULL"
#     assert excpected == actual



# def test_append() : 
#     llist = Linked_list()
#     llist.append(1)
#     llist.append(2)
#     llist.append(3)
#     excpected = "{'1'} -> {'2'} -> {'3'} -> NULL"
#     actual = llist.__str__()
#     assert excpected == actual

# def test_insert_before():
#     llist=Linked_list()
#     llist.insert(1)
#     llist.insert(2)
#     llist.insert(4)
#     llist.insert(5)
#     llist.insert_before(4,3)
#     excpected = "{'1'} -> {'2'} -> {'3'} -> {'4'} -> {'5'} -> NULL"
#     actual = llist.__str__()
#     assert excpected == actual

# def test_insert_before_first():
#     llist=Linked_list()
#     llist.insert(2)
#     llist.insert(3)
#     llist.insert(4)
#     llist.insert(5)
#     llist.insert_before(2,1)
#     excpected = "{'1'} -> {'2'} -> {'3'} -> {'4'} -> {'5'} -> NULL"
#     actual = llist.__str__()
#     assert excpected == actual
# def test_insert_after_mid():
#     llist=Linked_list()
#     llist.insert(1)
#     llist.insert(2)
#     llist.insert(3)
#     llist.insert(4)
#     llist.insert_after(4,5)
#     excpected = "{'1'} -> {'2'} -> {'3'} -> {'4'} -> {'5'} -> NULL"
#     actual = llist.__str__()
#     assert excpected == actual



# def test_k_lagerthan_length():
#     llist=Linked_list()
#     llist.insert(1)
#     llist.insert(2)
#     llist.insert(3)
#     llist.insert(4)
#     excpected = 'Invalid Index'
#     actual = llist.kthFromEnd(5)
#     assert excpected == actual

# def test_k_same_length():
#     llist=Linked_list()
#     llist.insert(1)
#     llist.insert(2)
#     llist.insert(3)
#     llist.insert(4)
#     excpected = 1
#     actual = llist.kthFromEnd(3)
#     assert excpected == actual

# def test_k_not_positive_int():
#     llist=Linked_list()
#     llist.insert(1)
#     llist.insert(2)
#     llist.insert(3)
#     llist.insert(4)
#     excpected = 'Invalid Index'
#     actual = llist.kthFromEnd(-1)
#     assert excpected == actual

# def test_one_index():
#     llist=Linked_list()
#     llist.insert(1)
#     excpected = 1
#     actual = llist.kthFromEnd(0)
#     assert excpected == actual


# def test_k_same_length():
#     llist=Linked_list()
#     llist.insert(1)
#     llist.insert(2)
#     llist.insert(3)
#     llist.insert(4)
#     llist.insert(5)
#     llist.insert(6)
#     excpected = 4
#     actual = llist.kthFromEnd(2)
#     assert excpected == actual



# @pytest.fixture
# def testing_fun():
#     llist = Linked_list()
#     llist.insert('Al-zoubi')
#     llist.insert('Mohammad')
#     llist.insert('Omar')
#     return llist
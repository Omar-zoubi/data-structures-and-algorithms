  
import pytest
from Data_Structures.linked_list.linked_list import *

def test_insert(testing_fun):
    excpected = "{Al-zoubi} -> {Mohammad} -> {Omar} ->  NULL"
    # actual = f"{testing_fun}"
    actual = testing_fun
    assert excpected == actual

def test_include(testing_fun):
    actual = [testing_fun.include("Omar"),testing_fun.include("mohaaa")]
    excpected = [True, False]
    assert excpected == actual
def test_magic(testing_fun):
    actual = print(testing_fun)
    excpected = "{Al-zoubi} -> {Mohammad} -> {Omar} ->  NULL"
    assert excpected == actual



def test_append() : 
    llist=LinkedList
    llist.append(1)
    llist.append(2)
    llist.append(3)
    excpected = "{1} -> {2} -> {3} ->  NULL"
    actual = llist.__str__()
    assert excpected == actual

def test_insert_before():
    llist=LinkedList
    llist.insert(1)
    llist.insert(2)
    llist.insert(4)
    llist.insert(5)
    llist.insert_before(4,3)
    excpected = "{1} -> {2} -> {3} -> {4} -> {5} ->  NULL"
    actual = llist.__str__()
    assert excpected == actual

def test_insert_before_first():
    llist=LinkedList
    llist.insert(2)
    llist.insert(3)
    llist.insert(4)
    llist.insert(5)
    llist.insert_before(2,1)
    excpected = "{1} -> {2} -> {3} -> {4} -> {5} ->  NULL"
    actual = llist.__str__()
    assert excpected == actual
def test_insert_after_mid():
    llist=LinkedList
    llist.insert(1)
    llist.insert(2)
    llist.insert(3)
    llist.insert(4)
    llist.insert_after(4,5)
    excpected = "{1} -> {2} -> {3} -> {4} -> {5} ->  NULL"
    actual = llist.__str__()
    assert excpected == actual

@pytest.fixture
def testing_fun():
    llist = Linked_list()
    llist.insert("Omar")
    llist.insert("Mohammad")
    llist.insert("Al-zoubi")
    return llist
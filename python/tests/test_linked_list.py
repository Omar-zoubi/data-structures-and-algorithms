import pytest
from code_challenges.Data_Structures.linked_list.linked_list import *

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


@pytest.fixture
def testing_fun():
    llist = Linked_list()
    llist.insert("Omar")
    llist.insert("Mohammad")
    llist.insert("Al-zoubi")
    return llist
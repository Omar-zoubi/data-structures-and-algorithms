import pytest
from linked_list.linked_list import *

def test_insert(testing_fun):
    excpected = "{Al-zoubi} -> {Mohammad} -> {Omar} ->  NULL"
    # actual = f"{testing_fun}"
    actual = testing_fun
    assert excpected == actual

def test_include(testing_fun):
    actual = [testing_fun.include("Omar"),testing_fun.include("mohaaa")]
    excpected = [True , False]
    assert excpected == actual


@pytest.fixture
def testing_fun():
    llist = Linked_list()
    llist.insert("Omar")
    llist.insert("Mohammad")
    llist.insert("Al-zoubi")
    return llist
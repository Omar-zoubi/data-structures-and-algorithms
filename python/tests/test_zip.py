import pytest
from Data_Structures.ll_zip.ll_zip import *

def test_zip():
    excpected = "{o} -> {m} -> {a} -> {r} -> NULL"
    # actual = f"{testing_fun}"
    li = Linked_list()
    li2 = Linked_list()
    li.insert('o')
    li.insert('a')
    li2.insert('m')
    li2.insert('r')
    zipLists(li,li2)
    actual = print(zipLists(li,li2))
    assert excpected == actual
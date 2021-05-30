import pytest
from code_challenges.Data_Structures.ll_zip.ll_zip import *
def test_list_zip_def_length():
    li=Linked_list()
    li2=Linked_list()
    li.insert("1")
    li.insert("2")
    li.insert("5")
    li2.insert("2")
    li2.insert("4")
    actual = print(zipLists(li,li2))
    expected = '{"1"} -> {"2"} -> {"3"} -> {"4"} -> {"5"} -> None'
    assert actual==expected
    
def test_list_zip():
    li=Linked_list()
    li2=Linked_list()
    li.insert("1")
    li.insert("3")
    li.insert("5")
    li2.insert("2")
    li2.insert("4")
    li2.insert("6")    
    expected = '{"1"} -> {"2"} -> {"3"} -> {"4"} -> {"5"} -> {"6"} -> None'
    actual = print(zipLists(li,li2))
    assert actual==expected
from code_challenges.Quik_sort.Quiq import *
import pytest
# def test_insertion_sort():
#     actual = quick_sort([6,2,7,0],0,3)
#     excpected = [0,2,6,7]
#     assert excpected == actual
# def test_insertion_sort2():
#     actual = quick_sort([30,20,15,8,3],0,4)
#     excpected = [3,8,15,20,30]
#     assert excpected == actual
# def test_insertion_sort3():
#     actual = quick_sort([5,12,7,8],0,3)
#     excpected = [5, 7, 8, 12]
#     assert excpected == actual
# def test_insertion_sort4():
#     actual = quick_sort([2,3,5,7,13,11],0,5)
#     excpected = [2,3,5,7,11,13]
#     assert excpected == actual
def test_sort():
    lis = [2,15,33,4,66,8]
    quick_sort(lis,0,5)
    assert lis == [2,4,8,15,33,66]
def test_reverse():
    lis = [50,39,28,17,6]
    quick_sort(lis,0,4)
    assert lis == [6,17,28,39,50]

def test_negative():
    lis = [6,-1,0,-0.5,1,-6]
    quick_sort(lis,0,5)
    assert lis == [-6,-1,-0.5,0,1,6]
def test_uniques():
    lis = [5,12,7,5,5,7]
    quick_sort(lis,0,5)
    assert lis == [5,5,5,7,7,12]
def test_one_item():
    lis = [0]
    quick_sort(lis,0,0)
    assert lis == [0]
def test_tow_item():
    lis = [1,0]
    quick_sort(lis,0,1)
    assert lis == [0,1]

def test_nearly_sorted():
    lis = [2,3,5,7,13,11]
    quick_sort(lis,0,5)
    assert lis == [2,3,5,7,11,13]
def test_alreaedy_sorted():
    lis = [1,2,3,4,5]
    quick_sort(lis,0,4)
    assert lis == [1,2,3,4,5]
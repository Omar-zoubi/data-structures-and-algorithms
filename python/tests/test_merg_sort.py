from code_challenges.merg_sort.merg_sort import *

def test_sort():
    lis = [2,15,33,4,66,8]
    merge_sort(lis)
    assert lis == [2,4,8,15,33,66]
def test_reverse():
    lis = [50,39,28,17,6]
    merge_sort(lis)
    assert lis == [6,17,28,39,50]

def test_negative():
    lis = [6,-1,0,-0.5,1,-6]
    merge_sort(lis)
    assert lis == [-6,-1,-0.5,0,1,6]
def test_uniques():
    lis = [5,12,7,5,5,7]
    merge_sort(lis)
    assert lis == [5,5,5,7,7,12]
def test_one_item():
    lis = [0]
    merge_sort(lis)
    assert lis == [0]
def test_tow_item():
    lis = [1,0]
    merge_sort(lis)
    assert lis == [0,1]

def test_nearly_sorted():
    lis = [2,3,5,7,13,11]
    merge_sort(lis)
    assert lis == [2,3,5,7,11,13]
def test_alreaedy_sorted():
    lis = [1,2,3,4,5]
    merge_sort(lis)
    assert lis == [1,2,3,4,5]
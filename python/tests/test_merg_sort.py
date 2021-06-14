from code_challenges.merg_sort.merg_sort import *
import pytest
def test_merge():
    tst = merge_sort([6,2,7,0])
    actual = tst
    excpected = [0,2,6,7]
    assert excpected == actual
def test_almost_sorted():
    actual = merge_sort([1,2,3,4,6,5])
    excpected = [1,2,3,4,5,6]
    assert excpected == actual
def test_merge_negativ():
    actual = merge_sort([0,12,7,8,-12])
    excpected = [-12,0,7,8,12]
    assert excpected == actual
def test_equl():
    actual = merge_sort([2,3,3,7,7,3])
    excpected = [2,3,3,3,7,7]
    assert excpected == actual
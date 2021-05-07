from array_binary_search.array_binary_search import BinarySearch
list1 = [12]
val1 = 15
list2 = [2,4,5,12]
val2 = 6
list3 = [-2,2,15]
val3 = 2
def test_BinarySearch():
    excepted = -1
    actual = BinarySearch(list1,val1 )
    assert actual == excepted

def test_BinarySearch2():
    excepted = -1
    actual = BinarySearch(list2,val2 )
    assert actual == excepted

def test_BinarySearch3():
    excepted = 1
    actual = BinarySearch(list3,val3)
    assert actual == excepted
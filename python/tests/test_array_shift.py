from code_challenges.ArrayShift.array_shift import adding_in_the_middile 
def test_list():
    actual= adding_in_the_middile([5,6,7,89], 12)
    expected = [5,6,12,7,89]
    assert actual == expected
def test_list():
    actual= adding_in_the_middile([5,6,7,89,15], 12)
    expected = [5,6,7,12,89,15]
    assert actual == expected

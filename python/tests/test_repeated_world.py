from code_challenges.reapetedword.repeat import *
def test_case_one():
    index_one = "It was a queer, sultry summer , the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."
    actual = first_world_repeted(index_one)
    excepted = 'summer'
    assert actual == excepted
def test_case_two():
    index_one = "Once upon a time, there was a brave princess who..."
    actual = first_world_repeted(index_one)
    excepted = 'a'
    assert actual == excepted
def test_case_three():
    index_one = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
    actual = first_world_repeted(index_one)
    excepted = 'it'
    assert actual == excepted
def test_case_four_No_Repeat():
    index_one = "Hello there, my name is Omar and I love programming"
    actual = first_world_repeted(index_one)
    excepted = 'no repeat'
    assert actual == excepted
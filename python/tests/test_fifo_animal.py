import pytest
from code_challenges.Data_Structures.fifo_animal.fifo_animal_shelter import *
def test_animal_shelter():
    obj=AnimalShelter()
    cat1=Cat('selen')
    cat2=Cat('soct')
    dog1=Dog('mix')
    dog2=Dog('rix')
    obj.enqueue(cat1)
    obj.enqueue(cat2)
    obj.enqueue(dog1)
    obj.enqueue(dog2)
    assert obj.deque('cat')=='selen'
    assert obj.deque('hamster')=='just cat and dog'
    assert obj.deque('dog')=='mix'
    assert obj.deque('dog')=='doo'
    assert obj.deque('cat')=='rix'
    assert obj.deque('cat')=='No queue to delete from'
    assert obj.deque('dog')=='No queue to delete from'
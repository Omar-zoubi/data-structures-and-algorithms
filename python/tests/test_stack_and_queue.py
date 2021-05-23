import pytest
from Data_Structures.stacks_and_queues.stacks_and_queues import *

def test_stack_push():

    ST= Stack()
    ST.push(1)
    ST.push(2)
    actual = ST.__str__()
    expected = "2\n1"
    assert actual == expected

def test_stack_push_multibal():
    ST= Stack()
    ST.push(1)
    ST.push(2)
    actual = ST.__str__()
    expected = "2\n1"
    assert actual == expected

def test_stack_pop():
    ST= Stack()
    ST.push(1)
    ST.push(2)
    actual = ST.pop()
    expected = 2
    assert actual == expected


def test_stack_multiple_pop():
    ST= Stack()
    ST.push(1)
    ST.push(2)
    ST.pop()
    ST.pop()
    expected = True
    actual = ST.is_empty()
    assert actual == expected

def test_stack_peek():
    ST= Stack()
    ST.push(1)
    ST.push(2)
    ST.push(3)
    actual = ST.peek()
    expected = 3
    assert actual == expected

def test_is_empty():
    ST= Stack()
    actual = ST.is_empty()
    expected = True
    assert actual == expected


# def test_stack_peek():
#     ST= Stack()
#     ST.peek()
#     actual = ST.peek()
#     expected = "Empty Stack!!"
#     assert actual == expected


def test_peek_pop_empty_Stack():
    
    ST= Stack()
    with pytest.raises(Empetystackexeption) as er:
        ST.peek()
    assert "Empty Stack!!"== str(er.value)
    with pytest.raises(Empetystackexeption) as err:
        ST.pop()
    assert "Empty Stack!!" == str(err.value)


def test_queue_enqueue_one_value():
    queue = Queue()
    queue.enqueue(12)
    expected = "12"
    actual = str(queue)
    assert actual == expected

def test_queue_multiple_enqueue():
    queue = Queue()
    queue.enqueue(4)
    queue.enqueue(3)
    queue.enqueue(6)
    queue.enqueue(1)
    expected = '4\n3\n6\n1'
    actual = str(queue)
    assert actual == expected

def test_queue_dequeue_one_value():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(4)
    queue.enqueue(3)
    queue.enqueue(6)
    queue.enqueue(1)
    queue.deque()
    expected = '4\n3\n6\n1'
    actual = str(queue)
    assert actual == expected



def test_queue_peek():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(4)
    queue.enqueue(3)
    queue.enqueue(6)
    expected = 1
    actual = queue.peek()
    assert actual == expected

def test_queue_multibale_dequeue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(4)
    queue.enqueue(3)
    queue.enqueue(6)
    queue.enqueue(1)
    queue.deque()
    queue.deque()
    queue.deque()
    queue.deque()
    queue.deque()
    expected = True
    actual = queue.is_empty()
    assert actual == expected

def test_queue_multibale_dequeue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(4)
    queue.enqueue(3)
    queue.enqueue(6)
    queue.enqueue(1)
    queue.deque()
    queue.deque()
    queue.deque()
    queue.deque()
    queue.deque()
    expected = True
    actual = queue.is_empty()
    assert actual == expected

def test_queue_is_empty():
    queue = Queue()
    expected = True
    actual = queue.is_empty()
    assert actual == expected

def test_peek_empty_queue():
    
    queue = Queue()
    with pytest.raises(EmptyQueueException) as er:
        queue.peek()
    assert "No Head" == str(er.value)
    with pytest.raises(EmptyQueueException) as err:
        queue.deque()
    assert "No queue to delete from" == str(err.value)
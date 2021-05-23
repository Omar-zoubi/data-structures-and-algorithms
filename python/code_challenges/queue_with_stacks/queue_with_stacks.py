class EmptySatckException(Exception):
    def __init_(self):
        return "The Stack is empty"

class EmptyQueueException(Exception):
    def __init_(self):
        return "The Queue is empty"
class Node():
    def __init__(self,value=None):
        self.value = value
        self.next = None
class PseudoQueue:

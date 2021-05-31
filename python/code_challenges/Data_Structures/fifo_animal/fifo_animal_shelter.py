class Node: 
  def __init__(self, value=None):
    self.value = value
    self.next = None
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        node = Node(value)

        if not self.front:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = self.rear.next
    def deque(self):
      if self.front:
        temp = self.front 
        self.front = self.front.next
        return temp

      raise EmptyQueueException("No queue to delete from")

    def peek(self):
      if self.front:
        return self.front.value
      raise EmptyQueueException("No queue to delete from")
    
    def is_empty(self):
      if self.front:
        return False
      return True

    def __str__(self):
        current = self.front
        items = []
        while current:
            items.append(str(current.value))
            current = current.next
        return "\n".join(items)


class AnimalShelter:
    def __init__(self):
        self.cats=Queue()
        self.dogs=Queue()

    def enqueue(self, data):
        if data.__class__.__name__=='Cat':
            self.cats.enqueue(data.name)
        elif data.__class__.__name__=='Dog':
            self.dogs.enqueue(data.name)
        else:
            return 'just cat and dog'

    def deque(self, pref):
        if pref=='cat':
            return self.cats.deque()
        elif pref=='dog':
            return self.dogs.deque()
        else:
            return 'just cat and dog'

class Cat:
    def __init__(self,name):
        self.name=name

class Dog:
    def __init__(self,name):
        self.name=name
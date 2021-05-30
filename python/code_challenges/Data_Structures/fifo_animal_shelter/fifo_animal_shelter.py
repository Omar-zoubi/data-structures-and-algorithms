class EmptyQueueException(Exception):
  pass
class Empetystackexeption(Exception):
  pass

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
      raise EmptyQueueException("No Head")
    
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
        self.cat=Queue()
        self.dog=Queue()

    def enqueue(self, data):
        if data.__class__.__name__=='Cat':
            self.cats.enqueue(data.name)
        elif data.__class__.__name__=='Dog':
            self.dogs.enqueue(data.name)
        else:
            return 'Only cats and dogs are allowed'

    def dequeue(self, pref):
        if pref=='cat':
            return self.cats.dequeue()
        elif pref=='dog':
            return self.dogs.dequeue()
        else:
            return 'There are only cats and dogs'

class Cat:
    def __init__(self,name):
        self.name=name

class Dog:
    def __init__(self,name):
        self.name=name

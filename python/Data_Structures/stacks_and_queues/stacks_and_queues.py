class EmptyQueueException(Exception):
  pass
class Empetystackexeption(Exception):
  pass

class Node: 
  def __init__(self, value=None):
    self.value = value
    self.next = None

class Stack:
  def __init__(self, node=None):
    self.top = node
  
  def push(self, value):
    if not self.top:
      self.top = Node(value)
    else:
      node = Node(value)
      node.next = self.top
      self.top = node
  
  def pop(self):
    if not self.is_empty():
        temp_node = self.top
        self.top = self.top.next
        temp_node.next = None
        return temp_node.value
    raise Empetystackexeption("Empty Stack!!")

  def is_empty(self):
    if self.top:
        return False
    return True


  def peek(self):
    if not self.is_empty():
        return self.top.value
    raise Empetystackexeption("Empty Stack!!")

    
  def __str__(self):
    current = self.top
    items = []
    while current:
      items.append(str(current.value))
      current = current.next
    return "\n".join(items)

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
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
    try:
        self.top.value
    except AttributeError:
        return "Empty"
    else:
        result = self.top.value
        temp = self.top.next
        self.top = temp
        return result

  def is_empty(self):
    if self.top:
      return False
    return True

  def peek(self):
    if not self.is_empty():
      return self.top.value
    
    raise EmptyStackException("Cannot peek an empty stack")
  
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

    def __str__(self):
        current = self.front
        items = []
        while current:
            items.append(str(current.value))
            current = current.next
        return "\n".join(items)
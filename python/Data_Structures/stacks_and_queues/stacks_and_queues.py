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
class PseudoQueue:
    def __init__(self):
        self.st1 = Stack()
        self.st2 = Stack()
        self.c = 0
    

    def enqueue(self, *value):

        self.c += 1
        for i in value:
            self.st1.push(i)

    def dequeue(self):

        if self.st2.is_empty():
            while self.c > 0:
                self.st2.push(self.st1.pop())
                self.c= self.c -1
            result = self.st2.pop()
            while True:
                self.st1.push(self.st2.pop())
                self.c +=1
                if self.st2.is_empty():
                    return result
        else:
            return "stack is empty!"


    def __str__(self):
        result = ''
        if self.st1.is_empty():
            current = self.st2.top
        else:
            current = self.st1.top
        while current:
            result += f"{{{current.value}}} -> "
            current = current.next
        return result


new_psQ = PseudoQueue()
new_psQ.enqueue(3)
new_psQ.enqueue(6)
new_psQ.enqueue(9)
new_psQ.enqueue(4)
new_psQ.enqueue(7)
new_psQ.enqueue(10)

print(new_psQ.__str__())
def test_dequeue():
    assert new_psQ.dequeue() == 3
    assert new_psQ.dequeue() == 6
    assert new_psQ.dequeue() == 9

if __name__ == "__main__":
    test_dequeue()
    print(new_psQ.__str__())
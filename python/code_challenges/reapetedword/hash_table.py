class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked_list:
    def __init__(self):
        self.head = None
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else :
            last_node =self.head

            while last_node.next:
                last_node = last_node.next
            last_node.next=new_node
    def __str__(self):
        cur_node= self.head
        result =""
        while cur_node:
            result += f"{ {str(cur_node.data)} } -> "
            cur_node=cur_node.next
        result += "NULL"
        return result
    def insert(self,data):
        new_node = Node(data)
        if self.head is None:
          self.head = new_node
          return
        last_node =self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next=new_node

class Hashtable:
    def __init__(self, size):
        self.size = size
        self.map = [None]*size
    def add(self, key, value):
        idx = self.hash(key)
        if not self.map[idx]:
            self.map[idx] = Linked_list()
        self.map[idx].insert([key, value])
    def get(self, key):
        idx = self.hash(key)
        if self.map[idx]:
            current = self.map[idx].head
            while current:
                if current.data[0] == key :
                    return current.data[1]
                current = current.next
        else:
            return None
    def contains(self,key):
        if  self.map[self.hash(key)]:
            return True
        else:
            return False
    def hash(self, key):
        ascii_total = 0
        for ch in key:
            ascii_total += ord(ch)
        hashed = ascii_total * 17
        hashed = hashed % self.size
        return hashed
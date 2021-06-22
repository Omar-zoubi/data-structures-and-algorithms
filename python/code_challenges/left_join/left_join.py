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
        self.list_for_keys= []
    def add(self, key, value):
        idx = self.hash(key)
        if not self.map[idx]:
            self.map[idx] = Linked_list()
        self.map[idx].insert([key, value])
        self.list_for_keys.append(key)
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

def left_joined(firstT, secondT):
    result = []
    for i in firstT.list_for_keys:
        if i in secondT.list_for_keys :
            result.append([i, firstT.get(i),secondT.get(i)])
        else:
            result.append([i,firstT.get(i), 'null'])
    return result
if __name__ == "__main__":
    table1=Hashtable(1024)
    table2=Hashtable(1024)

    table1.add('name','omar')
    table1.add('gender','male')
    table1.add('age','26')
    table1.add('dgree','bacha')
    table2.add('name','kaled')
    table2.add('gender','male')
    table2.add('tall','185cm')
    table2.add('dgree','master')

    print(left_joined(table1, table2))
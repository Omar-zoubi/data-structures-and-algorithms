class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked_list:
    def __init__(self):
        self.head = None


    def insert(self,data):
        new_node = Node(data)
        if self.head is None:
          self.head = new_node
          return
        last_node =self.head

        while last_node.next:
            last_node = last_node.next
        last_node.next=new_node
    
    def printss(self):
        cur_node= self.head
        result =""
        while cur_node:
            # print (f"{"cur_node.data"}" ,"->" )
            result += "{" + cur_node.data + "}" + "->"
            cur_node=cur_node.next
        # print("=>NULL")
        result += " NULL"
        print(result)


    def include(self, index):
        cur_node= self.head
        inc=False
        while cur_node:
            if cur_node.data== index:
                inc = True
            cur_node=cur_node.next
        return inc


linkedlist = Linked_list()
linkedlist.insert("A")
linkedlist.insert("B")
linkedlist.insert("w")
linkedlist.insert("B")
linkedlist.insert("d")
linkedlist.insert("e")
linkedlist.printss()

print(linkedlist.include("Al"))
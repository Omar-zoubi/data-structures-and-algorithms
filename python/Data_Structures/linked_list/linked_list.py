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
    
    def __str__(self):
        cur_node= self.head
        result =""
        while cur_node:
            # print (f"{"cur_node.data"}" ,"->" )
            result += f"{ {str(cur_node.data)} } -> "
            cur_node=cur_node.next
        # print("=>NULL")
        result += "NULL"
        return result


    def include(self, index):
        cur_node= self.head
        inc=False
        while cur_node:
            if cur_node.data== index:
                inc = True
            cur_node=cur_node.next
        return inc


    def append(self, data):
        new_node = Node(data)
        if self.head is None:
          self.head = new_node
        else :
            last_node =self.head

            while last_node.next:
                last_node = last_node.next
            last_node.next=new_node
    
    def insert_after(self, aftervalue, addval):
        new_node = Node(addval)
        current = self.head
        if not self.head:
                return "EMPETY LIST"
        else:
            current = self.head
            while current:
                if current.next:
                    if current.data == aftervalue:
                        nv = current.next
                        current.next = new_node
                        new_node.next = nv
                        return
                    else:
                        current = current.next
                else:
                    current.next = new_node
                    return 
            return "No mathch"
    



    def insert_before(self, nxvalue, addval):

        new_node = Node(addval)
        current = self.head
        if not self.head:
            return "this list is emptey"
        else:
            if self.head.data == nxvalue:
                previous = self.head
                self.head = new_node
                new_node.next = previous
                return 
            current = self.head
            while current.next :
                if current.next.data == nxvalue:
                    previous = current.next
                    current.next = new_node
                    new_node.next = previous
                    return 
                current = current.next

            return "No match"

              
llist = Linked_list()
llist.insert("Omar")
llist.insert("Mohammad")
llist.insert("Al-zoubi")
llist.insert_after("Mohammad", "5")
llist.insert_before("Mohammad", "5")
print(llist)
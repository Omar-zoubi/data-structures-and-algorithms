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
            result += "{" + cur_node.data + "}" + "->"
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

def zipLists(list1,list2):
    result_list=Linked_list()
    ll1=list1.head
    ll2=list2.head
    if ll1 or ll2:
        while ll1 or ll2:
            
            if ll1:
                result_list.append(ll1.data)
                ll1=ll1.next
            if ll2:
                result_list.append(ll2.data)
                ll2=ll2.next
    else:
        return 'no list to merge '
    result_list.__str__()


# if __name__ == "__main__":
#     li=Linked_list()
#     li2=Linked_list()
#     li.insert('o')
#     li.insert('a')
#     li.insert('z')
#     li2.insert('m')
#     li2.insert('r')
#     li2.insert('b')
#     zipLists(li,li2)
#     print(zipLists(li,li2))
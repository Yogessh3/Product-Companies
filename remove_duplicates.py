class Node:
    def __init__(self,data):
      self.data=data
      self.head=None
      self.next=None
class LinkedList:
    def __init__(self):
      self.head=None
    def insert(self,data):
      if(self.head is None):
        new_node=Node(data)
        self.head=new_node
      else:
        new_node=Node(data)
        curr=self.head
        while(curr.next):
          curr=curr.next
        curr.next=new_node
    def remove_duplicates(self):
        curr=self.head
        previous=None
        duplicate_elements=[]
        while(curr):
            if(curr.data in duplicate_elements):
              prev.next=curr.next
            else:
              duplicate_elements.append(curr.data)
              prev=curr
            curr=curr.next
    def print_list(self):
        curr=self.head
        while(curr):
            print(curr.data)
            curr=curr.next
l=LinkedList()
num=[int(x) for x in input().split()]
for i in num:
    l.insert(i)
l.remove_duplicates()
l.print_list()

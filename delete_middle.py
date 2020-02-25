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
    def delete_middle(self):
        curr=self.head
        count=0
        while(curr):
            count+=1
            curr=curr.next
        middle=count//2
        count=1
        curr=self.head
        while(count<middle):
            curr=curr.next
            count+=1
        curr.next=curr.next.next
    def print_list(self):
        curr=self.head
        while(curr):
            print(curr.data,end=" ")
            curr=curr.next
l=LinkedList()
num=[int(x) for x in input().split()]
for i in num:
    l.insert(i)
l.delete_middle()
l.print_list()

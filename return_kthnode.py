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
    def return_kthnode(self,key):
        curr=self.head
        count=0
        while(count<key):
            curr=curr.next
            count+=1
        print(curr.data)
l=LinkedList()
num=[int(x) for x in input().split()]
for i in num:
    l.insert(i)
k=int(input())
value=len(num)-k
l.return_kthnode(value)


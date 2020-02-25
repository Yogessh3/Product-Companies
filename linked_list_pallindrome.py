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
    def check_palindrome(self):
        curr=self.head
        stack=[]
        while(curr):
            stack.append(curr.data)
            curr=curr.next
        curr=self.head
        while(curr):
            val=stack.pop()
            if(curr.data!=val):
                return False
            curr=curr.next
        return True     
    def print_list(self):
        curr=self.head
        while(curr):
            print(curr.data,end=" ")
            curr=curr.next
l=LinkedList()
string=input().strip()
for i in string:
    l.insert(i)
if(l.check_palindrome()):
    print("Yes")
    l.print_list()
else:
    print("No")

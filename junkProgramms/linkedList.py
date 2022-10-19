import time 
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def __eq__(self,node):
        if isinstance(node,Node):
            return self.data==node.data
    def __repr__(self):
        return f'<Node {self.data}>'

class LinkedList:
    def __init__(self,head=None):
        self.head=head
    def printList(self):
        temp=self.head
        while temp is not None:
            print(temp.data)
            temp=temp.next
    def appendNode(self,node):
        temp=self.head
        while temp is not None:
            if temp.next is None:
                temp.next=node
                break
            temp=temp.next
    def addNode(self,prev_node,node):
        temp=self.head
        while temp is not None:
            if temp==prev_node:
                print('condition checked adding element\n\n')
                node.next=temp.next
                temp.next=node
                break
            temp=temp.next
    def deleteNode(self,node):
        temp=self.head
        while temp is not None:
            print(temp)
            print(temp.next)
            if temp.next==node:
                temp.next=temp.next.next
                break
            temp=temp.next
    def get_position(self, position):
        i=0
        current=self.head
        while current:
            if i==position:
                return current
            else:
                current=current.next
                i=i+1
        return current
    def insert(self, new_element, position):
        i=0
        current=self.head
        while current:
            print('inside the while loop')
            if position==i+1:
                print(f'adding the element in posiiton {position}')
                new_element.next=current.next
                current.next=new_element
                i=i+1
            else:
                print('incrementing the i')
                i=i+1
            current=current.next


    def delete(self, value):
        if self.head.data==value:
            self.head=self.head.next
        else:
            current=self.head
            while current:
                if current.next is not None:
                    if current.next.data==value:
                        current.next=current.next.next
                current=current.next
    def insert_first(self,new_element):
        if self.head:
            new_element.next=self.head
            self.head=new_element
        else:
            self.head=new_element
    def delete_first(self):
        if self.head:
            deleted=self.head
            self.head=self.head.next
            return deleted
        else:
            return self.head
class Stack(object):
    def __init__(self,top):
        self.ll=LinkedList(top)
    def push(self,node):
        self.ll.appendNode(node)
    def printStack(self):
        self.ll.printList()
    def pop(self):
        current=self.ll.head
        while current: 
            if current.next.next is None:
                last_node=current.next
                current.next=None
                return last_node
            current=current.next



head=Node(1)
second=Node(2)
tail=Node(3)
linkedList=LinkedList()
linkedList.head=head
head.next=second
second.next=tail
linkedList.appendNode(Node(4))
linkedList.insert_first(Node(0))
print(linkedList.delete_first())
linkedList.printList()
'''
stack=Stack(Node(0))
stack.push(Node(1))
stack.push(Node(2))
stack.printStack()
print(f"the last node value is {stack.pop()}\n\n")
print(f"ths last node vlaue is {stack.pop()}\n\n")
stack.printStack()
'''

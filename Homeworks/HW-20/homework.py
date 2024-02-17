# 1. შექმენით პითონის კლასი Node რომელსაც ექნება ორი ატრიბუტი (value, next), შემდეგ შექმენით LinkedList  კლასი 
#    რომლის კონსტრუქტორი მიიღებს Value პარამეტრს.
# 2. LinkedList კლასში შექმენით append მეთოდი, რომლის საშუალებითაც ჩაამტებთ სიის ბოლოში ახალ ნოუდს (Node  კლასის ახალ ობიექტს)
# 3. LinkedList კლასში შექმენით remove მეთოდი, რომლის საშუალებითაც წაშლით სიიდან მის ბოლო ელემენტს(Тail-ს)
# 4. პითონის Stack.py ფაილში შექმენილია Stack კლასი, დაწერეთ კლასის ფუნქციები (push და pop)


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value=None):
        if value is not None:
            self.head = Node(value)
        else:
            self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    def remove(self):
        if not self.head:
            raise Exception("List is empty")
        if not self.head.next:
            self.head = None
            return
        current_node = self.head
        while current_node.next.next:
            current_node = current_node.next
        current_node.next = None

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.value, end=" -> ")
            current_node = current_node.next
        print("None")


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0


#----- Testing LinkedList ------#
linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.print_list() 
linked_list.remove()
linked_list.print_list()  

#----- Testing Stack------#
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop()) 
print(stack.pop()) 
print(stack.pop()) 
# print(stack.pop())
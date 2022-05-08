# '''Class Template for a singly linked list Head -> Tail convention
# Exercise Part starts at line 40'''

# class for holding the data, defaults to empty node if no data is given


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None  # pointer to the next node

# Class for managing the list and nodes


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        node = Node(data)

        if self.head == None:  # if the node is empty, the new node is the head
            self.head = node
        # if not empty iterate through items and append new node at the end (tail)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
        self.size += 1  # always update the size to prevent costly iterations to get the size

    # defining iteration function to make iterating over nodes in the list possible
    def __iter__(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val

    def get_size(self):
        return self.size

    # '''
    # Exercise Part 1,2 and 3:
    # Implement the given methods below according to the requirements in the exercise sheet.
    # return the correct data types and values
    # '''

    def clear(self):
        # while self.head:
        #     temp = self.head
        #     self.head = self.head.next
        #     temp = None
        #     self.size -= 1
        self.head = None
        self.size = 0

    def get_data(self, data):
        current = self.head
        while current:
            if current.data == data:
                return data
            current = current.next
        return False

    def delete(self, data):
        current = self.head
        if current.data.data == data:
            self.head = current.next
            current = None
            self.size -= 1
            return
        while current:
            if current.data.data == data:
                break
            temp = current
            current = current.next
        temp.next = current.next
        current = None
        self.size -= 1

    # Print the linked list

#     def print(self):
#         temp = self.head
#         while (temp):
#             print(str(temp.data.data) + " ", end="")
#             temp = temp.next


# node1 = Node(1)
# node2 = Node(2)
# node3 = Node(3)
# node4 = Node(4)
# node5 = Node(5)

# MyList = SinglyLinkedList()

# MyList.append(node1)
# MyList.append(node2)
# MyList.append(node3)
# MyList.append(node4)
# MyList.print()
# print(" ")
# print(MyList.size)
# print(MyList.get_data(4))
# MyList.clear()
# print(MyList.size)
# MyList.append(node1)
# MyList.append(node2)
# MyList.append(node3)
# MyList.append(node4)
# MyList.print()
# MyList.delete(1)
# print(" ")
# MyList.print()
# print(" ")
# print(MyList.size)

# '''Exercise Part 4: Copy the code from the singly linked list implementation and rewrite it
# to implement a doubly linked list according to the exercise sheet. Dont forget to change the names of the classes
# in the code to reflect the new class name (NodeDLL instead of Node).
# '''


class NodeDLL:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        node = Node(data)

        if self.head == None:  # if the node is empty, the new node is the head
            self.head = node
        # if not empty iterate through items and append new node at the end (tail)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
            node.prev = current
        self.size += 1  # always update the size to prevent costly iterations to get the size

    # defining iteration function to make iterating over nodes in the list possible
    def __iter__(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val

    def get_size(self):
        return self.size

    def clear(self):
        while self.head:
            temp = self.head
            self.head = self.head.next
            temp = None
            self.size -= 1

    def get_data(self, data):
        current = self.head
        while current:
            if current.data.data == data:
                return data
            current = current.next
        return False

    def delete(self, data):
        current = self.head
        if current.data.data == data:
            self.head = current.next
            current.prev = None
            self.size -= 1
            return
        while current:
            if current.data.data == data:
                break
            temp = current
            current = current.next
        temp.next = current.next
        # HÜFE

        current = None
        self.size -= 1
    # '''Exercise Part 5 and 6:
    # Complete the classes below to implement a stack and queue data structure. You are free to use built-in
    # methods but you have to complete all methods below. Always return the correct data type according
    # to the exercise sheet'''


class MyStack:
    def __init__(self):
        self.items = []

    def push(self, element):
        self.items.append(element)

    def pop(self):
        if self.items:
            return self.items.pop()

    def top(self):
        if self.items:
            return self.items[-1]

    def size(self):
        return len(self.items)


class MyQueue:
    def __init__(self):
        self.items = []

    def push(self, element):
        self.items.append(element)

    def pop(self):
        if self.items:
            return self.items.pop(0)

    def show_left(self):
        if self.items:
            return self.items[-1]

    def show_right(self):
        if self.items:
            return self.items[0]

    def size(self):
        return len(self.items)

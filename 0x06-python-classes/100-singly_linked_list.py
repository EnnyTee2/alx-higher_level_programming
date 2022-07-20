#!/usr/bin/python3

"""a class Node that defines a node of a singly linked list
with private instance attributes and properties which
are accessed and changed by getters and setters respectively"""


class Node:
    """"
    Node (class): defines a node of a singly linked
    list raise error if type is not int or
    size is less than zero.
    Attributes:
        data (int): specifies the data
        next_node(): specifies the next node in the SLL
    """


    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return [node.__data for node in self]

    @data.setter
    def data(self, value):
        if type(data) is int:
            self.__data = value
        else:
            raise TypeError('data must be an integer')

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if (value is None) or (isinstance(value, self) is True):
            self.__next_node = value
        else:
            raise TypeError('next_node must be a Node object')

    def __str__(self):
        return str(self.__data)


class SinglyLinkedList:
    """"
    SinglyLinkedList (class): defines a singly linked
    list with a private instance attribute: head
    Attributes:
        head (Node): specifies the head of the list
        sorted_insert (): method that inserts new nodes into
        the proper sorted position in the SLL (ascending order)
    """
    
    def __init__(self, data=None):
        self.__head = None
        self.__tail = None
        if data != None:
            self.sorted_insert(data)

    def sorted_insert(self, value):
        if self.__head == None:
            self.__head = self.__tail = Node(value) 
        else:
            self.__tail.next_node = Node(value)
            self.__tail = self.tail.next_node
        return self.__tail

    def list_gen(self):
        it = [node for node in self]
        return it

    def recurs(self, lis):
        if len(lis) != 0:
            self.recurs(lis)
        return lis.pop()

    def __str__(self):
        for node in self:
            print(node)

    def __len__(self):
        count = 0
        node = self.__head
        while node:
            count += 1
            node = node.next_node
        return count

    def __iter__(self):
        current = self.__head
        while current:
            yield current
            current = current.next

#!python

from __future__ import print_function


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data"""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node"""
        return 'Node({})'.format(repr(self.data))


class LinkedList(object):

    def __init__(self, iterable=None):
        """Initialize this linked list; append the given items, if any"""
        self.head = None
        self.tail = None
        if iterable:
            for item in iterable:
                self.append(item)

    def __repr__(self):
        """Return a string representation of this linked list"""
        return 'LinkedList({})'.format(repr(self.items()))

    def items(self):
        """Return a list of all items in this linked list"""
        result = []
        current = self.head
        while current is not None:
            result.append(current.data)
            # result.append(current)
            current = current.next
        return result

    def is_empty(self):
        """Return True if this linked list is empty, or False"""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes"""
        node = self.head
        count = 0
        while node is not None:
            count += 1
            node = node.next

    def append(self, item):
        """Insert the given item at the tail of this linked list"""
        item_node = Node(item)
        if self.tail:
            self.tail.next = item_node
            self.tail = item_node
        else:
            self.tail = item_node
            self.head = item_node

    def prepend(self, item):
        """Insert the given item at the head of this linked list"""
        item_node = Node(item)
        if self.head:
            item_node.next = self.head
            self.head = item_node
        else:
            self.head = item_node
            self.tail = item_node

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError"""
        node = self.head
        new_first = None
        while node is not None:
            print(node.data, item)
            if node.next.data == item:
                new_first = node
            elif node.data == item:
                if node == self.head:
                    node.next = self.head
                else:
                    new_first.next = node.next
                    node.next = None
                break
            node = node.next

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality"""
        node = self.head
        while node is not None:
            print(node.data, quality)
            if node.data == quality:
                return node.data
            node = node.next


def test_linked_list():
    ll = LinkedList()
    print(ll)
    ll.append('A')
    print(ll)
    ll.append('B')
    print(ll)
    ll.append('C')
    print(ll)
    print('head: ' + str(ll.head))
    print('tail: ' + str(ll.tail))
    print(ll.length())

    ll.delete('A')
    print(ll)
    ll.delete('C')
    print(ll)
    ll.delete('B')
    print(ll)
    print('head: ' + str(ll.head))
    print('tail: ' + str(ll.tail))
    print(ll.length())


if __name__ == '__main__':
    test_linked_list()

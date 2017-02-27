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

    def __str__(self):
        """Return a formatted string representation of this linked list"""
        items = ['({})'.format(repr(item)) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list"""
        return 'LinkedList({})'.format(repr(self.items()))

    def items(self):
        """Return a list of all items in this linked list"""
        result = []
        current = self.head
        while current is not None:
            result.append(current.data)
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
        return count

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
        last_node = None
        print("node is", node)
        while node is not None:
            print(node.data, item)
            if node.data == item:
                if node != self.head and node != self.tail:
                    print("Node not head or tail.")
                    last_node.next = node.next
                    node.next = None
                if node == self.head:
                    print("Node is head.")
                    self.head = node.next
                if node == self.tail:
                    print("Node is tail.")
                    self.tail = last_node
                    if last_node:
                        last_node.next = None
                return
            last_node = node
            node = node.next
        print("Value not found. Raise ValueError.")
        raise ValueError('Could not find', item, 'in list.')

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality"""
        node = self.head
        while node is not None:
            # print(node.data, quality)
            # print("quality(node.data) =", quality(node.data))
            if quality(node.data):
                return node
            node = node.next
        return Node(None)


def test_linked_list():
    ll = LinkedList()
    print(ll)

    print('Appending items:')
    ll.append('A')
    print(ll)
    ll.append('B')
    print(ll)
    ll.append('C')
    print(ll)
    print('head: ' + str(ll.head))
    print('tail: ' + str(ll.tail))
    print('length: ' + str(ll.length()))

    # Enable this after implementing delete:
    print('Deleting items:')
    ll.delete('B')
    print(ll)
    ll.delete('C')
    print(ll)
    ll.delete('A')
    print(ll)
    print('head: ' + str(ll.head))
    print('tail: ' + str(ll.tail))
    print('length: ' + str(ll.length()))


if __name__ == '__main__':
    test_linked_list()

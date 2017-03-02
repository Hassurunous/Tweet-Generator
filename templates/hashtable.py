#!python

from linkedlist import LinkedList
import random


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size"""
        self.buckets = [LinkedList() for i in range(init_size)]  # n iterations for each element in init_size

    def __str__(self):
        """Return a formatted string representation of this hash table"""
        items = ['{}: {}'.format(repr(k), repr(v)) for k, v in self.items()]  # n iterations for each item in self.items()
        return '{' + ', '.join(items) + '}'  # n time to join each item in array

    def __repr__(self):
        """Return a string representation of this hash table"""
        return 'HashTable({})'.format(repr(self.items()))

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored"""
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table"""
        # Collect all keys in each of the buckets
        # O(n)
        all_keys = []  # Constant time to assign variable
        for bucket in self.buckets:  # O(b) iterations always
            for key, value in bucket.items():  # O(l) = n/b iterations always
                all_keys.append(key)  # Constant time to append
        return all_keys  # Constant time to return array

    def values(self):
        """Return a list of all values in this hash table"""
        all_values = []  # Constant time to assign variable
        # nlogn or nk
        for bucket in self.buckets:  # n iterations
            for key, value in bucket.items():  # n iterations
                all_values.append(value)  # Constant time to append
        return all_values  # Constant time to return array

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table"""
        # Collect all pairs of key-value entries in each of the buckets
        all_items = []  # Constant time to assign variable
        for bucket in self.buckets:  # n iterations
            all_items.extend(bucket.items())  # Constant time to extend
        return all_items  # Constant time to return array

    def length(self):
        """Return the length of this hash table by traversing its buckets"""
        length = 0
        for bucket in self.buckets:
            for key, value in bucket.items():
                length += 1
        return length

    def contains(self, key):
        """Return True if this hash table contains the given key, or False"""
        # for bucket in self.buckets:
        #     for key, value in bucket.items():
        #         print("Key, Key_In:")
        #         print(key, key_in)
        #         if key == key_in:
        #             return True
        node = self.buckets[self._bucket_index(key)].find(lambda item: item[0] == key)  # Runs the
        if node.data:
                return True
        return False

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError"""
        # for bucket in self.buckets:
        #     for key, value in bucket.items():
        #         # print("Key, Value", key, value)
        #         if key == key_in:
        #             return value
        node = self.buckets[self._bucket_index(key)].find(lambda item: item[0] == key)  # n
        if node.data:
            return node.data[1]
        raise KeyError

    def set(self, key, value):
        """Insert or update the given key with its associated value"""
        node = self.buckets[self._bucket_index(key)].find(lambda item: item[0] == key)
        if node.data:
            node.data = (key, value)
        else:
            self.buckets[self._bucket_index(key)].append((key, value))

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError"""
        # print(self)
        # for bucket in self.buckets:
        #     print("Bucket:", bucket)
        #     for key, value in bucket.items():
        #         # print("Key, Value", key, value)
        #         if key == key_in:
        #             print("Found key.")
        #             bucket = []
        #             print(bucket)
        #             return
        # print("Testing delete:", self.buckets[self._bucket_index(key)].find(lambda item: item[0] == key))
        node = self.buckets[self._bucket_index(key)].find(lambda item: item[0] == key)
        if node.data:
            return self.buckets[self._bucket_index(key)].delete(node.data)
        raise KeyError


def test_hash_table():
    ht = HashTable()
    print(ht)

    print('Setting entries:')
    ht.set('I', 1)
    print(ht)
    ht.set('V', 5)
    print(ht)
    ht.set('X', 10)
    print(ht)
    print('contains(X): ' + str(ht.contains('X')))
    print('get(I): ' + str(ht.get('I')))
    print('get(V): ' + str(ht.get('V')))
    print('get(X): ' + str(ht.get('X')))
    print('length: ' + str(ht.length()))

    # Enable this after implementing delete:
    # print('Deleting entries:')
    # ht.delete('I')
    # print(ht)
    # ht.delete('V')
    # print(ht)
    # ht.delete('X')
    # print(ht)
    # print('contains(X): ' + str(ht.contains('X')))
    # print('length: ' + str(ht.length()))


if __name__ == '__main__':
    test_hash_table()

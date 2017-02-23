#!python

from linkedlist import LinkedList
import random


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size"""
        self.buckets = [LinkedList() for i in range(init_size)]

    def __str__(self):
        """Return a formatted string representation of this hash table"""
        items = ['{}: {}'.format(repr(k), repr(v)) for k, v in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table"""
        return 'HashTable({})'.format(repr(self.items()))

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored"""
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table"""
        # Collect all keys in each of the buckets
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table"""
        all_values = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_values.append(value)
        return all_values

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table"""
        # Collect all pairs of key-value entries in each of the buckets
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the length of this hash table by traversing its buckets"""
        length = 0
        for bucket in self.buckets:
            for key, value in bucket.items():
                length += 1
        return length

    def contains(self, key_in):
        """Return True if this hash table contains the given key, or False"""
        for bucket in self.buckets:
            for key, value in bucket.items():
                print("Key, Key_In:")
                print(key, key_in)
                if key == key_in:
                    return True
        return False

    def get(self, key_in):
        """Return the value associated with the given key, or raise KeyError"""
        for bucket in self.buckets:
            for key, value in bucket.items():
                # print("Key, Value", key, value)
                if key == key_in:
                    return value
        raise KeyError

    def set(self, key_in, value_in):
        """Insert or update the given key with its associated value"""
        self.buckets[self._bucket_index(key_in)].append((key_in, value_in))

    def delete(self, key_in):
        """Delete the given key from this hash table, or raise KeyError"""
        print(self)
        for bucket in self.buckets:
            print("Bucket:", bucket)
            for key, value in bucket.items():
                # print("Key, Value", key, value)
                if key == key_in:
                    print("Found key.")
                    bucket = []
                    print(bucket)
                    return
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

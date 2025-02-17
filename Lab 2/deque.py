# remember that Item is a generic variable, you declare it
# when making an object
#
# For example:
# d = Deque[int]()
#
from typing import TypeVar

Item = TypeVar('Item')

class Node:
    def __init__(self, item: Item):
        self.item = item
        self.next = None
        self.prev = None


class Deque[Item]:
    # construct an empty deque
    def __init__(self):
        self.first: Node = None
        self.last: Node = None
        self._length = 0

    # is the deque empty?
    def is_empty(self) -> bool:
        return self._length == 0

    # return the number of items on the deque
    def size(self) -> int:
        return self._length

    # add the item to the front
    def add_first(self, item: Item) -> None:
        if item is None:
            raise ValueError("Item should not be none!")
        new_node = Node(item)
        if self.is_empty():
            self.first = new_node
            self.last = new_node
        else:
            new_node.next = self.first
            self.first.prev = new_node
            self.first = new_node
        self._length += 1

    # add the item to the back
    def add_last(self, item: Item) -> None:
        if item is None:
            raise ValueError("Item should not be none!")
        new_node = Node(item)
        if self.is_empty():
            self.first = new_node
            self.last = new_node
        else:
            new_node.prev = self.last
            self.last.next = new_node
            self.last = new_node
        self._length += 1

    # remove and return the item from the front
    def remove_first(self) -> Item:
        if self.is_empty():
            raise IndexError("Deque is empty!")
        current_first = self.first
        if self._length == 1:
            self.first = None
            self.last = None
        else:
            self.first = current_first.next
            self.first.prev = None
        self._length -= 1
        return current_first.item

    # remove and return the item from the back
    def remove_last(self) -> Item:
        if self.is_empty():
            raise IndexError("Deque is empty!")
        current_last = self.last
        if self._length == 1:
            self.first = None
            self.last = None
        else: 
            self.last = current_last.prev
            self.last.next = None
        self._length -= 1
        return current_last.item

    def __iter__(self):
        return self

    # return the current item and tick the current item to the next
    # otherwise, raise StopIteration
    def __next__(self) -> Item:
        if self._length == 0:
            raise StopIteration
        else:
            current_item = self.first
            next_item = current_item.next
            self.first = next_item
            self.length -= 1
            return current_item

    # unit testing (required)
    @staticmethod
    def main():
        d = Deque()
        print(d.is_empty()) # should be true since there are no items in the deque yet

        d.add_first("first item")

        # the first and last should be the first item since it is the first and last item in the deque
        print(d.first.item) # first item
        print(d.last.item) # first item

        d.add_last("last item")

        # the first should be the "first item" and the last should be the "last item"
        print(d.first.item) # first item
        print(d.last.item) # last item

        print(d.is_empty()) # should be false since there are now 2 items in the deque
        print(d.size()) # the size should now be two

        print(d.remove_first())
        # the first and last should be the "last item" since we removed the first item the only item left is the "last item"
        print(d.first.item) # last item
        print(d.last.item) # last item

         # the size shoul now be one leeser than the previos size, 
        print(d.size()) # should be 1
        print(d.remove_last())

        print(d.size())# should now be empty
        print(d.is_empty())

if __name__ == "__main__":
    Deque.main()

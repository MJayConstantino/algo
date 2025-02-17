# remember that Item is a generic variable, you declare it
# when making an object
#
# For example:
# d = Deque[int]()
#

class Node:
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None


class Deque[Item]:
    # construct an empty deque
    def __init__(self):
        self.first: Node = None
        self.last: Node = None
        self.size = 0

    # is the deque empty?
    def is_empty(self) -> bool:
        return self.size == 0

    # return the number of items on the deque
    def size(self) -> int:
        return self.size

    # add the item to the front
    def add_first(self, item: Item) -> None:
        if item is None:
            raise ValueError("Item should not be none!")
        new_node = Node(item)
        if self.is_empty:
            self.first = new_node
            self.last = new_node
        else:
            new_node.next = self.first
            self.first.prev = new_node
            self.first = new_node
        self.size += 1

    # add the item to the back
    def add_last(self, item: Item) -> None:
        if item is None:
            raise ValueError("Item should not be none!")
        new_node = Node(item)
        if self.is_empty:
            self.first = new_node
            self.last = new_node
        else:
            new_node.prev = self.last
            self.last.next = new_node
            self.last = new_node
        self.size += 1

    # remove and return the item from the front
    def remove_first(self) -> Item:
        if self.is_empty:
            raise IndexError("Deque is empty!")
        current_first = self.first
        self.first = current_first.next
        self.size -= 1
        return current_first.item

    # remove and return the item from the back
    def remove_last(self) -> Item:
        if self.is_empty:
            raise IndexError("Deque is empty!")
        current_last = self.last
        self.last = current_last.prev
        self.size -= 1
        return current_last.item

    def __iter__(self):
        pass

    # return the current item and tick the current item to the next
    # otherwise, raise StopIteration
    def __next__(self) -> Item:
        pass

    # unit testing (required)
    @staticmethod
    def main():
        d = Deque()
        d.add_first(1)
        d.add_last(2)
        print(d.is_empty())
        print(d.size)

if __name__ == "__main__":
    Deque.main()

# remember that Item is a generic variable, you declare it
# when making an object
#
# For example:
# d = Deque[int]()
#
class Deque[Item]:
    # construct an empty deque
    def __init__(self):
        pass

    # is the deque empty?
    def is_empty(self) -> bool:
        pass

    # return the number of items on the deque
    def size(self) -> int:
        pass

    # add the item to the front
    def add_first(self, item: Item) -> None:
        if item is None:
            raise ValueError("Item should not be none!")

    # add the item to the back
    def add_last(self, item: Item) -> None:
        if item is None:
            raise ValueError("Item should not be none!")

    # remove and return the item from the front
    def remove_first(self) -> Item:
        if self.is_empty:
            raise IndexError("Deque is empty!")

    # remove and return the item from the back
    def remove_last(self) -> Item:
        if self.is_empty:
            raise IndexError("Deque is empty!")

    def __iter__(self):
        pass

    # return the current item and tick the current item to the next
    # otherwise, raise StopIteration
    def __next__(self) -> Item:
        pass

    # unit testing (required)
    @staticmethod
    def main():
        pass


if __name__ == "__main__":
    Deque.main()

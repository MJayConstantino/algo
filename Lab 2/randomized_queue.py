import random

class RandomizedQueue[Item]:
    # construct an empty randomized queue
    def __init__(self):
        self.items: list[Item] = []
        self._iterator_list: list[Item] = []
        self._iterator_index = 0

    # is the randomized queue empty?
    def is_empty(self) -> bool:
        return self.size() == 0

    # return the number of items on the randomized queue
    def size(self) -> int:
        return len(self.items)

    # add the item
    def enqueue(self, item: Item) -> None:
        if item is None:
            raise ValueError("Item cannot be None!")
        self.items.append(item)  # Append item at the end

    # remove and return a random item
    def dequeue(self) -> Item:
        if self.is_empty():
            raise IndexError("Queue is empty")

        random_index = random.randrange(len(self.items))
        return self.items.pop(random_index)  # Remove and return the random item

    # return a random item (but do not remove it)
    def sample(self) -> Item:
        if self.is_empty():
            raise IndexError("Queue is empty")

        return random.choice(self.items)  # Return a random item without removing it

    # for looping this object will loop over the items in a random order
    def __iter__(self):
        self._iterator_list = self.items[:]  # Make a copy
        random.shuffle(self._iterator_list)  # Shuffle the copy
        self._iterator_index = 0  # Reset iterator index
        return self

    # return the current item and move to the next one
    def __next__(self) -> Item:
        if self._iterator_index >= len(self._iterator_list):
            raise StopIteration  # End of iteration

        item = self._iterator_list[self._iterator_index]
        self._iterator_index += 1
        return item

    # unit testing (required)
    @staticmethod
    def main():
        rq = RandomizedQueue[str]()

        print("Is empty?: ", rq.is_empty())  # True

        # Add items to the queue
        rq.enqueue("hello")
        rq.enqueue("world")
        rq.enqueue("goodbye")

        print("Enqueued hello, world, and goodbye")

        print("Size after enqueues:", rq.size())  # 3
        print("Is empty after enqueues?:", rq.is_empty())  # False

        print("Items in random order:", [item for item in rq])  # Random order of items

        print("Sample:", rq.sample())  # Random item
        print("Dequeued item:", rq.dequeue())  # Randomly removed item

        print("Size after dequeue:", rq.size())  # Size reduced by 1
        print("Remaining items:", [item for item in rq])  # Random order of remaining items


if __name__ == "__main__":
    RandomizedQueue.main()

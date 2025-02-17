from typing import TypeVar
import random

Item = TypeVar('Item')

class Node:
    def __init__(self, item: Item):
        self.item = item
        self.next = None
        self.prev = None

class RandomizedQueue[Item]:
    # construct an empty randomized queue
    def __init__(self):
        self.front = Node(None)
        self.back = Node(None)
        self.length = 0

    # is the randomized queue empty?
    def is_empty(self) -> bool:
        return self.length == 0

    # return the number of items on the randomized queue
    def size(self) -> int:
        return self.length

    # add the item
    def enqueue(self, item: Item) -> None:
        if item is None:
            raise ValueError("Item is empty!")

        new_node = Node(item)

        if self.is_empty():
            self.front = new_node
            self.back = new_node
        else:
            current_back = self.back
            current_back.next = new_node
            new_node.prev = current_back
            self.back = new_node  

        self.length += 1

    # remove and return a random item
    def dequeue(self) -> Item:
        if self.is_empty():
            raise IndexError("Queue is empty")

        random_index = random.randint(0, self.length - 1)
        current_node = self.front

        for _ in range(random_index):
            current_node = current_node.next

        item = current_node.item

        # Disconnect the node
        if current_node.prev:
            current_node.prev.next = current_node.next
        if current_node.next:
            current_node.next.prev = current_node.prev

        if current_node == self.front:
            self.front = current_node.next

        if current_node == self.back:
            self.back = current_node.prev

        self.length -= 1

        return item


    # return a random item (but do not remove it)
    def sample(self) -> Item:
        if self.is_empty():
            raise IndexError("Queue is empty")

        random_index = random.randint(0, self.length - 1)
        current_node = self.front

        for _ in range(random_index):
            current_node = current_node.next

        return current_node.item


    # for looping this object will loop over the items in a random order
    def __iter__(self):
        return self

    # return the current item and tick the current item to the next
    # otherwise, raise StopIteration
    def __next__(self) -> Item:
        if self.length == 0:
            raise StopIteration
        else:
            current_item = self.front
            next_item = current_item.next
            self.front = next_item
            self.length -= 1
            return current_item

    # unit testing (required)
    @staticmethod
    def main():
        rq = RandomizedQueue[str]()
        
        print(rq.is_empty())

        print(rq.enqueue("hello"))
        print(rq.enqueue("world"))
        print(rq.enqueue("goodbye"))
        print(rq.size())
        print(rq.is_empty())

        print(rq.sample())
        print(rq.dequeue())

        print(rq.size())

        items_in_queue = [item.item for item in rq]
        print(items_in_queue)

if __name__ == "__main__":
    RandomizedQueue.main()
from typing import TypeVar, Optional
import random

Item = TypeVar('Item')

class Node:
    def __init__(self, item: Item):
        self.item: Item = item
        self.next: Optional[Node] = None
        self.prev: Optional[Node] = None

class RandomizedQueue[Item]:
    # construct an empty randomized queue
    def __init__(self):
        self.front: Optional[Node] = None
        self.back: Optional[Node] = None
        self._length = 0

    # is the randomized queue empty?
    def is_empty(self) -> bool:
        return self._length == 0

    # return the number of items on the randomized queue
    def size(self) -> int:
        return self._length

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

        self._length += 1

    # remove and return a random item
    def dequeue(self) -> Item:
        if self.is_empty():
            raise IndexError("Queue is empty")

        random_index = random.randint(0, self._length - 1)
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

        self._length -= 1

        return item


    # return a random item (but do not remove it)
    def sample(self) -> Item:
        if self.is_empty():
            raise IndexError("Queue is empty")

        random_index = random.randint(0, self._length - 1)
        current_node = self.front

        for _ in range(random_index):
            current_node = current_node.next

        return current_node.item


    # for looping this object will loop over the items in a random order
    def __iter__(self):
        nodes = []
        current_node = self.front
        while current_node:
            nodes.append(current_node.item)
            current_node = current_node.next

        random.shuffle(nodes)  # Shuffle the collected items

        for item in nodes:
            yield item  # Return items one by one


    # return the current item and tick the current item to the next
    # otherwise, raise StopIteration
    def __next__(self) -> Item:
        if self._length == 0:
            raise StopIteration
        else:
            current_item = self.front
            next_item = current_item.next
            self.front = next_item
            self._length -= 1
            return current_item

    # unit testing (required)
    @staticmethod
    def main():
        rq = RandomizedQueue[str]()
        
        print(rq.is_empty())

        # add items to the queue
        rq.enqueue("hello")
        rq.enqueue("world")
        rq.enqueue("goodbye")

        print(rq.size())
        print(rq.is_empty())

        print([item for item in rq]) # print items in queue

        print(rq.sample())
        print(rq.dequeue()) # remove a random item from the queue

        print(rq.size())

        print([item for item in rq]) # print items in queue

       

if __name__ == "__main__":
    RandomizedQueue.main()
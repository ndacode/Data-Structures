import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

### Queues
#  * Should have the methods: `enqueue`, `dequeue`, and `len`.
  
class Queue:
    def __init__(self):
        # Why is our DLL a good choice to store our elements?
        self.size = 0
        self.storage = DoublyLinkedList()

#  * `enqueue` should add an item to the back of the queue.
    def enqueue(self, value):
        self.size
        return self.storage.add_to_tail(value)

#  * `dequeue` should remove and return an item from the front of the queue.
    def dequeue(self):
        return self.storage.remove_from_head()
        
# * `len` returns the number of items in the queue.
    def len(self):
        return self.storage.length


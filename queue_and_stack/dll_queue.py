from doubly_linked_list import DoublyLinkedList
from doubly_linked_list import ListNode
import sys
sys.path.append('../doubly_linked_list')


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.size += 1
        self.storage.add_to_tail(value)

    def dequeue(self):
        if not self.storage:
            return None
        self.size -= 1
        return self.storage.remove_from_head()

    def len(self):
        return len(self.storage)

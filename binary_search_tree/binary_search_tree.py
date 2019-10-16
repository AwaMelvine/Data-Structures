# from dll_stack import Stack
# from dll_queue import Queue
import sys
sys.path.append('../queue_and_stack')


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self, value):
        self.bst = Node(value)

    # Insert the given value into the tree

    def insert(self, value):
        # LESS THAN
        if value < self.bst.value:
            if self.bst.left is None:
                print("insert left")
                self.bst.left = Node(value)
                return
            else:
                print(f"move to left")
                self.bst.value = self.bst.left.value
                self.insert(value)

        # GREATER THAN
        elif value > self.bst.value:
            if self.bst.right is None:
                print("insert right")
                self.bst.right = Node(value)
                return
            else:
                print(f"{self.bst.value} move right")
                self.bst.value = self.bst.right.value
                self.insert(value)

        # Return True if the tree contains the value
        # False if it does not

    def contains(self, target):
        # if target == self.value:
        #     return True
        # if target < self.value:
        #     self.value = self.left
        #     self.contains(target)
        # if target > self.value:
        #     self.value = self.right
        #     self.contains(target)
        # return False
        pass

    # Return the maximum value found in the tree

    def get_max(self):
        if self.right is None:
            return self.value
        if self.right is not None:
            self.value = self.right
            self.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        pass

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def add(self, previous_node, node):

        if previous_node is None:
            self.head = node
            return

        temp = previous_node.next
        previous_node.next = node
        node.next = temp
        return self.head

    def remove_tail(self, previous_node):
        previous_node.next = None

    def get_previous_node(self):
        current_node = self.head
        previous_node = None
        while current_node.next:
            previous_node = current_node
            current_node = current_node.next
        return previous_node, current_node

    def print(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.value, end = ' ')
            current_node = current_node.next


    def reverse(self):
        current_node = self.head
        if current_node.next is None:
            return self.head
        next_node = current_node.next
        while next_node is not None:
            print(current_node.value, next_node.value)
            temp = next_node.next
            next_node.next = current_node
            current_node = next_node
            next_node = temp

        self.head.next = None
        self.head = current_node

        return self.head


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.add(None, Node(1))
    linked_list.add(linked_list.head, Node(5))
    linked_list.add(linked_list.head, Node(4))
    linked_list.add(linked_list.head, Node(3))
    linked_list.add(linked_list.head, Node(2))
    linked_list.reverse()
    print()
    linked_list.print() 
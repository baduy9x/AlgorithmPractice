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

if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.add(None, Node(1))
    linked_list.add(linked_list.head, Node(5))
    linked_list.add(linked_list.head, Node(4))
    linked_list.add(linked_list.head, Node(3))
    linked_list.add(linked_list.head, Node(2))
    current_node = linked_list.head

    linked_list.print()
    print()

    while current_node.next is not None:
        previous_node, last_node = linked_list.get_previous_node()

        if previous_node == current_node:
            break

        linked_list.remove_tail(previous_node)
        new_previous_node = current_node
        current_node = current_node.next
        linked_list.add(new_previous_node, last_node)
    linked_list.print()
        


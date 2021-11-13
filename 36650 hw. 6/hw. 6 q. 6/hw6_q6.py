class Node(object):
    def __init__(self, data):
        self.data = data
        self.previous = None


# Class to create a Linked List
class LinkedList(object):
    def __init__(self, tail=None):
        self.tail = tail

    def print_list(self):
        if self.tail == None:
            raise ValueError("List is empty")

        current = self.tail
        while current:
            print(current.data, end="  ")
            current = current.previous
        print("\n")

    def search(self, data):
        if self.tail == None:
            raise ValueError("List is empty")

        current = self.tail
        while current:
            if current.data == data: 
                return True
            current = current.previous
        return False

    # Delete a node in a linked list
    def delete(self, data):
        if not self.tail:
            return

        temp = self.tail

        # Check if tail node is to be deleted
        if self.tail.data == data:
            self.tail = temp.previous
            print("Deleted node is " + str(self.tail.data))
            return

        while temp.previous:
            if temp.previous.data == data:
                print("Node deleted is " + str(temp.previous.data))
                temp.previous = temp.previous.previous
                return
            temp = temp.previous
        print("Node not found")
        return
    
    def insert(self, data):
        new_node = Node(data)
        old_tail = self.tail
        self.tail = new_node
        new_node.previous = old_tail

first_node = Node(11)
linked_list = LinkedList(first_node)
linked_list.insert(3)
linked_list.insert(6)
linked_list.insert(5)

print("The Linked List is (after insertion):")
linked_list.print_list()

linked_list.delete(6)

print("The Linked List is (after deleting 6):")
linked_list.print_list()

print("Does 5 exist in the Linked List?")
print(linked_list.search(5))

print("Does 17 exist in the Linked List?")
print(linked_list.search(17))


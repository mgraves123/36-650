class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


# Class to create a Linked List
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    # Print the linked list
    def print_list(self):
        if self.head == None:
            raise ValueError("List is empty")

        current = self.head
        while current:
            print(current.data, end="  ")
            current = current.next
        print("\n")

    # Find length of Linked List
    def size(self):
        if self.head == None:
            return 0

        size = 0
        current = self.head
        while current:
            size += 1
            current = current.next

        return size

    # Insert a node in a linked list
    def insert(self, data):
        node = Node(data)
        current = self.head
        if not current:
            self.head = node
        else:
            while (current.next):
                current = current.next
            current.next = node

    # Delete a node in a linked list
    def delete(self, data):
        if not self.head:
            return

        temp = self.head

        # Check if head node is to be deleted
        if self.head.data == data:
            self.head = temp.next
            print("Deleted node is " + str(self.head.data))
            return

        while temp.next:
            if temp.next.data == data:
                print("Node deleted is " + str(temp.next.data))
                temp.next = temp.next.next
                return
            temp = temp.next
        print("Node not found")
        return
    
    def sort(self):
        if self.head==(None):
            return
        current = self.head
        while (current):
            next_node = current.next
            while (next_node):
                if current.data > next_node.data: 
                    tmp = current.data
                    current.data = next_node.data
                    next_node.data =  tmp
                next_node = next_node.next
            current = current.next
        return self
    
    def get_last_dup(self, first_dup, current_dup):
        while(current_dup.next is not None and first_dup.data == current_dup.next.data):
            current_dup = current_dup.next
        return current_dup.next
        
    def remove_dups(self):
        if self.head==(None):
            return
        self.sort()
        tmp = self.head
        next_node = tmp.next
        while (next_node):
            if tmp.data == next_node.data: 
                first_dup = tmp
                current_dup = next_node
                tmp.next = self.get_last_dup(first_dup, current_dup)
            tmp = tmp.next
            if tmp is None:
                next_node = None
            else: 
                next_node = tmp.next
        return 


first_node = Node(11)
linked_list = LinkedList(first_node)
linked_list.insert(3)
linked_list.insert(6)
linked_list.insert(6)
linked_list.sort()
print("The Linked List is:")
linked_list.print_list()

linked_list.remove_dups()
print("After removing duplicates Linked List is:")
linked_list.print_list()
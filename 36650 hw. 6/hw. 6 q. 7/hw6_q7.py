class Node:
    def __init__(self, data):
      self.small = None
      self.big = None 
      self.too_big = None
      self.data = data 
      
    def insert(self, data):
        if self.data:
            if ((data - self.data) < 0):
                if self.small is None:
                    self.small = Node(data)
                else:
                    self.small.insert(data)
            elif (0 <= (data - self.data) < 10):
                if self.big is None:
                    self.big = Node(data)
                else:
                    self.big.insert(data)
            else:
                if self.too_big is None:
                    self.too_big = Node(data)
                else:
                    self.too_big.insert(data)
        else:
            self.data = data

    def in_order_traversal_print(self):
        if self.small:
            self.small.in_order_traversal_print()
        print(self.data)
        if self.big:
            self.big.in_order_traversal_print()
        if self.too_big:
            self.too_big.in_order_traversal_print()

    def delete(self, lst, value):
        if self.small:
            self.small.delete(lst, value)
        lst.append(self.data)
        if self.big:
            self.big.delete(lst, value)
        if self.too_big:
            self.too_big.delete(lst, value)
        for i in range(len(lst)):
            if lst[i] == value: 
                lst.remove(value)
        return lst


root = Node(20)
root.insert(40)
root.insert(45)
root.insert(32)

root.in_order_traversal_print()

root.delete([], 45)

root.in_order_traversal_print()
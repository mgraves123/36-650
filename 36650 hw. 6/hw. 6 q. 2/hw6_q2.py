#https://www.geeksforgeeks.org/python-list-pop/
#https://www.tutorialspoint.com/python/python_loop_control.htm

class Queue:

    inner_list = []
    counter = 0

    def enqueue(self, value):
        self.inner_list.insert(self.counter, value)
        self.counter = self.counter + 1
        
        
    def dequeue(self):
        value = self.inner_list.pop(0)
        self.counter = self.counter - 1
        return value

    def delete(self, value):
        n = len(self.inner_list)
        for i in range(n):
            item = self.dequeue()
            if item == value:
                continue
            self.enqueue(item)
        return 

obj = Queue()
obj.enqueue(5)
obj.enqueue(7)
obj.enqueue(13)
obj.enqueue(4)
obj.enqueue(7)
obj.delete(7)
print(obj.dequeue())

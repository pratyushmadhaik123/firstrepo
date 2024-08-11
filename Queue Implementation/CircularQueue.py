class Queue:
    def __init__(self, limit=4, size=0, front=1, rear=4):
        self.items = []
        self.limit = limit
        self.size = size
        self.front = front
        self.rear = rear

    def IsFull(self):
        return self.size == self.limit
    
    def IsEmpty(self):
        return self.size == 0
    
    def Enqueue(self, item):
        if self.IsFull() == True:
            return "Queue is full. Unable to Enqueue item"
        else:
            self.items.append(item)
            self.size += 1
            if self.rear == self.limit:
                self.rear = 1
            else:
                self.rear += 1 
            return "list:" + str(self.items) + "  front:" + str(self.front) + "  rear:" + str(self.rear) + "  size:" + str(self.size) + "  LIMIT: " + str(self.limit)
        
    def Dequeue(self):
        if self.IsEmpty() == True:
            return "Empty Queue. Nun to Dequeue"
        else:
            deleted_item = self.items[0]
            self.items.remove(deleted_item)
            self.size -= 1
            if self.front == self.limit:
                self.front = 1
            else:
                self.front += 1
            return "list:" + str(self.items) + "  front:" + str(self.front) + "  rear:" + str(self.rear) + "  size:" + str(self.size) + "  LIMIT: " + str(self.limit) + '  DELETED item:' + str(deleted_item)


queue = Queue()
print(queue.Dequeue())
print(queue.Enqueue(1))
print(queue.Enqueue(2))
print(queue.Enqueue(3))
print(queue.Enqueue(4))
print(queue.Enqueue(5))
print(queue.Dequeue()) 

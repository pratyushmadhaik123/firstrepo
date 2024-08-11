class Queue:
    def __init__(self, max_size, size=0, front=0, rear=-1):
        self.items = []
        self.max_size = max_size
        self.size = size
        self.front = front
        self.rear = rear

    def IsEmpty(self):
        return self.size == 0

    def IsFull(self):
        return self.rear == self.max_size - 1

    def Enqueue(self, item):
        if self.IsFull() == True:
            return "Queue is Full. Unable to Enqueue"
        else:
            self.items.append(item)
            self.rear += 1
            self.size += 1
            return "  list:" + str(self.items) + "  front:" + str(self.front) + "  rear:" + str(self.rear) + "  size:" + str(self.size)
    
    def Dequeue(self):
        if self.IsEmpty() == True:
            return "Empty Queue. Nun to Dequeue"
        else:
            self.items.remove(self.items[0])
            self.rear -= 1
            self.size -= 1
            return "  list:" + str(self.items) + "  front:" + str(self.front) + "  rear:" + str(self.rear) + "  size:" + str(self.size)

        

queue = Queue(4)
print(queue.Dequeue())
print(queue.Enqueue(1))
print(queue.Enqueue(2))
print(queue.Enqueue(3))
print(queue.Enqueue(4))
print(queue.Enqueue(5))
print(queue.Dequeue())


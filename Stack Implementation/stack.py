class Stack:
    def __init__(self, max_size):
        self.items = []
        self.max_size = max_size

    def IsFull(self):
        return len(self.items) == self.max_size\
        
    def IsEmpty(self):
        return len(self.items) == 0
    
    def Push(self, item):
        if self.IsFull() == True:
            return "Full. Unable to push"
        else:
            self.items.append(item)
            return self.items
    
    def Pop(self):
        if self.IsEmpty() == True:
            return "Nun to Pop"
        else:
            self.items.pop()
            return self.items
    
    def Peek(self):
        if self.IsEmpty() == True:
            return "Nun to peek"
        else:
            return self.items[-1]
        


stack = Stack(4)
stack.Push(1)
stack.Push(2)
stack.Push(3)
stack.Push(4)
stack.Push(5)
stack.Pop()
stack.Peek()
stack.Pop()
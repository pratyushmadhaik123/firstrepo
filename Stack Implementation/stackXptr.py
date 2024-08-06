class Stack:
    def __init__(self, max_size, sb=0, sp=-1):
        self.items = []
        self.max_size = max_size
        self.sb = sb
        self.sp = sp

    def setsp(self, sp):
        self.sp = sp

    def getsp(self):
        return self.sp
    
    def setsb(self, sb):
        self.sb = sb

    def getsb(self):
        return self.sb
    
    def IsFull(self):
        return self.sp == self.max_size-1
        
    def IsEmpty(self):
        return self.sp == -1
    
    def Push(self, item):
        if self.IsFull() == True:
            return "Full. Unable to push"
        else:
            self.items.append(item)
            self.sp += 1
            return str(self.items) + " sp:" + str(self.sp)
    
    def Pop(self):
        if self.IsEmpty() == True:
            return "Nun to Pop"
        else:
            self.items.pop()
            self.sp -= 1
            return str(self.items) + " sp:" + str(self.sp)
    
    def Peek(self):
        if self.IsEmpty() == True:
            return "Nun to peek"
        else:
            return str(self.items) + " last item:" + str(self.items[-1]) + " sp:" + str(self.sp)
        


stack = Stack(4)
print(stack.Push(1))
print(stack.Push(2))
print(stack.Push(3))
print(stack.Push(4))
print(stack.Push(5))
print(stack.Pop())
print(stack.Peek())
print(stack.Pop())
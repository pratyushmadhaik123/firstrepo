#dyanmic linked list

class Node():
    def __init__(self, data, ptr=None):
        self.data = data
        self.ptr = ptr

    def setdata(self, data):
        self.data = data
    
    def getdata(self):
        return self.data
    
    def setptr(self, ptr):
        self.ptr = ptr
    
    def getptr(self):
        return self.ptr
    

class LinkedList():
    def __init__(self):
        self.start = None

    def insert(self, item):
        if self.start == None:
            self.start = Node(item)
        else:
            current = self.start
            if item < current.getdata():
                newNode = Node(item)
                newNode.setptr(self.start)
                self.start = newNode
            else:
                while current != None and current.getdata() < item:
                    current = current.getptr()
                previous = self.start
                while previous.getptr() != current:
                    previous = previous.getptr()
                newNode = Node(item)
                previous.setptr(newNode)
                newNode.setptr(current)

    def delete(self, item):
        if self.start == None:
            return "List is empty"
        else:
            current = self.start
            if item == current.getdata():
                print("Deleted node: " + item)
                self.start = current.getptr()
            else:
                while current != None and not current.getdata() > item:
                    current = current.getptr()
                deleted = self.start
                while deleted.getptr() != current:
                    deleted = deleted.getptr()
                if deleted.getdata() != item:
                    print("data not found")
                else:
                    previous = self.start
                    while previous.getptr() != deleted:
                        previous = previous.getptr()
                    previous.setptr(current)
                    print("Deleted nde: " + item)
    def display(self):
        i = 1
        current = self.start
        print("|{:^7}|{:^7}|".format("node", "name"))
        while current.getptr() != None:
            print("|{:^7}|{:^7}|".format(i, current.getdata()))
            current = current.getptr()
            i += 1
        print("{:^7}|{:<7}".format(i, current.getdata()))
            
a = LinkedList()
a.insert("hehe")
a.insert("lmao")
a.insert("train")
a.delete("lmao")
a.display()
a.insert("tree")
a.insert("man")
a.insert("bread")
a.delete("bread")
a.display()
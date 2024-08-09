##Linked List

class Node:

    def __init__(self, data):
        self.ptr = None
        self.data = data

    def getdata(self):
        return self.data

    def setdata(self, data):
        self.data = data

    def setptr(self, ptr):
        self.ptr = ptr

    def getptr(self):
        return self.ptr

class LinkedList:

    def __init__(self):
        self.start = None

    def insert(self, data):
        if self.start == None:
            self.start = Node(data)
        else:
            current = self.start
            if data < current.getdata():
                newNode = Node(data)
                newNode.setptr(self.start)
                self.start = newNode
            else:  
                while current != None and current.getdata() < data:
                    current = current.getptr()
                previous = self.start
                while previous.getptr() != current:
                    previous = previous.getptr()
                newNode = Node(data)
                previous.setptr(newNode)
                newNode.setptr(current)

    def delete(self, data):
        if self.start == None:
            return "List is empty"
        else:
            current = self.start
            if data == current.getdata():
                print("Deleted node: " + data)
                self.start = current.getptr()
            else:
                while current != None and not current.getdata() > data:
                    current = current.getptr()
                deleted = self.start
                while deleted.getptr() != current:
                    deleted = deleted.getptr()
                if deleted.getdata() != data:
                    print("Specified data not found")
                else:
                    previous = self.start
                    while previous.getptr() != deleted:
                        previous = previous.getptr()
                    previous.setptr(current)
                    print("Deleted node: " + data)
                

    def display(self):
        i = 1
        current = self.start
        print("{:^5}|{:<10}".format("node", "name"))
        while current.getptr() != None:
            print("{:^5}|{:<10}".format(i, current.getdata()))
            current = current.getptr()
            i += 1
        print("{:^5}|{:<10}".format(i, current.getdata()))


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
class Node():
    def __init__(self, data='', ptr=-1):
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
    def __init__(self, size=20):
        self.Nodes = [Node() for i in range(size)]
        self.start = -1
        self.nextfree = 0

        for i in range(len(self.Nodes)):
            self.Nodes[i].setptr(i + 1)

    def IsEmpty(self):
        return self.start == -1
    
    def IsFull(self):
        return self.nextfree == -1
    
    def Insert(self, item):
        #check is LL is full
        if self.IsFull() == True:
            print("No free nodes available")
            return
        #store item in nextfree
        self.Nodes[self.nextfree].setdata(item)

        #insert into empty linkedlist
        if self.start == -1:
            temp = self.Nodes[self.nextfree].getptr()
            self.Nodes[self.nextfree].setptr(-1)
            self.start = self.nextfree
            self.nextfree = temp

        else:
            previous = -1
            current = self.start
            while current != -1:
                if item < self.Nodes[current].getdata():
                    break
                previous = current
                current = self.Nodes[current].getptr()
            #insert into 1st Node
            if previous == -1:
                temp = self.Nodes[self.nextfree].getptr()
                self.Nodes[self.nextfree].setptr(self.start)
                self.start = self.nextfree
                self.nextfree = temp
            #insert into non-1st node
            else:
                temp = self.Nodes[self.nextfree].getptr()
                self.Nodes[self.nextfree].setptr(current)
                self.Nodes[previous].setptr(self.nextfree)
                self.nextfree = temp

    def Delete(self, item):
        #check if list is empty
        if self.IsEmpty() == True:
            print("Nothing to delete. Empty List")
            return

        previous = -1
        current = self.start
        while current != -1:
            if item == self.Nodes[current].getdata():
                break
            previous = current
            current = self.Nodes[self.nextfree].getptr()
        if current == -1:
            print("No node found")
            return
        self.Nodes[current].setName("<-DELETED->")

        #delete 1st Node
        if previous == -1:
            temp = self.nextfree
            self.nextfree = current
            self.Start = self.Nodes[current].getptr()
            self.Nodes[current].setptr(temp)
        #delete non-1st Node
        else:
            temp = self.nextfree
            self.nextfree = current
            self.Nodes[previous].setptr(self.Nodes[current].getptr())
            self.Nodes[current].setptr(temp)


    def Display(self):
        print('|{:^7}|{:^7}|{:^7}|'.format("Index", "Data", "Pointer"))
        for index in range(len(self.Nodes)):
            print('|{:^7}|{:^7}|{:^7}|'.format(index, self.Nodes[index].getdata(), self.Nodes[index].getptr()))
        print(self.start, self.nextfree)
        

def menu():
    print("""\n1. Initialise Linked List
2. Insert item
3. Delete item
4. Display Linked List
5. Exit Programm
    """)

def main():
    while True:
        menu()
        choice = input("Select your choice: ")
        if choice == '1':
            llst = LinkedList()
        elif choice == '2':
            try:
                item = input("Input item to insert: ")
                llst.Insert(item)
            except:
                print("Error. Cannot insert.")
        elif choice == '3':
            try:
                item = input("Input item to delete: ")
                llst.Delete(item)
            except:
                print("Error. Cannot delete.")
        elif choice == '4':
            try:
                llst.Display()
            except:
                print("Error in display.")
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid option selected. Select 1 to 5 only.")


main()
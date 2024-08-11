class ListNode():
    def __init__(self, name='', ptr=-1):
        self.__Name = name
        self.__Pointer = ptr

    def getName(self):
        return self.__Name

    def setName(self, name):
        self.__Name = name

    def getPointer(self):
        return self.__Pointer

    def setPointer(self, ptr):
        self.__Pointer = ptr

class LinkedList():
    def __init__(self, size=20):
        self.__Node = [ListNode() for i in range(size)]
        self.__Start = -1
        self.__NextFree = 0

        for i in range(len(self.__Node)):
            self.__Node[i].setPointer(i + 1)

    #self.__Node[self.__NextFree].setName()

    def IsEmpty(self):
        return self.__Start == -1

    def IsFull(self):
        return self.__NextFree == -1

    def Insert(self, item):
        # check if LinkedList is full
        if self.IsFull():
            print("No free nodes available")
            return
        # store item in NextFree
        self.__Node[self.__NextFree].setName(item)

        # insert into empty linked list
        if self.__Start == -1:
            temp = self.__Node[self.__NextFree].getPointer()
            self.__Node[self.__NextFree].setPointer(-1)
            self.__Start = self.__NextFree
            self.__NextFree = temp

        else:
            previous = -1
            current = self.__Start
            while current != -1:
                if item < self.__Node[current].getName():
                    break
                previous = current
                current = self.__Node[current].getPointer()
            # insert into 1st Node
            if previous == -1:
                temp = self.__Node[self.__NextFree].getPointer()
                self.__Node[self.__NextFree].setPointer(self.__Start)
                self.__Start = self.__NextFree
                self.__NextFree = temp
            # insert into non-1st Node
            else:
                temp = self.__Node[self.__NextFree].getPointer()
                self.__Node[self.__NextFree].setPointer(current)
                self.__Node[previous].setPointer(self.__NextFree)
                self.__NextFree = temp

    def Delete(self, Data):
        # check if LinkedList is empty
        if self.IsFull():
            print("Nothing to delete")
            return

        previous = -1
        current = self.__Start
        while current != -1:
            if Data == self.__Node[current].getName():
                break
            previous = current
            current = self.__Node[current].getPointer()
        if current == -1:
            print("no node found")
            return
        self.__Node[current].setName("<DELETED>")

        # delete 1st Node
        if previous == -1:
            temp = self.__NextFree
            self.__NextFree = current
            self.__Start = self.__Node[current].getPointer()
            self.__Node[current].setPointer(temp)
        # delete non-1st Node
        else:
            temp = self.__NextFree
            self.__NextFree = current
            self.__Node[previous].setPointer(self.__Node[current].getPointer())
            self.__Node[current].setPointer(temp)

    def Display(self):
        print("|{:^7}|{:^7}|{:^7}|".format("index", "data", "pointer"))
        for index in range(len(self.__Node)):
            print("|{:^7}|{:^7}|{:^7}|".format(index, self.__Node[index].getName(), self.__Node[index].getPointer()))

        print("StartPtr = ", self.__Start, "NextFree = ", self.__NextFree)

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
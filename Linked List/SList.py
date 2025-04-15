# 단순 연결 리스트 (Singly Linked List)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f"[{self.data}]"

class SList:
    def __init__(self):
        self.head = None
        self.count = 0  

    def find(self, value):
        current = self.head
        while current is not None:
            if current.data == value:
                return current
            else:
                current = current.next
        return None

    def remove(self, value):
        findNode = self.find(value)
        if findNode is None:
            return None
        else:
            current = self.head
            previous = None
            while current is not findNode:
                previous = current    
                current = current.next
            if previous is None:
                self.head = current.next
            else:
                previous.next = current.next
            current.next = None
            self.count -= 1
            return current

    def insertFront(self, newNode):
        if self.head is None:
            self.head = newNode
            self.count = 1
        else:
            newNode.next = self.head
            self.head = newNode
            self.count += 1

    def append(self, newNode):
        if self.head is None:
            self.head = newNode
            self.count = 1;
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = newNode
            self.count += 1

    def show(self):
        print("[Head]->", end="")
        current = self.head
        while current is not None:
            print(f"[{current.data}]- ", end ="")
            current = current.next

        print(f"||({self.count} nodes.)")

    def appendValue(self, value):
        self.append(Node(value))

    def reverse(self):
        revList = SList()

        while self.head is not None:
            n = self.shift()
            revList.insertFront(n)
        
        self.head = revList.head
        self.count = revList.count

    def shift(self):
        if self.head is None:
            return None
        else:
            header = self.head
            self.head = self.head.next
            header.next = None
            self.count -= 1
            return header
        
    def reverse2(self):
        current = self.head
        previous = None
        while current is not None:
            next = current.next
            current.next = previous

            previous = current
            current = next
        self.head = previous

    def sort(self, order="UP"):
        sortList = SList()
        current = self.head
        while current is not None:
            sortList.insertSorted(current.data, order)
            current = current.next
        self.head = sortList.head
        self.count = sortList.count

    def list(self):
        lst = list()
        current = self.head
        while current:
            lst.append(int(current.data))
            current = current.next
        return lst

    def insertSorted(self, newNode, order="UP"):
        if self.head is None:
            self.head = newNode
            self.count = 1
        else:
            current = self.head
            previous = None 

            while current is not None:
                if order == "UP":
                    check = newNode.data > current.data
                else:
                    check = newNode.data < current.data

                if check:
                    previous = current
                    current = current.next
                else:
                    if previous is None:
                        newNode.next = current
                        self.head = newNode
                    else:
                        previous.next = newNode
                        newNode.next = current
                    self.count += 1
                    return
            previous.next = newNode
            self.count += 1

    def copy(self):
        list = SList()
        current = self.head
        while current is not None:
            list.appendValue(current.data)
            current = current.next
        return list
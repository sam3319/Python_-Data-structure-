"""
    이중 연결 리스트 (Double Linked List)
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    def __str__(self):
        return f"[{self.data}]"
class DList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def append(self, data):
        newNode = Node(data)
        if  self.count == 0:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode 
        self.count += 1
    
    def show(self):
        print("head", end="->")
        current = self.head
        while current:
            print(current, end="-")
            current = current.next
        print(f"({self.count} nodes)")  

    def insertFront(self, data):
        if self.count == 0:
            self.append(data)
        else:
            newNode = Node(data)
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode
            self.count += 1

    def find(self, data):
        current = self.head
        while current:
            if current.data == data:
                break
            else:
                current = current.next
        return current     

    def insertBefore(self, targetNode, data):
        if targetNode is None:
            return
        if self.head is targetNode:
            self.insertFront(data)
        else:
            newNode = Node(data)

            newNode.next = targetNode
            newNode.prev = targetNode.prev
            targetNode.prev.next = newNode
            targetNode.prev = newNode

            self.count += 1

            return

    def insertAfter(self, targetNode, data):
        if targetNode is None:
            return       
        newNode = Node(data)

        if targetNode.next is not None:
            newNode.prev = targetNode
            newNode.next = targetNode.next
            targetNode.next.prev = newNode
            targetNode.next = newNode
        else:
            targetNode.next = newNode
            newNode.prev = targetNode
        self.count += 1

        return

    def insertSorted(self, data): 
        current = self.head
        while current:
            if current.data >= data:
                    self.insertBefore(current, data)
                    return
            else:
                current = current.next
        self.append(data)    

    def remove(self, targetNode):
        if targetNode is None:
            return
        if self.count == 1:
            self.head = None
            self.tail = None
            self.count = 0
            return
        elif self.head is targetNode:
            self.head = targetNode.next
            targetNode.next.prev = None
        elif self.tail is targetNode:
            self.tail = targetNode.prev
            targetNode.prev.next = None
        else:
            targetNode.prev.next = targetNode.next
            targetNode.next.prev = targetNode.prev
        self.count -= 1
        del targetNode

    def isEmpty(self):
        return True if self.count == 0 else False


# lst = DList()

# lst.append(10)
# lst.append(20)
# lst.append(30)



# lst.insertSorted(40)
# lst.insertSorted(50)
# lst.insertSorted(45)
# lst.remove(lst.find(40))
# lst.remove(lst.find(45))
# lst.remove(lst.find(50))


# lst.show()
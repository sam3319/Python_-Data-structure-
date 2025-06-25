"""
    이진 트리 (Binary Tree)
"""
from Queue import *

class BTree:
    def __init__(self, value):
        self.key = value
        self.left = None
        self.right = None

    def __str__(self):
        return f"[{self.key}]"
    
    def node(self):
        return f"{self.left if self.left else "[None]"}<-[{self.key}]->{self.right if self.right else "[None]"}"

    # 전위 순회
    def preOrder(self):
        print(self, end=" ")
        if self.left:
            self.left.preOrder()
        if self.right:
            self.right.preOrder()
    
    # 중위 순회
    # 1. 왼쪽으로 가서 출력
    # 2. 루트 출력
    # 3. 오른쪽으로 가서 출력
    def inOrder(self):
        if self.left:
            self.left.inOrder()

        print(self, end=" ")

        if self.right:
            self.right.inOrder()
            
    #후위 순회
    # 1. 왼쪽으로 가서 출력
    # 2. 오른쪽으로 가서 출력
    # 3. 루트 출력
    
    def postOrder(self):
        if self.left:
            self.left.inOrder()

        if self.right:
            self.right.inOrder()

        print(self, end=" ")
    
    # 레벨 순회
    def levelOrder(self):
        queue = Queue()
        queue.add(self)

        while not queue.isEmpty():
            node = queue.remove()
            print(node, end=" ")
            if node.left:
                queue.add(node.left)
            if node.right:
                queue.add(node.right)
        print("")
        
    # 주어진 이진 트리의 노드 수를 카운팅하여 반환
    def nodeCount(self):
        count = 1

        if self.left:
            count += self.left.nodeCount()

        if self.right:
            count += self.right.nodeCount()
            
        return count

    def height(self):
        if self.left is None and self.right is None:
            return 1
        if self.left is None:
            return self.right.height()+1
            
        if self.right is None:
            return self.left.height()+1

        return max(self.left.height(), self.right.height()) + 1
    
    # 완전 이진 트리

    def isComplete(self):
        queue = Queue()
        danger = False
        if self.left is None:
            return False
        
        queue.add(self)
        
        while not queue.isEmpty():
            node = queue.remove()
            if node.left:
                if danger:
                    return False
                else:
                    queue.add(node.left)
            else:
                danger = True
            if node.right:
                if danger:
                    return False
                queue.add(node.right)
            else:
                danger = True

        return True

    def toList(self):
        if not self.isComplete():
            return None
        lst = [None]
        queue = Queue()
        queue.add(self)
        while not queue.isEmpty():
            node = queue.remove()
            lst.append(node.key)
            if node.left:
                queue.add(node.left)
            if node.right:
                queue.add(node.right)
        
        return lst
#======================================================
class BSTree(BTree):

    def insert(self, value):
            if value < self.key:
                if self.left:
                    return self.left.insert(value)
                else:
                    self.left = BSTree(value)
                    return 1
            elif value > self.key:
                if self.right:
                    return self.right.insert(value)
                else:
                    self.right = BSTree(value)
                    return 1
            else:
                return 0
                


                    

        




        
                   
            
node = BSTree(100)

node.insert(50)
node.insert(30)
node.insert(100)
node.insert(60)

node.inOrder()


        





# nodeA = BTree("A")
# nodeB = BTree("B")
# nodeC = BTree("C")
# nodeD = BTree("D")
# nodeE = BTree("E")
# nodeF = BTree("F")
# nodeG = BTree("G")
# nodeH = BTree("H")


# nodeA.left = nodeB
# nodeA.right = nodeC

# nodeB.left = nodeD
# nodeB.right = nodeE

# nodeC.right = nodeF

# nodeD.right = nodeG

# nodeE.left = nodeH

# nodeA.preOrder()
# nodeA.inOrder()
# nodeA.postOrder()
# nodeA.inOrder()
# print(nodeA.nodeCount())
# print(nodeA.height())
# print(nodeA.isComplete())
# print(nodeA.toList())
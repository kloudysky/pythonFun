class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None

    def addFirst(self, data):
        node = Node(data)
        if self.isEmpty():
            self.first = node
            self.last = node
        else:
            node.next = self.first
            self.first = node

    def addLast(self, data):
        node = Node(data)
        if self.isEmpty():
            self.first = node
            self.last = node
        else:
            self.last.next = node
            self.last = node

    def isEmpty(self):
        return self.first == None

    def deleteFirst(self):
        if self.isEmpty():
            raise NotImplementedError("List is empty")
        if self.first == self.last:
            self.first = self.last = None
        else:
            second = self.first.next
            self.first = None
            self.first = second
    
    def deleteLast(self):
        if self.isEmpty():
            raise NotImplementedError("List is empty")
        if self.first == self.last:
            self.first = self.last = None
        else:
            previousNode = self._getPrevious(self.last)
            self.last = previousNode
            self.last.next = None

    def _getPrevious(self, node: Node):
        currentNode = self.first
        while currentNode:
            if currentNode.next == node:
                return currentNode
            currentNode = currentNode.next
        return None
    
    def contains(self, data):
        return self.indexOf(data) != -1

    def indexOf(self, data):
        idx = 0
        currentNode = self.first
        while currentNode is not None:
            if currentNode.data == data:
                return idx
            idx += 1
            currentNode = currentNode.next
        return -1
    
    def toList(self):
        if self.isEmpty():
            return []
        linkedListList = []
        currentNode = self.first
        while currentNode:
            linkedListList.append(currentNode.data)
            currentNode = currentNode.next
        return linkedListList

    def __len__(self):
        count = 0
        if self.isEmpty():
            return 0
        currentNode = self.first
        while currentNode:
            count += 1
            currentNode = currentNode.next
        return count

    def __str__(self):
        if self.isEmpty():
            return "Linked List is Empty"
        toList = f'{self.first.data}'
        currentNode = self.first.next
        while currentNode is not None:
            toList += f' -> {currentNode.data}'
            currentNode = currentNode.next
        return toList
    
    def __iter__(self):
        return iter(self.toList())
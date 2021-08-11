class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __str__(self):
        return f'{self.data}'

class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def addFirst(self, data):
        node = Node(data)
        if self.isEmpty():
            self.first = node
            self.last = node
        else:
            node.next = self.first
            self.first = node
        self.size += 1

    def addLast(self, data):
        node = Node(data)
        if self.isEmpty():
            self.first = node
            self.last = node
        else:
            self.last.next = node
            self.last = node
        self.size += 1

    def isEmpty(self):
        return self.first == None

    def deleteFirst(self):
        if self.isEmpty():
            return
        if self.first == self.last:
            self.first = self.last = None
        else:
            second = self.first.next
            self.first = None
            self.first = second
        self.size -= 1
    
    def deleteLast(self):
        if self.isEmpty():
            return
        if self.first == self.last:
            self.first = self.last = None
        else:
            previousNode = self._getPrevious(self.last)
            self.last = previousNode
            self.last.next = None
        self.size -= 1

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
    
    def reverse(self):
        if self.isEmpty():
            return
        previous = self.first
        current = self.first.next
        while current:
            next = current.next
            current.next = previous
            previous = current
            current = next
        self.last = self.first
        self.last.next = None
        self.first = previous

    def __len__(self):
        return self.size

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
class Heap:
    def __init__(self) -> None:
        self._items = []

    def push(self, val):
        self._items.append(val)
        self._bubbleUp()
    
    def _bubbleUp(self):
        idx = len(self._items) - 1
        while idx > 0 and self._items[idx] > self._items[self._parentIdx(idx)]:
            self._swap(idx, self._parentIdx(idx))
            idx = self._parentIdx(idx)

    def peak(self):
        return self._items[0]

    def pop(self):
        if self.isEmpty():
            return self._items
        peak = self._items.pop(0)

        if not self.isEmpty():
            self._bubbleDown()

        return peak

    def _bubbleDown(self):
        last = self._items.pop()
        self._items.insert(0, last)

        idx = 0
        while idx <= len(self._items) and not self._isValidParent(idx):
            largerChildIndex = self._largerChildIdx(idx)
            self._swap(idx, largerChildIndex)
            idx = largerChildIndex

    def _largerChildIdx(self, idx):
        if not self._hasLeftChild(idx):
            return idx

        if not self._hasRightChild(idx):
            return self._rightChild(idx)

        if self._leftChild(idx) > self._rightChild(idx):
            return self._leftChild(idx)
        else:
            return self._rightChild(idx)

    def _hasLeftChild(self, idx):
        self._leftIndex(idx) <= len(self._items)

    def _hasRightChild(self, idx):
        self._rightIndex(idx) <= len(self._items)

    def _isValidParent(self, idx):
        if not self._hasLeftChild(idx):
            return True
        
        if not self._hasRightChild(idx):
            return self._items[idx] >= self._leftChild(idx) 

        return self._items[idx] >= self._leftChild(idx) and self._items[idx] >= self._rightChild(idx)

    def _leftChild(self, idx):
        return self._items[self._leftIndex(idx)]

    def _rightChild(self, idx):
        return self._items[self._rightIndex(idx)]

    def _leftIndex(self, idx):
        return idx * 2 + 1

    def _rightIndex(self, idx):
        return idx * 2 + 2

    def _parentIdx(self, idx):
        return (idx - 1) // 2

    def isEmpty(self):
        return len(self._items) == 0

    def _swap(self, idxA, idxB):
        temp = self._items[idxA]
        self._items[idxA] = self._items[idxB]
        self._items[idxB] = temp

    def __str__(self):
        return str(self._items)
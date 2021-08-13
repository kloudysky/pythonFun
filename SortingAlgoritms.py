class BubbleSort:
    
    @classmethod
    def sort(cls, l: list) -> None:
        swapped = True
        while swapped:
            swapped = False
            for i in range(len(l) - 1):
                i2 = i + 1
                if l[i] > l[i2]:
                    cls._swap(l, i, i2)
                    swapped = True
    
    @classmethod
    def _swap(cls, l: list, idx1: int, idx2: int) -> None:
        l[idx1], l[idx2] = l[idx2], l[idx1]

class SelectionSort:

    @classmethod
    def sort(cls, l: list) -> None:
        for i in range(len(l)):
            for j in range(i, len(l)):
                if l[j] < l[i]:
                    cls._swap(l, j, i)

    @classmethod
    def _swap(cls, l: list, idx1: int, idx2: int) -> None:
        l[idx1], l[idx2] = l[idx2], l[idx1]

class InsertionSort:

    @classmethod
    def sort(cls, l: list) -> None:
        for i in range(1, len(l)):
            current = l[i]
            j = i - 1
            while j >= 0 and l[j] > current:
                l[j + 1] = l[j]
                j -= 1
            l[j + 1] = current

class MergeSort:

    @classmethod
    def sort(cls, l: list) -> None:
        if len(l) < 2:
            return

        mid = len(l) // 2
        left = l[:mid]
        right = l[mid:]

        cls.sort(left)
        cls.sort(right)

        cls._merge(l, left, right)

    @classmethod
    def _merge(cls, l: list, left: list, right: list) -> None:
        i = j = k = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                l[k] = left[i]
                i += 1
            else:
                l[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            l[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            l[k]=right[j]
            j += 1
            k += 1

class QuickSort:

    @classmethod
    def sort(cls, l: list) -> None:
        cls._sort(l, 0, len(l) - 1)

    @classmethod
    def _sort(cls, l: list, start: int, end: int): 
        if start >= end:
            return

        boundary = cls._partition(l, start, end)
        
        cls._sort(l, start, boundary - 1)
        cls._sort(l, boundary + 1, end)

    @classmethod
    def _partition(cls, l: list, start: int, end: int) -> int:
        pivot = l[end]
        boundary = start - 1
        for i in range(start, end + 1):
            if l[i] <= pivot:
                boundary += 1
                cls._swap(l, i, boundary)
        
        return boundary
    
    @classmethod
    def _swap(cls, l: list, idx1: int, idx2: int) -> None:
        l[idx1], l[idx2] = l[idx2], l[idx1]

class CountingSort:

    @classmethod
    def sort(cls, l: list) -> None:
        counts = [0 for _ in range(len(l))]
        for num in l:
            counts[num] += 1

        k = 0
        for i in range(len(counts)):
            for j in range(counts[i]):
                l[k] = i
                k += 1

class BucketSort:

    @classmethod
    def sort(cls, l: list) -> None:
        buckets = [[] for _ in range(len(l))]
        for num in l:
            buckets[num // len(buckets)].append(num)
        
        k = 0
        for bucket in buckets:
            bucket.sort()
            for num in bucket:
                l[k] = num
                k += 1

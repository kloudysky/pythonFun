class DynamicArray(object):
    def __init__(self):
        self.size = 0
        self.capacity = 1
        self.array = self._create_array(self.capacity)
        
    def __len__(self):
        return self.size
    
    def __str__(self):
        if self.size == 0:
            return '[]'
        array_string = 'DynamicArray - ['
        for i in range(self.size - 1):
            array_string += str(self.array[i]) + ', '
        array_string += str(self.array[self.size - 1]) + ']'
        return array_string

    def __getitem__(self, index):
        if not 0 <= index < self.size:
            raise IndexError(f'Given index: {index} is out of range. Current array size: {self.size}')
        
        return self.array[index]

    def _create_array(self, length):
        return [None] * length

    def _resize(self, new_capacity):
        new_array = self._create_array(new_capacity)
        
        for i in range(self.size):
            new_array[i] = self.array[i]
            
        self.array = new_array
        self.capacity = new_capacity
        
    def append(self, element):
        if self.size == self.capacity:
            self._resize(2 * self.capacity)
        
        self.array[self.size] = element
        self.size += 1
    
    def pop(self, index=None):
        if not index:
            index = self.size - 1
        if not 0 <= index < self.size:
            return IndexError(f'Given index: {index} is out of range. Current array size: {self.size}')
        
        print(index)
        element = None

        if self.size > 0:
            element = self.array[index]
            for i in range(index, self.size):
                self.array[i] = self.array[i + 1]
            self.array[self.size - 1] = None
            self.size -= 1
            
            if self.size < self.capacity // 4:
                self._resize(self.capacity // 2)
        
        return element
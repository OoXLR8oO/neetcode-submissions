class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.current = 0
        self.data = [None] * capacity

    def get(self, i: int) -> int:
        return self.data[i]

    def set(self, i: int, n: int) -> None:
        self.data[i] = n

    def pushback(self, n: int) -> None:
        if self.current == self.capacity:
            self.resize()
        self.data[self.current] = n
        self.current = self.current + 1

    def popback(self) -> int:
        val = self.data[self.current - 1]
        self.current = self.current - 1
        return val
 
    def resize(self) -> None:
        temp_data = [None] * (self.capacity * 2)
        for i in range(self.current):
            temp_data[i] = self.data[i]
        self.data = temp_data
        self.capacity = self.capacity * 2

    def getSize(self) -> int:
        return self.current
    
    def getCapacity(self) -> int:
        return self.capacity
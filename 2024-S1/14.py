class MaxHeap:
    def __init__(self):
        self.binary_heap = [0]
        self.size = 0
        
    def is_empty(self):
        return self.size == 0 
        
    def percolate_up(self, i):
        while i // 2 > 0 and self.binary_heap[i].score > self.binary_heap[i//2].score:
            self.binary_heap[i], self.binary_heap[i//2] = self.binary_heap[i//2], self.binary_heap[i]
            i = i // 2
            
    def insert(self, gamer):
        self.binary_heap.append(gamer)
        self.size += 1
        self.percolate_up(self.size)
        
    def get_larger_child_index(self, i):
        if i * 2 + 1 > self.size:
            return i * 2
        else:
            if self.binary_heap[i*2].score > self.binary_heap[i*2+1].score:
                return i * 2
            else:
                return i * 2 + 1
                
    def percolate_down(self, i):
        while (i * 2) <= self.size:
            larger_child_index = self.get_larger_child_index(i)
            if self.binary_heap[i].score < self.binary_heap[larger_child_index].score:
                self.binary_heap[larger_child_index], self.binary_heap[i] = self.binary_heap[i], self.binary_heap[larger_child_index]
            i = larger_child_index

    def get_max_value(self):
        max_value = self.binary_heap[1]
        self.binary_heap[1] = self.binary_heap[-1]
        self.binary_heap.pop()
        self.size -= 1
        self.percolate_down(1)
        return max_value
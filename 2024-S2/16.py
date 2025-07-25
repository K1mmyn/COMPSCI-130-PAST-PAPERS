class PriorityQueue:
    def __init__(self):
        self.binary_heap = [0]
        self.size = 0
        self.number_of_swaps = 0
        
    def merge(self, other):
        self.create_heap_fast(other.binary_heap[1:])

    def __str__(self):
        return str(self.binary_heap)

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def percolate_up(self, i):
        while i // 2 > 0 and self.binary_heap[i] < self.binary_heap[i//2]:
            self.binary_heap[i], self.binary_heap[i//2] = self.binary_heap[i//2], self.binary_heap[i]
            self.number_of_swaps += 1
            i = i // 2

    def insert(self, item):
        self.binary_heap.append(item)
        self.size += 1
        self.percolate_up(len(self))

    def get_smaller_child_index(self, i):
        if i * 2 + 1 > self.size:
            return i * 2
        else:
            if self.binary_heap[i*2] < self.binary_heap[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1

    def percolate_down(self, i):
        while (i * 2) <= self.size:
            mc = self.get_smaller_child_index(i)
            if self.binary_heap[i] > self.binary_heap[mc]:
                self.binary_heap[mc], self.binary_heap[i] = self.binary_heap[i], self.binary_heap[mc]
                self.number_of_swaps += 1
            i = mc

    def create_heap_fast(self, values):
        for index in range(len(values)):
            self.binary_heap.append(values[index])
            self.size += 1
        for index in range(len(self.binary_heap)//2, 0, -1):
            self.percolate_down(index)    

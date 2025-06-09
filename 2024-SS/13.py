class LinearHashTable:
    def __init__(self, size=7):
        self.size = size
        self.slots = [None] * size
        self.count = 0
        
    def __str__(self):
        return str(self.slots)
        
    def get_hash_code(self, key):
        return key % self.size
        
    def clear(self):
        self.slots = [None] * self.size
        
    def is_empty(self):
        return self.__len__() == 0
        
    def __len__(self):
        count = 0
        for item in self.slots:
            if item != None:
                count += 1
        return count
        
    def load_factor(self):
        return self.count / self.size
        
    def put(self, key):
        if self.__len__() >= self.size:
            raise IndexError("ERROR: The hash table is full.")
        self.count += 1
            
        index = self.get_hash_code(key)
        
        while self.slots[index] != None:
            index = (index + 1) % self.size
        self.slots[index] = key
            
        if self.load_factor() > 0.7:
            self.rehash()
        
        
    def rehash(self):
        self.size *= 2
        self.count = 0
        old_data = self.slots
        self.slots = [None] * self.size
        
        for key in old_data:
            if key is not None:
                self.put(key)
        
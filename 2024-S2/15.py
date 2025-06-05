class QuadraticHashTable:
    def __init__(self, size=7):
        self.size = size
        self.slots = [None] * size

    def __str__(self):
        return str(self.slots)

    def get_hash_index(self, key):
        return (100 * key[0] + key[1]) % self.size

    def clear(self):
        self.slots = [None] * self.size

    def put(self, key):
        original_index = index = self.get_hash_index(key)
        increment = 1
        while self.slots[index] != None:
            index = (original_index + increment ** 2) % self.size
            increment += 1
        self.slots[index] = key
        return (increment-1)

    def is_empty(self):
        return self.__len__() == 0

    def __len__(self):
        return sum(1 for slot in self.slots if slot is not None)
        
def total_num_collisions(table, positions):
    total = 0
    for position in positions:
        collisions = table.put(position)
        total += collisions
        
    return total

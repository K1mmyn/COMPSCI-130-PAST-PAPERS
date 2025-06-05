class SequenceIterator:
    def __init__(self, numbers):
        self.numbers = numbers
        self.current = 0
        
    def __next__(self):
        if self.current == len(self.numbers):
            raise StopIteration
            
        num = self.numbers[self.current]
        self.current += 1
        return num
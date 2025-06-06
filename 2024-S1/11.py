class  DivisibleNumbersIterator:
    def __init__(self, number_of_terms=5, divisor=1):
        self.number_of_terms = number_of_terms
        self.divisor = divisor
        self.current = divisor
        self.count = 0
        
    def __next__(self):
        if self.count == self.number_of_terms:
            raise StopIteration()
            
        self.count += 1    
        num = self.count * self.divisor
        return num
class RecamanSequence:
    def __init__(self, terms=2):
        self.numbers = []
        for i in range(terms):
            self.numbers.append(self.add_recursive(i))
            
    def add_recursive(self, n):
        if n == 0:
            return 0
            
        num = self.numbers[-1] - n
        
        if num > 0 and num not in self.numbers:
            return num
        else:
            return num + (2 * n)
    
    def __str__(self):
        return str(self.numbers)
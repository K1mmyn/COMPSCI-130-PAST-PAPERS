class PlateNumber:
    def __init__(self, code="AAA111"):
        self.code = code
        self.letters = "".join([char for char in code if char.isalpha()])
        self.digits = int("".join([char for char in code if char.isdigit()]))
        
    def __str__(self):
        return f"{self.code}({self.letters},{self.digits})"
        
    def __eq__(self, other):
        if not isinstance(other, PlateNumber):
            return False
            
        return self.code == other.code
        
    def __lt__(self, other):
        if not isinstance(other, PlateNumber):
            return False
            
        if self.letters == other.letters:
            return self.digits < other.digits
            
        return self.letters < other.letters
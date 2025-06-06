class ParkingSlot:
    def __init__(self, code="UNKNOWN"):
        self.code = code
        self.available = True
        
    def is_available(self):
        return self.available == True
        
    def set_occupied(self):
        self.available = False
    
    def __str__(self):
        message = "available"
        if not self.is_available():
            message = "occupied"
        return f"{self.code} ({message})"
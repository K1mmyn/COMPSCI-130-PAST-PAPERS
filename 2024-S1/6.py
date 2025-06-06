class ParkingBlock:
    def __init__(self, name, prefix, capacity):
        self.name = name
        self.capacity = capacity
        self.parking_slots = [ParkingSlot(f"{prefix}{x}") for x in range(capacity)]
        
    def get_first_available_slot(self):
        for slot in self.parking_slots:
            if slot.is_available():
                return slot
                
        return None
        
    def get_available_list(self):
        return [slot for slot in self.parking_slots if slot.is_available()]
        
    def get_available_slots_count(self):
        return len(self.get_available_list())
        
    def __str__(self):
        slots = self.get_available_list()
        return f"{self.name}({len(slots)}): " + ",".join([str(slot) for slot in slots])
class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0
    
    def size(self):
        return self.count
    
    def add(self, item): 
        self.head = Node(item, self.head)
        self.count += 1
    
    def clear(self):
        self.head = None
        self.count = 0
        
    def is_empty(self):
        return self.count == 0
    
    def __str__(self):
        if self.count > 0:
            current = self.head
            data = []
            while current != None:
                data += [current.get_data()]
                current = current.get_next()
            return "Head: " + " --> ".join(str(d) for d in data)
        return ''
        
    def remove_first_odd_node(self):
        current = self.head
        previous = None
        node_removed = None
        
        while node_removed is None and current is not None:
            if current.data % 2 == 1:
                next_node = current.next
                node_removed = current
                self.count -=1
                
                if previous is None:
                    self.head = next_node
                    continue 
                previous.next = next_node
                
            else:
                previous = current
                current = current.next
                
        return node_removed
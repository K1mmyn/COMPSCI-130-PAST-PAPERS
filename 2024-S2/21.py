class LinkedList:    
    def __init__(self):
        self.head = None
        self.count = 0

    def add(self, item): 
        self.head = Node(item, self.head)
        self.count += 1

    def get_head(self):
        return self.head

    def size(self):
        return self.count

    def clear(self):
        self.head = None
        self.count = 0   

    def is_empty(self):
        return self.count == 0

    def __str__(self):
        if self.count > 0:
            current = self.head
            data = []
            while current:
                data.append(str(current.get_data()))
                current = current.next
            return "Head: " + " --> ".join(data)
        return ''
        
    def swap_pairs_of_nodes(self):
        if self.head is None or self.head.next is None:
            return

        previous = None
        current_node = self.head
        next_node = current_node.next
        
        
        while next_node is not None:
            if previous is None:
                self.head = next_node
                
            current_node.next = next_node.next
            next_node.next = current_node
            previous = current_node

            current_node = current_node.next
            
            if current_node is None or current_node.next is None:
                next_node = None
            else:
                next_node = current_node.next
                previous.next = next_node
            
            
            
        
            
            
            
            
        
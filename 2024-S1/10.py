class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def add(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node
        self.count += 1
        
    def __str__(self):
        self_str = "head --> "
        if self.is_empty():
            self_str += "None"
        else:
            current = self.head
            while current != None:
                if current.next == None:
                    self_str += str(current)
                else:
                    self_str += str(current) + " --> "
                current = current.next
        return self_str
        
    def swap_ends(self):
        if self.head is None or self.head.next is None:
            return 
        
        first_node = self.head
        previous = None
        current = first_node
        
        while current.next is not None:
            previous = current
            current = current.next
            
        last_node = current
        
        if first_node.next == last_node:
            last_node.next = first_node
            first_node.next = None
            self.head = last_node
            return
            
        
        last_node.next = first_node.next
        previous.next = first_node
        first_node.next = None
        self.head= last_node
            
        
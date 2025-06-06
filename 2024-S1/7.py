def interleave_stacks(stack1, stack2):
    def add_remaining_item(stack, stack_to_add):
        while not stack_to_add.is_empty():
            stack.push(stack_to_add.pop())
            
    s = Stack()
    s1 = Stack()
    s2 = Stack()
    
    while not stack1.is_empty():
        s1.push(stack1.pop())
    while not stack2.is_empty():
        s2.push(stack2.pop())
        
    while not s1.is_empty() and not s2.is_empty():
        s.push(s1.pop())
        s.push(s2.pop())
        
    if s1.is_empty():
        add_remaining_item(s, s2)
    else:
        add_remaining_item(s, s1)
        
    return s
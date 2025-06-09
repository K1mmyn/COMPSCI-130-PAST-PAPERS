def delete_mid(a_stack):
    s = Stack()
    if a_stack.is_empty():
        return
    if a_stack.size() % 2 == 0:
        for i in range(a_stack.size() //2 - 1):
            s.push(a_stack.pop())
    else:
        for i in range(a_stack.size() //2):
            s.push(a_stack.pop())
            
    a_stack.pop()
    while not s.is_empty():
        a_stack.push(s.pop())
def double_reverse(string):
    s = Stack()
    f_string = ""
    
    for char in string:
        s.push(char)
        
    while not s.is_empty():
        substring = ""
        while not s.peek().isalpha():
            substring += s.pop()
            
        f_string +=  s.pop() + substring
    
    return f_string
    
        
    
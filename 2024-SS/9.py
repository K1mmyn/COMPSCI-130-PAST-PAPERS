def reverse_queue_region(a_queue, start, end):
    s = Stack()
    for i in range(1, start):
        a_queue.enqueue(a_queue.dequeue())
        
    for i in range(start, end + 1):
        s.push(a_queue.dequeue())
        
    for i in range(start, end + 1):
        a_queue.enqueue(s.pop())
        
    for i in range(end, a_queue.size()):
        a_queue.enqueue(a_queue.dequeue())
        
    return a_queue
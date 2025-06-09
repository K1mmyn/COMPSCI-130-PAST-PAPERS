def max_product_of_k(numbers, k):
    if k > len(numbers):
        return None
    pq = PriorityQueue()
    
    for num in numbers:
        pq.insert(num)
        
    for i in range(pq.size - k):
        pq.delete_minimum()

    total = 1    
    for i in range(pq.size):
        total *= pq.delete_minimum()
    return total
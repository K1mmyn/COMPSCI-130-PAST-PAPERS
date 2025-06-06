def collecting_sweets(sweet_queue):
    count = 1
    
    while not sweet_queue.is_empty():
        for i in range(sweet_queue.size()):
            child = sweet_queue.dequeue()
            if child[1] + (count * 5) < 50:
                sweet_queue.enqueue(child)
                print(f"{child[0]} has {child[1] + (count*5)} sweets and rejoins the queue!")
            else:
                print(f"{child[0]} has {child[1] + (count*5)} sweets and goes home happy!")
                
        count += 1
class Student:
    def __init__(self, name, friends): 
        self.name = name        
        self.friends = friends
        
def print_all_connections_by_distance(student):
    q = Queue()
    
    for friend in student.friends:
        q.enqueue(friend)
    
    while not q.is_empty():
        last_student = q.dequeue()
        for friend in last_student.friends:
            q.enqueue(friend)
        print(last_student.name, end=" ")
        
    
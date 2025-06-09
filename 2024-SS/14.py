class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def insert_left(self, new_data):
        if self.left == None:
            self.left = BinaryTree(new_data)
        else:
            t = BinaryTree(new_data, left=self.left)
            self.left = t

    def insert_right(self, new_data):
        if self.right == None:
            self.right = BinaryTree(new_data)
        else:
            t = BinaryTree(new_data, right=self.right)
            self.right = t

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right

    def __iter__(self):
        return BTLevelorderIterator(self)
    #insert the __iter__(self) method here

class BTLevelorderIterator:
    def __init__(self, btree):
        self.tree = btree
        self.queue = Queue()
        self.queue.enqueue(btree)
        
    def __next__(self):
        if self.queue.is_empty():
            raise StopIteration()
        
        tree = self.queue.dequeue()
        if tree.left is not None:
            self.queue.enqueue(tree.left)
        if tree.right is not None:
            self.queue.enqueue(tree.right)
        return tree

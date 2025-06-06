def add_odd_data(binary_tree):
    if binary_tree is None:
        return 0
        
    if binary_tree.data % 2 == 1:
        return add_odd_data(binary_tree.left) + int(binary_tree.data) + add_odd_data(binary_tree.right)
    
    else:
        return add_odd_data(binary_tree.left) + add_odd_data(binary_tree.right)
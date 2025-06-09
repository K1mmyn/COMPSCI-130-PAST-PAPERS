def count_nodes_len_greater_than(binary_tree, length):
    if binary_tree is None:
        return 0
    
    total = count_nodes_len_greater_than(binary_tree.left, length) + count_nodes_len_greater_than(binary_tree.right, length)
        
    if len(binary_tree.data) > length:
        total += 1
        
    return total
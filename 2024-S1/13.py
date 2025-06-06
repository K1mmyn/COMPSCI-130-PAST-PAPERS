def reconstruct_tree(inorder_sequence, preorder_sequence):
    if len(inorder_sequence) == 0 or len(preorder_sequence) == 0:
        return None
        
    root = preorder_sequence.pop(0)
    root_index = inorder_sequence.index(root)
    
    l_in, r_in = inorder_sequence[:root_index], inorder_sequence[root_index + 1:]
    l_pre, r_pre = preorder_sequence[:len(l_in)], preorder_sequence[len(l_in):]
    
    return [root, reconstruct_tree(l_in, l_pre), reconstruct_tree(r_in, r_pre)]
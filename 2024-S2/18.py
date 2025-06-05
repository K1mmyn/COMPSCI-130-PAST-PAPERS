def bst_values_below(bst, max_value):
    if bst is None:
        return []
        
    if bst.data >= max_value:
        return bst_values_below(bst.left, max_value)
        
    return bst_values_below(bst.left, max_value) +  [bst.data] + bst_values_below(bst.right, max_value)
    
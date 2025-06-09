def get_sorted_list(search_tree):
    if search_tree is None:
        return []
        
    return get_sorted_list(search_tree.right) + [search_tree.data] + get_sorted_list(search_tree.left)
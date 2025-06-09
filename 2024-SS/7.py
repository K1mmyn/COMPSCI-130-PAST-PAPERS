def create_chain_nodes_from_list(a_list):
    if not len(a_list):
        return
    first_node = Node(a_list[0])
    current = first_node
    for i in range(1, len(a_list)):
        current.next = Node(a_list[i])
        current = current.next
        
    return first_node
        
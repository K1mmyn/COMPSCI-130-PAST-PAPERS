def create_nodes_chain(a_stack):
    head_node = Node(a_stack.pop())
    while not a_stack.is_empty():
        previous_node = Node(a_stack.pop())
        previous_node.next = head_node
        head_node = previous_node
        
    return head_node
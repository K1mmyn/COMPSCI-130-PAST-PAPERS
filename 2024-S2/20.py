def simplify_one_step(tree):
    operation = {
        "*": lambda x,y: x * y,
        "/": lambda x,y: x // y,
        "-": lambda x,y: x - y,
        "+": lambda x,y: x + y,
    }
    if tree.left is None or tree.right is None:
        return
    
    if isinstance(tree.left.data, int) and isinstance(tree.right.data, int):
        num = operation[tree.data](int(tree.left.data), int(tree.right.data))
        tree.data = num
        tree.left,tree.right = None, None
        return tree.data
        
    simplify_one_step(tree.left)
    simplify_one_step(tree.right)
def complex_recursion(n, k):
    if n <= 0 or k <= 0:
        return 1,0
        
    if n < k:
        x = complex_recursion(n + 1, k -2)
        return (x[0] + (2 * n), x[1] + 1)
    else:
        x = complex_recursion(n - 1, k)
        y = complex_recursion(n - 2, k)
        return (x[0] + y[0], x[1] + y[1] + 2)
        
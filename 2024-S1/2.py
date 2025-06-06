def remove_even_multiples_of_7(numbers):
    for i in range(len(numbers) - 1, -1 ,-1):
        if numbers[i] % 2 == 0 and numbers[i] % 7 == 0:
            numbers.pop(i)
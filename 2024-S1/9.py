def get_max_odd_num(positive_numbers):
    if len(positive_numbers) == 0:
        return 0
        
    num = positive_numbers[0]
    
    if num % 2 == 1 and num > get_max_odd_num(positive_numbers[1:]):
        return num
    else:
        return get_max_odd_num(positive_numbers[1:])
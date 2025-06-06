def prompt_odd_larger(limit):
    user_input = None
    
    while user_input is None:
        try:
            user_num = int(input(f"Enter an odd integer larger than {limit}: "))
            if user_num % 2 == 1 and user_num > limit:
                user_input = user_num
        except ValueError:
            print("Invalid input!")
            
    return user_input
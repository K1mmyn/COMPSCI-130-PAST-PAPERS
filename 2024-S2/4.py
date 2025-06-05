def prompt_weekday():
    weekday_dict = {1:'Monday', 2:'Tuesday', 3:'Wednesday', 
      4:'Thursday', 5:'Friday', 6:'Saturday', 7:'Sunday'}
      
    user_day = None
    while user_day == None:
        try:
            user_input = int(input("Enter a weekday digit (1-7): "))
            if user_input >= 1 and user_input <= 7:
                user_day = user_input
        except ValueError:
            pass
        
    return weekday_dict[user_day]
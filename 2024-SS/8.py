def contains_letter(a_word, a_letter):
    if a_letter not in a_word:
        return (False, -1)
        
    result = contains_letter(a_word[1:], a_letter)
        
    if a_letter == a_word[0]:
        return (True, 0)
    else:
        return (result[0], result[1] + 1)
        
    
def categorize_marks_by_range(filename, number_of_ranges):
    try:
        file = open(filename)
        content = file.read().split('\n')
        
        number_dict = {}
        step = 100 // number_of_ranges
        
        for x in range(number_of_ranges):
            number_dict[x * step] = []
         
        for num in content:
            num = int(num)
            for key in number_dict.keys():
                if num >= key and num < (key + step):
                    number_dict[key].append(num)
                
        for key in number_dict.keys():
            number_dict[key] = sorted(number_dict[key])
        file.close()        
        return number_dict
            
            
            
    except FileNotFoundError:
        print(f"ERROR: The file '{filename}' does not exist.")
        return {}
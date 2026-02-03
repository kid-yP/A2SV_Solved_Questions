def swap_case(s):
    result_list = []
    
    for ch in s:
        if ch.islower():
            result_list.append(ch.upper())
        elif ch.isupper():
            result_list.append(ch.lower())
            
        else:
            result_list.append(ch) 
    return "".join(result_list)

  
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

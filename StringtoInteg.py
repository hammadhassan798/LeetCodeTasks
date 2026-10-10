def correctstring(s):
    newst = ""
    counter = 0
    
    for i in s:
        if i == " " and counter == 0:
            continue
        elif i == " " and counter > 0:
            break 
        elif i == "-" and counter == 0:
            newst += i
        elif i == "+" and counter == 0:
            newst += i
        elif i >= "0" and i <= "9":  
            newst += i
        else:
            break 
        
        counter += 1
        
    return newst
def stringtoint(s):
    found = correctstring(s)
    sign = 1
    res = 0
    
    if found == "" or found == "+" or found == "-":
        return 0
    
    start_index = 0

    if found[0] == "-":
        sign = -1
        start_index = 1  
    elif found[0] == "+":
        start_index = 1 
  
    for i in range(start_index, len(found)):
        digit = ord(found[i]) - ord("0")
        res = (res * 10) + digit
        
    res *= sign
   
    INT_MAX = 2147483647
    INT_MIN = -2147483648
    if res > INT_MAX:
        return INT_MAX
    if res < INT_MIN:
        return INT_MIN
        
    return res
print(stringtoint("42"))
    
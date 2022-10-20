def normalize_num_phone(number): 
    if number[0:2] =='+7':
       return number
    elif number[0:1]=='8' in number:
        temp= number[1:] 
        number= '+7'+temp
        return number
    else:
        number= '+7'+number
        return number    

def chek_valid_num_phone(num):
     if num[0:2] =='+7' and len(num)==12:
        return(True)
     elif num[0:1]=='8' in num and len(num)==11:
        return(True)
     elif len(num)==10 and num[0:2] !='+7':
        return(True)
     else:
        return(False) 
def swap_case(s):
    a=''

    for i in s:
        if i.islower()==True:
            a+=i.upper()
        elif i.isupper()==True:
            a+=i.lower()
        else:
            a+=i
    
    return a

if __name__ == '__main__':

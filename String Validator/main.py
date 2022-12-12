if __name__ == '__main__':
    s = input()
    print(any(c.isalnum() for c in s)) #The any() function returns True if any item in an iterable are true, otherwise it returns False.
    print(any(c.isalpha() for c in s)) #If the iterable object is empty, the any() function will return False
    print(any(c.isdigit() for c in s))
    print(any(c.islower() for c in s))
    print(any(c.isupper() for c in s))

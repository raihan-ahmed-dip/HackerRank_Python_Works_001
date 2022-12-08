if __name__ == '__main__':
    s = input()
    l1 = False 
    l2 = False 
    l3 = False 
    l4 = False 
    l5 = False
    for l in s:
        if l.isalnum():
            l1 = l1 or True
        if l.isalpha():
            l2 = l2 or True
        if l.isnumeric():
            l3 = l3 or True
        if l.islower():
            l4 = l4 or True
        if l.isupper():
            l5 = l5 or True
    print(f"{l1}\n{l2}\n{l3}\n{l4}\n{l5}")
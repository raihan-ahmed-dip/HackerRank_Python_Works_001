def swap_case(s):
    new_string = ""
    for l in s:
        if l.isupper():
            new_string += l.lower()
        else:
            new_string += l.upper()
    return new_string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
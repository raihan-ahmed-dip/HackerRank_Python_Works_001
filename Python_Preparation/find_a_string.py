def count_substring(string, sub_string):
    slen = len(string)
    sublen = len(sub_string)
    slit = list(string)
    c = 0
    for i in range(0, slen-sublen+1):
        if ''.join(slit[i:(i+sublen)]) == sub_string:
            c += 1
    return c

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
def split_and_join(line):
    sl = line.strip().split(' ')
    return '-'.join(sl)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
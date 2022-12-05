if __name__ == '__main__':
    N = int(input())
    lst = []

    for _ in range(N):
        inp = list(input().strip().split())
        cm = inp[0]
        if cm == 'insert':
            lst.insert(int(inp[1]), int(inp[2]))
        elif cm == 'print':
            print(lst)
        elif cm == 'remove':
            lst.remove(int(inp[1]))
        elif cm == 'append':
            lst.append(int(inp[1]))
        elif cm == 'sort':
            lst.sort()
        elif cm == 'pop':
            lst.pop()
        elif cm == 'reverse':
            lst.reverse()
        else:
            pass
    
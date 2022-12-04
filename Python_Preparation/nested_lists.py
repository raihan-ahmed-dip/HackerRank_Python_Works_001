if __name__ == '__main__':
    l = []
    nl = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        l.append([name, score])
        nl.append(score)

    min = min(nl)
    min2 = max(nl)

    for n in nl:
        if n > min and n <= min2:
            min2 = n
    nm = []
    for x in l:
        if x[1] == min2:
            nm.append(x[0])

    nm.sort()
    for n in nm:
        print(n)
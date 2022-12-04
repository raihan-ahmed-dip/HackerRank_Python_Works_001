if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    r = -100
    m = max(arr)
    for i in arr:
        if i < m and i >= r:
            r = i
    print(r)
if __name__ == '__main__':
    n, m = map(int, input().split())
    wc = 'WELCOME'
    ds = '.|.'
    w = len(wc)
    k = len(ds)
    x = 1
    for r in range(int((n+1)/2)-1):
        print('-'*(int((m-(x*k))/2)) + ds*x + '-'*(int((m-(x*k))/2)))
        x += 2
    print('-'*(int((m - w)/2)) + wc + '-'*(int((m - w)/2)))
    x -= 2
    for r in range(int((n+1)/2)-1):
        print('-'*(int((m-(x*k))/2)) + ds*x + '-'*(int((m-(x*k))/2)))
        x -= 2

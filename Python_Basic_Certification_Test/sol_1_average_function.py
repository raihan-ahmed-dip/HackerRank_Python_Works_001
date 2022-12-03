import os

def avg(*l)->float:
    s = 0.0
    for i in l:
        s += float(i)
    ln = len(l)
    a = s/ln
    return a


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    nums = list(map(int, input().split()))
    res = avg(*nums)
    
    fptr.write('%.2f' % res + '\n')

    fptr.close()
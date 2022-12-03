n, m = map(int, input().split())
l = list(map(int, input().split()))
a = set(map(int, input().split()))
b = set(map(int, input().split()))

h = 0

for x in l:
    if x in a:
        h += 1
for y in l:
    if y in b:
        h -= 1

print(h)
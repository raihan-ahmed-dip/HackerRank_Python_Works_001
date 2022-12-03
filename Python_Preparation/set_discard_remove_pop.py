n = int(input())
s = set(map(int, input().split()))
co = int(input())

for c in range(co):
    cm = list(input().split())
    command = cm[0]
    if command == 'pop':
        s.pop()
    if command == 'remove':
        e = int(cm[1])
        s.remove(e)
    if command == 'discard':
        e = int(cm[1])
        s.discard(e)

sm = 0
for j in s:
    sm += j

print(sm)

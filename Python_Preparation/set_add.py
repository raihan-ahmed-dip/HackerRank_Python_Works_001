n = int(input())
c = set()
for _ in range(n):
    cname = input()
    c.add(cname.strip())

print(len(c))
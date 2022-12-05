en = int(input())
ens = set(input().strip().split())

fr = int(input())
frs = set(input().strip().split())

print(len(ens.intersection(frs)))
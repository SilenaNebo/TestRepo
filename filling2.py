n, m = [int(i) for i in input().split()]
for i in range(n):
    for j in range(i+1, n*m +1, n):
        print(str(j).ljust(3), end= ' ')
    print()


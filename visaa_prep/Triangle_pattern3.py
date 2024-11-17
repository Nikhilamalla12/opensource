N=int(input())
for i in range(1, N + 1):
    lft = ''.join(str(x) for x in range(1, i + 1))
    spaces=' '*(2 * (N - i))
    rgt = ''.join(str(x) for x in range(i, 0, -1))
    print(lft+spaces+rgt)

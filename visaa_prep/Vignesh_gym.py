X, Y, Z = map(int,input().strip().split())
if X + Y <= Z:
    print(2)
elif X <= Y:
    print(1)
else:
    print(0)

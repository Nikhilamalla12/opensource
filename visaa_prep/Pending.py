X,Y,Z = map(int, input().strip().split())
time = X * Y
ava_time = Z * 24 * 60
if time<=ava_time:
    print("YES")
else:
    print("NO")

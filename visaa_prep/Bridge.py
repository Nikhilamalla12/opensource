x, y, z = map(int,input().strip().split())
mang_capacity=z-y
if mang_capacity<=0:
    print(0)
else:
    max_mang = mang_capacity // x
    print(max_mang)

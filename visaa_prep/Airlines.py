import math
X,N=map(int,input().split())
A= X*100
if A>=N:
    print(0)
else:
    E=N-A
    planes=math.ceil(E/100)
    print(planes)

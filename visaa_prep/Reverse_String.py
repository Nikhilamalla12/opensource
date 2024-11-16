n=int(input())
arr = list(map(int, input().split()))
reverse=arr[::-1]
print(" ".join(map(str, reverse)))

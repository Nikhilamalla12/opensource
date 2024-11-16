n,m = map(int,input().split())
arr = list(map(int, input().split()))
sum_div = 0
sum_not_div = 0
for num in arr:
    if num % m == 0:
        sum_div += num
    else:
        sum_not_div += num
result = sum_div - sum_not_div
print(result)

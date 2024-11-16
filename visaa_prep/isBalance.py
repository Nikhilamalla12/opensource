n=int(input())
arr = list(map(int, input().split()))
rem_arr=[]
total_sum=sum(arr)
left_weight = 0
for i in range(n):
    right_weight = total_sum - left_weight-arr[i]
    balance = abs(left_weight-right_weight)
    rem_arr.append(balance)
    left_weight += arr[i]
print(" ".join(map(str, rem_arr)))

def binary_search(arr, x):
    l,r = 0, len(arr)-1
    while l <= r:
        mid = (l+r) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid +1
        else:
            r=mid-1
    return -1
n =int(input())
arr = list(map(int, input().split()))
x=int(input())
result = binary_search(arr, x)
print(result)

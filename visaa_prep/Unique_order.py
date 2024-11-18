N=int(input())
arr = list(map(int, input().split()))
seen = set()
unique_elements = []
for num in arr:
    if num not in seen:
        seen.add(num)
        unique_elements.append(num)
print(" ".join(map(str, unique_elements)))

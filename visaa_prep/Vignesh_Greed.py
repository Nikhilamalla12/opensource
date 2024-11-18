def max_triangle(N, sticks):
    sticks.sort(reverse=True)
    for i in range(N - 2):
        a, b, c = sticks[i], sticks[i+1], sticks[i+2]
        if a < b + c:
            return a + b + c
    return -1
N = int(input())
sticks = list(map(int, input().split()))
print(max_triangle(N, sticks))

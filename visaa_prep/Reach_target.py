T=int(input())
results = []
for _ in range(T):
    X, Y = map(int, input().split())
    runs=X-Y+1
    results.append(runs)
for result in results:
    print(result)

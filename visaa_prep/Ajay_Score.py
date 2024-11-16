def main():
    t=int(input())
    results = []
    for _ in range(t):
        X,N = map(int, input().split())
        points = X//10
        score = points*N
        results.append(score)
    for result in results:
        print(result)
        
if __name__=="__main__":
        main()

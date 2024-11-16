def main():
    T=int(input())
    for _ in range(T):
        X,N=map(int,input().split())
        points=X//10
        score=points*N
        print(score)
if __name__=="__main__":
    main()
    

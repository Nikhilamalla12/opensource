def main():
    N=int(input())
    for i in range(1, N+1):
        print(' '.join(str(i) for _ in range(i)))
if __name__=="__main__":
    main()

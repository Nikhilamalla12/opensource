def main():
    N=int(input())
    current = 1
    for i in range(1, N+1):
        row=[]
        for j in range(i):
            row.append(current)
            current+=1
        print(" ".join(map(str, row)))
if __name__=="__main__":
    main()

def main():
    N=input()
    d_sum = sum(int(digit) for digit in N)
    if d_sum%2 == 0:
        print("Vignesh")
    else:
        print("Charan")
if __name__=="__main__":
    main()

N=int(input())
matrix=[]
for _ in range(N):
    matrix.append(list(map(int, input().split())))
mirror_matrix = [row[::-1] for row in matrix]
for row in mirror_matrix:
    print(*row)

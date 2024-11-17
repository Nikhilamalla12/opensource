N=int(input())
matrix = []
for _ in range(N):
    matrix.append(list(map(int,input().split())))
trans_matrix = [[matrix[j][i] for j in range(N)] for i in range(N)]
for row in trans_matrix:
    print(*row)

X=int(input().strip())
dis=0.1*X
dis_nrml = 100
max_dis = max(dis,dis_nrml)
amount = X-max_dis
print(int(amount))

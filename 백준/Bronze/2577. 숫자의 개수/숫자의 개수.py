mul = 1
for _ in range(3):
    mul *= int(input())

dic = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
for i in list(str(mul)):
    dic[int(i)] += 1

print(*list(dic.values()), sep='\n')
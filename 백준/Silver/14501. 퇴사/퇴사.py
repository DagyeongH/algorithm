import sys

# input
N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
money = [0]*(N+1)

for idx in range(len(arr)):
    day = idx+arr[idx][0]
    if day < N+1:
        money[day] = max(money[day], max(money[:idx+1])+arr[idx][1])
        
print(max(money))
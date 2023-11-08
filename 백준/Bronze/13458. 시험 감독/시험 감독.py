import sys
import math

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B, C = map(int, sys.stdin.readline().split())

cnt = N
for val in A:
    val -= B
    if val > 0:
        if val % C > 0:
            cnt += ((val//C)+1)
        else:
            cnt += (val//C)

print(cnt)
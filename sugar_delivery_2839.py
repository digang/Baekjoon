import sys
input = sys.stdin.readline

N = int(input())

a, b = divmod(N,5)
if b == 0 :
    print(a)
    exit()
else:
    for i in range(a + 1):
        k = a - i
        c, d = divmod(N - (k * 5), 3)
        if d == 0:
            print(k + c)
            exit()

print("-1")

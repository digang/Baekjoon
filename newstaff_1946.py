import sys
from operator import itemgetter, attrgetter
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    li = []
    staffNum = int(input())
    for _ in range(staffNum):
        a, b = map(int, input().split())
        li.append([a,b])

    li = sorted(li, key=itemgetter(0))
    min = li[0][1]
    count = int(1)
    for i in range(1, staffNum):
        if li[i][1] < min:
            count += 1
            min = li[i][1]
    print(count)

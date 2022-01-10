import sys
input = sys.stdin.readline

def binary_search(s,e,nl,num):
    while s<=e :
        mid = (s+e) // 2
        if nl[mid] == num:
            return 1
        elif nl[mid] > num:
            e = mid-1
        else:
            s = mid+1
    return 0

T = int(input())
for _ in range(T):
    N = int(input())
    Nlist = list(map(int,input().split()))
    Nlist.sort()
    M = int(input())
    Mlist = list(map(int,input().split()))
    for num in Mlist:
        print(binary_search(0,N-1,Nlist,num))

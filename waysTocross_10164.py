import sys
import math
input = sys.stdin.readline

N,M,K = map(int,input().split())

#li = [[0 for _ in range(M)] for _ in range(N)]
if ( K == 0 ) :
    print( int(math.factorial( N + M - 2) / (math.factorial(N - 1) * math.factorial(M - 1)) ))
else :
    row = (K // M)
    col = K - (M * row) - 1
    preways = int( math.factorial(row + col) / (math.factorial(row) * math.factorial(col)) )
    laterways = int( math.factorial(N - row - 1  + M - col - 1) / (math.factorial( N - row - 1 ) * math.factorial(M - col - 1)) )
    print(preways * laterways)

import sys
from collections import Counter
input = sys.stdin.readline

r, c, k = map(int,input().split())  
arr = [list(map(int,input().split())) for _ in range(3)]
flag = False
time = 0
r -= 1
c -= 1

def checkop(a):
    row = len(a)
    col = len(a[0])
    
    if row >= col:
        return True
    else:
        return False

def sorting(board):
    new_board = []
    max_length = 0
    for row in board:
        new_row = []
        result = Counter(row)
        if result.get(0):
            del result[0]
        t = list(zip(result.keys(), result.values()))
        t.sort(key = lambda x : (x[1],x[0]))
        for x in t:
            new_row.append(x[0])
            new_row.append(x[1])
        new_row = new_row[:100]
        new_board.append(new_row)
        max_length = max(max_length, len(new_row))
    
    for row in new_board:
        while len(row) < max_length:
            row.append(0)
            
    return new_board

while True:
    
    if r < len(arr) and c < len(arr[0]) and arr[r][c] == k : 
        print(time)
        break
    
    if time > 100:
        print("-1")
        break
    
    if checkop(arr):
        # row >= col
        arr = sorting(arr)
        
    
    else:
        arr = [list(x) for x in zip(*arr)]
        arr = sorting(arr)
        arr = [list(x) for x in zip(*arr)]
        # col > row
    
    time += 1

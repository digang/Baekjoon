import sys

input = sys.stdin.readline

dy = [-1,-1,-1,0,1,1,1,0]
dx = [-1,0,1,1,1,0,-1,-1]

N, M, K = map(int, input().split())
real_board = [list(map(int, input().split())) for _ in range(N)]
board = [ [5] * N for _ in range(N)]
tree_board = [ [ [] for _ in range(N) ] for _ in range(N)]

tree_count = 0

for _ in range(M):
    x, y, z = map(int,input().split())
    tree_board[x-1][y-1].append(z)
    tree_count += 1
    
for year in range(K):
    #spring
    for i in range(N):
        for j in range(N):
            if tree_board[i][j]:
                tree_board[i][j].sort()
                temp_tree, dead_tree = [], 0
                for age in tree_board[i][j]:
                    if age <= board[i][j]:
                        board[i][j] -= age
                        age += 1
                        temp_tree.append(age)
                    else :
                        tree_count -= 1
                        dead_tree += age // 2
                board[i][j] += dead_tree
                tree_board[i][j] = []
                tree_board[i][j].extend(temp_tree)
    #summer but did in spring
    
    #fall
    for i in range(N):
        for j in range(N):
            if tree_board[i][j]:
                for age in tree_board[i][j]:
                    if age % 5 == 0:
                        for k in range(8):
                            nx = i + dy[k]
                            ny = j + dx[k]
                            if 0<= nx < N and 0 <= ny < N:
                                tree_count += 1
                                tree_board[nx][ny].append(1)
    
    #winter
    for i in range(N):
        for j in range(N):
            board[i][j] += real_board[i][j]
            
print(tree_count)
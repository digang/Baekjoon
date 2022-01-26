import sys

n, l = map(int, sys.stdin.readline().rsplit())
arr = [list(map(int, sys.stdin.readline().rsplit())) for _ in range(n)]
answer = 0

def solve(y, x, val, cnt):
    #끝에 다다른 경우
    if x == n: return True

    #평지인경우 
    if arr[y][x] == val: cnt += 1

    #높이차이가 2이상인 경우
    elif abs(arr[y][x]-val) > 1: return False

    #높이가 높아진 경우
    elif val < arr[y][x]:
        # L 보다 도로의 길이가 짧다면
        if cnt < l: return False

        # 아니라면 카운트 초기화 하고 다시 진행
        val = arr[y][x]
        cnt = 1
    
    #높이가 낮아진 경우
    elif val > arr[y][x]:
        k = 0
        cnt = 0
        for k in range(x, n):
            #평지의 개수 세주기.
            if arr[y][k] == arr[y][x]: cnt += 1

            #평지가 없다면 break
            else: break

            #경사로의 길이와 도로의 길이가 같아도 break (경사로를 깔아야하니까)
            if cnt == l: break

        #시작점 갱신
        val = arr[y][x]
        if cnt < l: return False
        x = k
        cnt = 0
    
    return solve(y, x+1, val, cnt)

for i in range(n):
    if solve(i, 1, arr[i][0], 1): answer += 1
    
arr = [[arr[j][i] for j in range(n)] for i in range(n)]
for i in range(n):
    if solve(i, 1, arr[i][0], 1): answer += 1

print(answer)
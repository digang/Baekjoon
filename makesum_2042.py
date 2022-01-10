import sys
sys.stdin.readline

def init(tree, arr, node, start, end):
    if start == end :
        tree[node] = arr[start]
        return tree[node]

    mid = (start + end) // 2

    tree[node] = init(tree,arr, node * 2, start, mid) + init(tree,arr,node * 2 + 1, mid +1, end)

    return tree[node]

def update(tree,arr, node, start, end, index, diff):

    if(not(start <= index and index <= end)):
        return

    tree[node] += diff

    if start == end:
        return

    if(start != end):
        mid = (start + end) // 2
        update(tree,arr,node * 2, start, mid, index, diff)
        update(tree,arr,node * 2 + 1, mid + 1, end, index, diff)

def sum(tree, node, start, end, left, right):
    if left > end or right < start:
        return 0

    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2
    return sum(tree, node * 2, start, mid, left, right) + sum(tree, node * 2 + 1, mid + 1, end, left, right)

N, M, K = map(int, input().split())
arr = [0]
tree = [0 for _ in range(N * 4)]
for _ in range(N):
    arr.append(int(input().rstrip()))

init(tree, arr, 1, 1, N)


for _ in range(M + K):
    a, b, c = map(int,input().split())
    if a == 1:
        diff = c - arr[b]
        arr[b] = c
        update(tree, arr,1, 1, N, b, diff)
    elif a == 2:
        print(sum(tree, 1, 1, N, b, c))


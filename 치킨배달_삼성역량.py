from dis import dis
import sys
import math
from itertools import combinations
from xml.dom import minidom
input = sys.stdin.readline

n, m = map(int, input().split())    

world = [ list(map(int, input().split())) for _ in range(n)]
chicken = []

chicken_count = 0
for i in range(n):
    for j in range(n):
        if world[i][j] == 2:
            chicken.append([chicken_count,i,j])
            chicken_count += 1

def getMindistance(y,x):
    distance = []
    for i in range(n):
        for j in range(n):
            if world[i][j] == 1:
                distance.append(abs(i-y) + abs(j-x))
    
    return distance

min_distance = []
for item in chicken:
    y = item[1] 
    x = item[2]
    distance = getMindistance(y,x)
    min_distance.append(distance)

comb = list(combinations(min_distance,m))
result = 9999999

for item in comb:
    result_sum = 0
    for i in range(len(item[0])):
        sum = 100000
        for j in range(len(item)):
            sum = min(sum, item[j][i])
        result_sum += sum
    
    result = min(result_sum, result)

print(result)
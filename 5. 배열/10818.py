# 첫째 줄에 주어진 정수 N개의 최솟값과 최댓값을 공백으로 구분해 출력한다.

T = int(input())

num = list(map(int,input().split()))
max = num[0]
min = num[0]

for i in num:
    if i > max:
        max = i
    elif i < min:
        min = i
print(min, max, end='')
# print(min(num), max(num))
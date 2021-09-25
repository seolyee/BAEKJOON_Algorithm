# 첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.

N = int(input())

for i in range(1, N+1):
    print(' ' * (N-i) + '*' * i)
    
# X보다 작은 수를 입력받은 순서대로 공백으로 구분해 출력한다. 
# X보다 작은 수는 적어도 하나 존재한다.

N, X = map(int, input().split())
num = list(map(int, input().split()))

for i in range(N):
    if num[i] < X:
        print(num[i], end = " ")


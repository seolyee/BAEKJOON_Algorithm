# 1부터 n까지 합을 출력한다.

N = int(input())
total = 0

for i in range(1, N+1): # 1 ~ N-1
    total += i
print(total)

# sum 함수 사용
# print(sum(range(1, N+1)))
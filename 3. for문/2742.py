# 첫째 줄부터 N번째 줄 까지 차례대로 출력한다.
N = int(input())

for i in range(N, 0 , -1): # N부터 1까지 역순
    print(i)

# 1 ~ N -> 1 ~ N-1
# N ~ 1 -> N ~ 1-1

# for i in range(1, n+1)[::-1]:
#     print(i)

# comprehension 코드
# [print(i) for i in range(1, int(input())+1)[::-1]]
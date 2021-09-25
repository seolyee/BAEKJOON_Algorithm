# 각 테스트 케이스마다 A+B를 출력한다.

T = int(input()) # 테스트 케이스 개수 T

for i in range(T): # T만큼 반복
    A, B = map(int, input().split())
    print(A+B)
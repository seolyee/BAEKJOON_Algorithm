# 각 테스트 케이스마다 "Case #x: "를 출력한 다음, A+B를 출력한다. 
# 테스트 케이스 번호는 1부터 시작한다.
T = int(input())

for i in range(1, T+1):  # 1부터 T까지
    A, B = map(int, input().split())
    print(f'Case #{i}: {A+B}')
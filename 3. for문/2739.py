# 출력형식과 같게 N*1부터 N*9까지 출력한다.

N = int(input()) # 단 입력

for i in range(1, 10) : # 1 ~ 9
    print(N, '*', i, '=', N*i)

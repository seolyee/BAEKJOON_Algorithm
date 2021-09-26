# 각 테스트 케이스마다 A+B를 출력한다.
# 입력의 마지막에는 0 두 개가 들어온다.

while 1:
    A, B = map(int, input().split())
    if (A==0 and B==0):
        break
    else:
        print(A+B)
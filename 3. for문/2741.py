# 첫째 줄부터 N번째 줄 까지 차례대로 출력한다.
N = int(input())

for i in range(1, N+1):
    print(i)

# comprehension 표현식
#[출력 표현식 for interable 자료 요소 in iterable 자료형]
# [print(i) for i in range(1, int(input())+1)]
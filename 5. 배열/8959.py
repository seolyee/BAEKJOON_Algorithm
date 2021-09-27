# 첫째 줄에 테스트 케이스의 개수가 주어진다. 
# 각 테스트 케이스는 한 줄로 이루어져 있고, 길이가 0보다 크고 80보다 작은 문자열이 주어진다. 
# 문자열은 O와 X만으로 이루어져 있다.
# 예를 들어, 10번 문제의 점수는 3이 된다.
# "OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다.
# 각 테스트 케이스마다 점수를 출력한다.

T = int(input())

for i in range(T):
    ox_list = list(input())
    score = 0
    sum_score = 0

    for ox in ox_list: # 새로운 ox리스트를 입력 받으면 점수 합계를 리셋한다.
        if ox == 'O':
            score += 1 # 'O'가 연속되면 점수가 1점씩 커진다.
            sum_score += score # sum_score = sum_score + score
        else:
            score = 0
    print(sum_score)
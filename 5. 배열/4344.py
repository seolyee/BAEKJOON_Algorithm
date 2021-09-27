# 첫째 줄에는 테스트 케이스의 개수 C가 주어진다. 
# 둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고, 
# 이어서 N명의 점수가 주어진다. 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.
# 각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력한다.
# 예시 5 50 50 70 80 100

T = int(input())

for i in range(T):
    num_list = list(map(int, input().split()))

    avg = sum(num_list[1:]) / num_list[0]  # 평균을 구함 (num_list[0]: 학생 수, num_list[1:] 점수)
    cnt = 0

    for score in num_list[1:]:
        if score > avg:
            cnt += 1  # 평균 이상인 학생 수
    rate = cnt/num_list[0] *100
    print(f'{rate:.3f}%')
        



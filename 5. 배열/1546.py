# 첫째 줄에 시험 본 과목의 개수 N이 주어진다. 
# 이 값은 1000보다 작거나 같다. 둘째 줄에 세준이의 현재 성적이 주어진다. 
# 이 값은 100보다 작거나 같은 음이 아닌 정수이고, 적어도 하나의 값은 0보다 크다.
# 첫째 줄에 새로운 평균을 출력한다. 실제 정답과 출력값의 절대오차 또는 상대오차가 10-2 이하이면 정답이다.
# 예를 들어, 세준이의 최고점이 70이고, 수학점수가 50이었으면 수학점수는 50/70*100이 되어 71.43점이 된다.

T = int(input())
num_list = list(map(int,input().split()))

max_score = max(num_list)
sum = 0

for i in range(T):
    num_list[i] = num_list[i]/max_score *100
    sum += num_list[i]
print(sum/T)

# 어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다. 
# 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. 
# N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오. 

num = int(input())
hansu = 0

for i in range(1, num+1):
    if i < 100:
        hansu += 1 # 100보다 작으면 모두 한수
    else:
        num_str = list(map(int, str(i)))
        if num_str[2] - num_str[1] == num_str[1] - num_str[0]:
            hansu += 1 # x의 각 자리가 등차수열이면 한수

print(hansu)
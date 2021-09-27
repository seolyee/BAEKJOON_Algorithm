# 첫째 줄부터 아홉 번째 줄까지 한 줄에 하나의 자연수가 주어진다. 주어지는 자연수는 100 보다 작다.
# 첫째 줄에 최댓값을 출력하고, 둘째 줄에 최댓값이 몇 번째 수인지를 출력한다.

index = 0
num_list = []

for i in range(9):
    num = int(input())
    num_list.append(num)

print(max(num_list))
print(num_list.index(max(num_list))+1)
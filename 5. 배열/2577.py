# 첫째 줄에는 A × B × C의 결과에 0 이 몇 번 쓰였는지 출력한다. 
# 마찬가지로 둘째 줄부터 열 번째 줄까지 A × B × C의 결과에 
# 1부터 9까지의 숫자가 각각 몇 번 쓰였는지 차례로 한 줄에 하나씩 출력한다.

A = int(input())
B = int(input())
C = int(input())

temp = str(A*B*C) # 17,037,300

for i in range(10):
    num = str(i)
    print(temp.count(num))
# 26부터 시작한다. 2+6 = 8이다. 새로운 수는 68이다. 
# 6+8 = 14이다. 새로운 수는 84이다. 
# 8+4 = 12이다. 새로운 수는 42이다. 
# 4+2 = 6이다. 새로운 수는 26이다.
# 위의 예는 4번만에 원래 수로 돌아올 수 있다. 따라서 26의 사이클의 길이는 4이다.
# N이 주어졌을 때, N의 사이클의 길이를 구하는 프로그램을 작성하시오.

num = int(input()) # 68
tmp = num
cnt = 0

while True:
    a = num // 10 # 6
    b = num % 10 # 8
    c = (a + b) % 10 # (6 + 8) % 10 = 1"4"
    num = (b * 10) + c # 80 + 4 = 84

    cnt = cnt + 1 # 사이클 수 + 1
    if(tmp == num): # tmp에 입력된 num과 똑같은 숫자가 나오면 break
        break

print(cnt)
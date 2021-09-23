# 사분면 고르기
X= int(input())
Y= int(input())

if (X > 0) and (Y > 0):
    print("1") # X, Y 양수
elif (X < 0) and (Y > 0):
    print("2") # X 음수, Y 양수
elif (X < 0) and (Y < 0):
    print("3") # X, Y 음수
else:
    print("4") # X 양수, Y 음수
    
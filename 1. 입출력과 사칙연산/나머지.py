A, B, C = map(int , input().split()) 
print((A+B)%C, ((A%C) + (B%C))%C, (A*B)%C, ((A%C) * (B%C))%C, sep='\n')
# 첫째 줄에 (A+B)%C, 
# 둘째 줄에 ((A%C) + (B%C))%C, 
# 셋째 줄에 (A×B)%C, 
# 넷째 줄에 ((A%C) × (B%C))%C를 출력한다.
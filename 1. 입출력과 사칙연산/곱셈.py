A, B = map(int, input().split())

out1 = A*((B%100)%10) # 2360
out2 = A*((B%100)//10) # 3776
out3 = A*(B//100)  # 1416
result = A*B # 181720

print(out1, out2, out3, result, sep='\n')

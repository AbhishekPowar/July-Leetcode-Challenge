n = 67

binary32 = f'{n:032b}'
revN = int(binary32[::-1], 2)
print(revN)

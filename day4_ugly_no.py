N = 7
n2 = 0
n3 = 0
n5 = 0

ugly = [1]
while len(ugly) < N:
    small = min(
        ugly[n2]*2,
        ugly[n3]*3,
        ugly[n5]*5
    )
    if small not in ugly:
        ugly.append(small)
    if small == ugly[n2]*2:
        n2 += 1
    elif small == ugly[n3]*3:
        n3 += 1
    else:
        n5 += 1
ans = ugly[-1]


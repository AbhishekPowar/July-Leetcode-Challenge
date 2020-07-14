arr = [9, 9]
idx = len(arr)-1
carry = 1
summ = 0
while idx >= 0:
    summ = arr[idx]+carry
    if summ < 10:
        arr[idx] += 1
        break
    else:
        arr[idx] = 0
        carry = 1
        idx -= 1
if idx == -1:
    arr.insert(0, 1)
print(arr)

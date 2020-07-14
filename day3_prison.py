cells = [0, 1, 0, 1, 1, 0, 0, 1]
N = 7
c_len = 8


d = {}
rep = 14
for n in range(15):
    last = cells[:]
    cells[0], cells[c_len-1] = 0, 0
    for i in range(1, c_len-1):
        cells[i] = int(last[i-1] == last[i+1])
    d[n] = tuple(cells)
ans = d[N-1 % 14]
print(ans)


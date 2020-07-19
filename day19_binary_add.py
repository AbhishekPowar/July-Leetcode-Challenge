def addBinary(a: str, b: str) -> str:
    # return bin(int(a,2)+int(b,2))[2:]
    def cmd(a, b, c):
        if c == '0':
            if a == b:
                if a == '0':
                    return '0', '0'
                else:
                    return '1', '0'
            else:
                return '0', '1'
        else:
            if a == b:
                if a == '0':
                    return '0', '1'
                else:
                    return '1', '1'
            else:
                return '1', '0'

    s1 = a
    s2 = b
    s1_len = len(s1)
    s2_len = len(s2)
    maxx = max(s1_len, s2_len)
    s1 = s1.zfill(maxx)
    s2 = s2.zfill(maxx)

    s1 = list(reversed(s1))
    s2 = list(reversed(s2))
    s3 = []
    c = '0'
    for i in range(maxx):
        a = s1[i]
        b = s2[i]
        c, x = cmd(a, b, c)
        print(x)
        s3.append(x)
    if c == '1':
        s3.append(c)
    return ''.join(s3[::-1])

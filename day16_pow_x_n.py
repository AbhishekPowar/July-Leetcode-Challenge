class Solution:
    def myPow(self, x: float, n: int) -> float:
        def pow(x, n):
            if n == 1:
                return x
            elif n % 2 == 0:
                nby2 = pow(x, n//2)
                return nby2*nby2
            else:
                nby2 = pow(x, n//2)
                return nby2*nby2*x
        if n > 0:
            return pow(x, n)
        elif n == 0:
            return 1
        else:
            return 1/pow(x, -n)

class Solution:
    def addDigits(self, num: int) -> int:
        # Human brain like solution
        # summ = sum(map(int,list(str(num))))
        # return summ if summ<10 else self.addDigits(summ)

        # recursive solution
        summ = 0
        while num:
            summ += num % 10
            num = num//10
        return summ if summ < 10 else self.addDigits(summ)

        # Iterative solution
        while num >= 10:
            summ = 0
            while num:
                summ += num % 10
                num //= 10
            num = summ
        return num

        if num:
            return 9 if num % 9 == 0 else num % 9
        else:
            return 0

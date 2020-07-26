class Solution:
    def addDigits(self, num: int) -> int:
        # Human brain like solution
        # summ = sum(map(int,list(str(num))))
        # return summ if summ<10 else self.addDigits(summ)

        # efficient soln
        summ = 0
        while num:
            summ += num % 10
            num = num//10
        return summ if summ < 10 else self.addDigits(summ)

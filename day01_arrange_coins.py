def arrangeCoins(self, n: int) -> int:
        N=n
        # cur=0
        # for i in range(N+2):
        #     cur+=i
        #     if cur>N:
        #         # print(i-1)
        #         # break
        #         return i-1
        return  int((2*N + 0.25)**0.5 - 0.5)

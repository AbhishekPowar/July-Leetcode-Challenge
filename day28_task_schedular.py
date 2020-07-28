# class Solution:
#     def leastInterval(self, tasks: List[str], n: int) -> int:
#         self.cool = [0]*n
#         self.coolset = set(self.cool)
#         def calc(tasks):
#             if len(tasks)>0:
#                 taskfound=0
#                 for i in tasks:
#                     if i not in self.coolset:
#                         taskfound=1
#                         break
#                 self.cool = self.cool[1:]+[0]
#                 if taskfound:
#                     tasks.remove(i)
#                     self.cool[n-1] = i
#                 self.coolset = set(self.cool)
#                 return 1+calc(tasks)
#             else:
#                 return 0
#         return calc(tasks)

#                  #############################################
#                  # Disclaimer I couldn't solve it on my own  #
#                  # Watched solution                          #
#                  #############################################


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if not tasks:
            return 0
        from collections import Counter
        hmap = Counter(tasks)  # Counting frequncy
        # maxOcc or maxfrequency of a elemnt
        maxOcc = hmap.most_common(1)[0][1]
        # howmany with frequency ==maxOcc
        howmany = sum((hmap[i] == maxOcc for i in hmap))
        # len(tasks) optimal condition
        return max(len(tasks),  (maxOcc-1)*(n+1) + howmany)


# 1
# How to under stand
# say tasks = [8,8,8]  and n = 2
# 8 _ _
# 8 _ _
# 8


# 2
# say tasks = [8,8,8]  and n = 3

#   (n+1)
# ___|___
# |      |
#             _
# 8 7 _ _      |_ (maxOcc-1)
# 8 7 _ _     _|
# 8 7
# |__|
#   |
#  (howmany)


# 3
# len(tasks)
# [9,8,8,8,8,7,7,7,6,5,4,3,2,1] n=2

# 1
# 4 3 2
# 8 7 9
# 8 7 6
# 8 7 5
# 8
# here (maxOcc-1)*(n+1) + howmany < len
# so it will take time = len

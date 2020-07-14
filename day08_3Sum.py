def threeSum(nums):
    arr = nums
    target = 0
    hashMap = {}

    for i in arr:
        if hashMap.get(i,0) <2 :
            hashMap[i] = hashMap.get(i,0)+1
        elif i==0 and hashMap.get(0,0) == 2:
            hashMap[0]+=1

    newArr = []
    for k in hashMap:
        newArr.extend([k]*hashMap[k])

    print(newArr)

    hmap = defaultdict(list)
    n = len(newArr)
    res =set()
    for i in range(n):
        hmap[newArr[i]].append(i)


    for i in range(n):
        for j in range(i+1,n):
            csum = newArr[i]+newArr[j]
            if -csum in hmap:
                for k in hmap[-csum]:
                    if k not in [i,j]:
                        val = [newArr[i],newArr[j],newArr[k]]
                        res.add(tuple(sorted(val)))
    ans =[list(i) for i in res]
    return ans
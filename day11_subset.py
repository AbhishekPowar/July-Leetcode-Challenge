sub = set()
def div(arr, l, h, temp=[]):
    sub.add(tuple(temp))
    if l < h:
        div(arr, l+1, h, temp)
        temp = temp+[arr[l]]
        div(arr, l+1, h, temp)
div(nums, 0, len(nums))
sub = sorted(sub, key=lambda x: (len(x), x))
return sub
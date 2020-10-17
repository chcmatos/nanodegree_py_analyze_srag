def interval_extract(list):
    length = len(list)
    i = 0
    while (i < length):
        low = list[i]
        while i < length-1 and list[i]+1 == list[i + 1]:
            i += 1
        high = list[i]
        if (high - low >= 1):
            yield [low, high]
        elif (high - low == 1):
            yield [low, ]
            yield [high, ]
        else:
            yield [low, ]
        i += 1

def __fill_interval_range__(target):
    targetlen = len(target)
    i = 0
    arr = []
    while(i < targetlen):        
        e = target[i]
        if (len(arr) == 0 or abs(e - arr[-1]) <= 1):
            arr.append(e)
        else:
            item = arr[-1] + 1
            ran = list(range(item, e, int(abs(e / item))))
            arr.extend(ran)
            arr.append(e)
        i += 1
    return arr

def __interval_extract__(target):
    new_list = target.copy()
    new_list.sort()
    l = len(new_list)
    i = 0
    arr = []
    while((i + 1) < l):
        arr.append(new_list[i + 1] - new_list[i])
        i+=1
    print(arr)
    return sum(arr) / len(arr)


# Driver code
l=[8496, 17134, 1083, 117648, 1917]
print(__interval_extract__(l))

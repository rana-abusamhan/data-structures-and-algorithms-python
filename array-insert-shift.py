def insertShiftArray(arr,value):
    length = len(arr)
    if length % 2 == 0:
        idx = length // 2
        newArr = arr[:idx] + [value] + arr[idx:]
        return newArr
    else:
        idx = ((length + 1) // 2)
        newArr = arr[:idx] + [value] + arr[idx:]
        return newArr


arr = [1,2,4]
print(insertShiftArray(arr,3))

arr = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]];
arr.sort(key = lambda x:x[1])
arr = list(filter(lambda x:x[1]!=arr[0][1], arr))
arr.sort(key = lambda x:x[1])
arr = list(filter(lambda x:x[1]==arr[0][1], arr))
for i in range(len(arr)):
    print(arr[i][0])
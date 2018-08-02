#n = int(input())
arr = [2,3,4,5]
m = max(arr)
print(max(list(filter(lambda a:a != max(arr), arr))))
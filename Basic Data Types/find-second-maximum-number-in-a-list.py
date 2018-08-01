#n = int(input())
arr = [2,3,5,5]
m = max(arr)
print(max(list(filter(lambda a:a != max(arr), arr))))
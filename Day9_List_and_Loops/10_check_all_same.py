arr = [2, 2, 2, 2]
flag = True

for i in arr:
    if i != arr[0]:
        flag = False
        break

if flag:
    print("All elements are same")
else:
    print("Not same")
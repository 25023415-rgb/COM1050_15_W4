a, b = map(int, input().split())
if a >= 0 and b >= 0:
    y = b/2 - a
    x = a - y
    if x >= 0 and y >= 0 and x / int(x) == 1 and y / int(y) == 1:
        print(x, y)
    else:
        print("Invalid")
else:
    print("Invalid")
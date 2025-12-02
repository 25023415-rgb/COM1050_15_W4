while True:
    try:
        n = int(input())
        if n > 0:
            break
        else:
            print("Vui lòng nhập một số nguyên dương")
    except ValueError:
        print("Vui lòng nhập một số nguyên dương")

timthay42 = False
for i in range(1, n + 1):
    so = int(input())
    if so == 42:
        timthay42 = True

if timthay42 == True:
    print("I have found the meaning of life!")
else:
    print("It's a joke!")

num = 1
increment = 2
while num <= 7:
    count = num
    while count > 0:
        print(num, end="")
        count -= 1
    if num == 5:
        increment = 1
    num += increment
    print()

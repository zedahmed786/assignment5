for i in range(1, 6):
    for j in range(1, i):
        print('* ', end='')
    print()
i = 5
while i >= 1:
    for j in range(i):
        print('* ', end='')
    print()
    i -= 1
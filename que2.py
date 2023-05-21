num = int(input('Enter range: '))
div = int(input('Enter divisor'))
for i in range(num):
    if i % div == 0:
        print(i)
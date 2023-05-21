list = []
bool = []
for i in range(10):
    list.append(int(input()))
    bool.append(False)
print('Positive numbers:')
for i in list:
    if(i > 0):
        print(i)
print('Negative numbers:')
for i in list:
    if(i < 0):
        print(i)
print('Odd numbers:')
for i in list:
    if(i % 2 == 1):
        print(i)
print('Even numbers:')
for i in list:
    if(i % 2 == 0):
        print(i)
print('Occurences')
for i in range(len(list)):
    c = 0
    if not bool[i]:
        for j in range(i, len(list)):
            if list[j] == list[i]:
                c += 1
                bool[j] = True
        print(list[i], ' occurs', c, ' times')
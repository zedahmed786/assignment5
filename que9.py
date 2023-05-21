size = int(input('Enter size of list: '))
list = []
bool = []
for i in range(size):
    list.append(input())
    bool.append(False)
for i in range(len(list)):
    c = 0
    if not bool[i]:
        for j in range(i, len(list)):
            if list[j] == list[i]:
                c += 1
                bool[j] = True
        print(list[i], ' occurs', c, ' times')
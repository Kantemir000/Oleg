print('Введите значение: ', end ='')
n = int(input())
r = 0
for i in range(1, n + 1):
    r += 1
    print (' ' * (n - r), end = '')
    for k in range(1, i):
        print(k, end='')
    for k in range(i, 0, -1):
        print(k, end='')
    print('')
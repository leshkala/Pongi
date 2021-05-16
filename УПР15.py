import sys
def moon_weight():
    print('Введите ваш вес')
    weight =int(sys.stdin.readline())
    print('Введите прирост вашего веса')
    i =int(sys.stdin.readline())
    print('Введите количество лет')
    age =int(sys.stdin.readline())
    moon = weight * 0.165
    for z in range(0, age):
       print(moon)
       moon=moon+i
moon_weight()
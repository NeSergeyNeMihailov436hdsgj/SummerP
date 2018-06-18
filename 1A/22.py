import datetime
import math

def printTimeStamp(name):
    print('Автори програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
r = int(input("Введите радиус: "))
print("Площа круга с указанным радиусом: ", math.pi * math.pow(r, 2), "\nОбъем шара с указанным радиусом: ", 4/3 * (math.pi * math.pow(r, 3)))
printTimeStamp("Давлат Чорновол,Сергій Михайлов")
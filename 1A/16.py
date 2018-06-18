import datetime
def printTimeStamp(name):
    print('Автори програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
pole = list(map(int,input("Укажите ширину и длинну поля в метрах через пробел: ").split()))
print((pole[0] * pole[1]) / 10000, "гектаров\n",(pole[0] * pole[1]) / 100, "аров")
printTimeStamp("Давлат Чорновол,Сергій Михайлов")

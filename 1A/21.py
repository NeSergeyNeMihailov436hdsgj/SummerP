import datetime
def printTimeStamp(name):
    print('Автори програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
a = int(input("Введите целое число: "))
print("Сумма всех числел: ", (a * (a + 1)) / 2)
printTimeStamp("Давлат Чорновол,Сергій Михайлов")

import datetime
import time

def printTimeStamp(name):
    print('Автори програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

print("%s"%time.asctime())
printTimeStamp("Давлат Чорновол,Сергій Михайлов")
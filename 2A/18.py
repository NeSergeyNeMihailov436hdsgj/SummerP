import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
tuple1 = [('A', 1), ('B', 2), ('C', 3)]
print(tuple1)
dict1 = dict([('A', 1), ('B', 2), ('C', 3)])
print(dict1)
printTimeStamp('Михайлов Сергій')

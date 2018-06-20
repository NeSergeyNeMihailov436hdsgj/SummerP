import datetime


def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

inp=(input("Numbers:").split(" "))
a=(inp)
midle=(int(a[0])+int(a[1])+int(a[2])-int(min(a))-int(max(a)))
print(min(a),str(midle),max(a))
print("Сергій Михайлов")
import datetime
def printTimeStamp(name):
    print('Автор программы: ' + name)
    print('Время компиляции: ' + str(datetime.datetime.now()))
numbers = list (map(int,input("Введите 3 целых числа через пробел: ").split()))
numbers = sorted(numbers)
print("Значение между максимумом и минимумом: ",(numbers[0] + numbers[1] + numbers[2]) - min(numbers) - max(numbers))
printTimeStamp("Сергій Михайлов")

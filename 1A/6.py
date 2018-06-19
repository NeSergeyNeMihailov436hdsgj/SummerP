import datetime


def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

cost_of_food=int(input("Price of order:"))
print("Tip - ","%.2f"%(cost_of_food*float(0.14)),"$","\nTax - ","%.2f"%(cost_of_food*float(0.18)),"$","\nTotal amount - ","%.2f"%(cost_of_food+(cost_of_food*float(0.18))+(cost_of_food*float(0.14))),"$")
printTimeStamp("Сергій Михайлов ")

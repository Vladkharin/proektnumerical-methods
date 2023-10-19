import math
# args = input('Введите числа')
args = 2.65
# argsStart = [2.65, 2.66, 2.67, 2.68, 2.69, 2.70, 2.71, 2.72]
# argsEnd = input('Введите конечное число ')
argsEnd = 2.72

numberEnd = int(( argsEnd - args) * 100 + 1)
# print(numberEnd)

# step = input('Введите шаг')
step = 0.005
step2 = 0.01

# interval1 = input('Введите интервал уплотнения Первое число ')
interval1 = 2.66
# interval2 = input('Введите интервал уплотнения Второе число ')
interval2 = 2.68

array = []
arrayModificated = []
valueArray = []

# array.append(argsStart)
for i in range (0, numberEnd):
    arg = round(float(args) + i * step2, 2)
    array.append(arg)


valueArray = [-3.2456, -2.8943, -1.4849, 0.2525, 12.4348, 14.3437, 5.8284, 2.3437]
# for i in range (0, len(array)):
#     value = float(input(f'Введите значение x который равен {array[i]}, значене f(x) будет равно: '))
#     valueArray.append(value)

startInteval = array.index(interval1)
endInterval = array.index(interval2)

arrayModificated = array[:]

for i in range(startInteval, endInterval):
    value = array[i] + step
    arrayModificated.insert(i + 1, value)
    
arrayModificated.sort()

objectImaginaryUnit = {}
for i in range(0, len(array)):
    objectItem = {
        'xi': array[i],
        'yi': valueArray[i]
    }

    # print(i)
    for x in range(0, len(array) - i):
        objectItem[f'deltay{x}'] = 0;
    
    objectImaginaryUnit[i] = objectItem


# print(objectImaginaryUnit)

for i in range(0, len(objectImaginaryUnit) - 1):
    if (objectImaginaryUnit.get(i, False)):
        objectImaginaryUnit[i][f'deltay0'] = round(objectImaginaryUnit[i]['yi'] - objectImaginaryUnit[i + 1]['yi'], 4)
    else :
        objectImaginaryUnit[i][f'deltay0'] = 0

for x in range(1, len(objectImaginaryUnit)):
    for i in range(0, len(objectImaginaryUnit) - x):
        if (objectImaginaryUnit.get(i, False)):
            objectImaginaryUnit[i][f'deltay{x}'] = round(objectImaginaryUnit[i][f'deltay{x-1}'] - objectImaginaryUnit[i + 1][f'deltay{x-1}'], 4)
        else :
            objectImaginaryUnit[i][f'deltay{x}'] = 0

startIntevalMod = arrayModificated.index(interval1)
endIntervalMod = arrayModificated.index(interval2)
objectQ = {}

for i in range(startIntevalMod + 1, endIntervalMod):
    if (i % 2 != 0):
        continue
    # print(i)
    if (endInterval < len(objectImaginaryUnit)/ 2):
        objectQ[f"q{i-1}"] = round((arrayModificated[i] - array[0])/step, 4)
    else:
        objectQ[f"q{i-1}"] = round((arrayModificated[i] - array[len(array) - 1])/step, 4)

objectPrimer = {}   
    # result 
for x in range(0, len(objectQ)):
    print(x)
    if (x == 1):
        x = x + 1
    q = objectQ[f'q{x + 1}']
    primer = 0
    resultQ = q;
    # print(q)
    for i in range (0, len(array)):
        if (i == 0):
            primer = round(primer + objectImaginaryUnit[i][f'deltay0'], 4)
            continue
        if (i == 1):
            primer  = round(resultQ + primer + objectImaginaryUnit[i][f'deltay0'], 4)
            continue
        
        resultQ = resultQ * (q - 1)
        primer  = round((resultQ + primer + objectImaginaryUnit[i][f'deltay0'])/math.factorial(i) , 4)


        # print(resultQ)
    objectPrimer[f'primer{x + 1}-q{x + 1}'] = primer

# print(objectQ)
# print(objectPrimer)
# print(objectImaginaryUnit)
valueArrayMod = valueArray[:]

for i in range(startInteval, endInterval + 1):
    # print(i)
    if (i % 2 == 0):
        continue
    # print(i)
    value = objectPrimer[f'primer{i}-q{i}']
    valueArrayMod.insert(i + 1, value)

# print(valueArray)
# print(array)
# print(valueArrayMod)
# print(arrayModificated)
# print(argsStart)
# print(argsEnd)

# [-3.2456, -2.8943, -1.4849, 0.2525, 12.4348, 14.3437, 5.8284, 2.3437]
# [2.65, 2.66, 2.67, 2.68, 2.69, 2.7, 2.71, 2.72]
# [-3.2456, -2.8943, 0.0381, -1.4849, 4.0649, 0.2525, 12.4348, 14.3437, 5.8284, 2.3437]
# [2.65, 2.66, 2.665, 2.67, 2.675, 2.68, 2.69, 2.7, 2.71, 2.72]
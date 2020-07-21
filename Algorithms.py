import time
#Linear Sort
def linear_sort(data,drawData,timeTick):
    for j in range(len(data)):
        minIndx = j
        for i in range(j+1,len(data)):
            if data[i] < data[minIndx]:
                minIndx = i
                drawData(data, ['green' if x == j or x == i else 'red' for x in range(len(data))])
                time.sleep(timeTick)
        data[j],data[minIndx] = data[minIndx],data[j]
    drawData(data, ['green' for x in range(len(data))])

#Quick Sort
def partition(data,low,high,drawData, timeTick):
    Pivot = data[high]
    i  = low

    drawData(data,getColorArray(len(data),low, high, i, i))
    time.sleep(timeTick)

    for j in range (low,high):
        if data[j] < Pivot:
            drawData(data, getColorArray(len(data), low, high, i, j, True))
            time.sleep(timeTick)

            data[i], data[j] = data[j],data[i]
            i = i + 1
        drawData(data, getColorArray(len(data), low, high, i, j))
        time.sleep(timeTick)

    drawData(data, getColorArray(len(data), low, high, i, high, True))
    time.sleep(timeTick)

    data[i] ,data[high] =data[high] , data [i]

    return i


def quick_sort(data, low, high, drawData, timeTick):
    if low < high:
        pi = partition(data,low,high,drawData,timeTick)

        quick_sort(data,low,pi-1,drawData,timeTick)
        quick_sort(data,pi+1,high,drawData,timeTick)

def getColorArray(datalen, low, high, i, currIndx, isSwapping=False):
    colorArray = []
    for x in range(datalen):
        if x >= low and x <= high:
            colorArray.append('grey')
        else:
            colorArray.append('white')
        if x == high:
            colorArray[x] = 'blue'
        elif x == i:
            colorArray[x] = 'red'
        elif x == currIndx:
            colorArray[x] = 'yellow'

        if isSwapping:
            if x == i or x == currIndx:
                colorArray[x] = 'green'
    return colorArray

#Merge Sort
def merge_sort(data, drawData, timeTick):
    merge_sort_alg(data, 0, len(data) - 1, drawData, timeTick)


def merge_sort_alg(data, left, right, drawData, timeTick):
    if left < right:
        middle = (left + right) // 2
        merge_sort_alg(data, left, middle, drawData, timeTick)
        merge_sort_alg(data, middle + 1, right, drawData, timeTick)
        merge(data, left, middle, right, drawData, timeTick)


def merge(data, left, middle, right, drawData, timeTick):
    drawData(data, getColorArray(len(data), left, middle, right))
    time.sleep(timeTick)

    leftPart = data[left:middle + 1]
    rightPart = data[middle + 1: right + 1]

    leftIdx = rightIdx = 0

    for dataIdx in range(left, right + 1):
        if leftIdx < len(leftPart) and rightIdx < len(rightPart):
            if leftPart[leftIdx] <= rightPart[rightIdx]:
                data[dataIdx] = leftPart[leftIdx]
                leftIdx += 1
            else:
                data[dataIdx] = rightPart[rightIdx]
                rightIdx += 1

        elif leftIdx < len(leftPart):
            data[dataIdx] = leftPart[leftIdx]
            leftIdx += 1
        else:
            data[dataIdx] = rightPart[rightIdx]
            rightIdx += 1

    drawData(data, ["green" if x >= left and x <= right else "white" for x in range(len(data))])
    time.sleep(timeTick)


def getColorArray(leght, left, middle, right):
    colorArray = []

    for i in range(leght):
        if i >= left and i <= right:
            if i >= left and i <= middle:
                colorArray.append("yellow")
            else:
                colorArray.append("pink")
        else:
            colorArray.append("white")

    return colorArray

#Bubble Sort
def bubble_sort(data,drawData, timeTick):
    for _  in range(len(data)-1):
        for j in range(len(data)-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1],data[j]
                drawData(data, ['green' if x ==j or x ==j+1 else 'red' for x in range(len(data))])
                time.sleep(timeTick)
    drawData(data, ['green' for x in range(len(data))])
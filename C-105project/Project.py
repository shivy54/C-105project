import math
import csv

file = open("data.csv",newline="")
reader = csv.reader(file)
data = list(reader)
newData = data[0]
def mean(data):
    n = len(data)
    total = 0
    for x in data :
        total += int(x)
    mean = total/n
    return mean
#squaring and gettng the values

sqauredList = []
for number in newData:
    a = int(number) - mean(newData)
    a = a**2
    sqauredList.append(a)
# getting sum
sum = 0
for num in sqauredList:
    sum = sum + num
#dividing the sum by the total value
result = sum/(len(newData)-1)

ans = math.sqrt(result)
print(ans)
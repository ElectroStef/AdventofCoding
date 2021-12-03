import os
import sys
import array
import csv
import numpy as np
from pathlib import Path

sonarArray = []
count = 0

currentDir = os.getcwd()

file = input("file (day1.txt): ")
filePath = os.path.normpath(os.path.join(currentDir, file))

openFile = open(filePath, 'r')
reader = csv.reader(openFile, delimiter = " ")
sonarArray = next(reader)
for col in reader:
        sonarArray.append(col[0])
openFile.close

array = np.array(sonarArray)
finalArray = array.astype(float)

for i in range(len(finalArray)- 1):
    print(finalArray[i], finalArray[i+1])
    if finalArray[i] < finalArray[i+1]:
        count +=

print(count)

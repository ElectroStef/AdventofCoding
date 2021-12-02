import os
import sys
import array
import csv
import numpy as np
from pathlib import Path

x = 0;
z = 0;
y = 0;
sonarArray = []

currentDir = os.getcwd()
file = input("file (day2.txt): ")
filePath = os.path.normpath(os.path.join(currentDir, file))

openFile = open(filePath, 'r')
reader = csv.reader(openFile, delimiter = "\n")
#inputArray = next(reader)
for col in reader:
        sonarArray.append(col[0])
openFile.close

for i in sonarArray:
   commandArray = i.split(' ')
   dir = commandArray[0]
   dis = int(commandArray[1])

   if dir == "forward":
      x += dis
   elif dir == "down":
      z += dis
   elif dir == "up":
      y -= dis

#print(sonarArray)
#print(commandArray)
print("x: ", x)
print("y: ", y) #turns out there is no left right cuz i don't read
print("z: ", z)
#print(input[5])

finalZ = z + y
print("final z:", finalZ)
finalLocation = x*finalZ
print(finalLocation)

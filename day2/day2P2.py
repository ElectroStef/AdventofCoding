import os
import sys
import array
import csv
import numpy as np
from pathlib import Path

x = 0;
z = 0;
aim = 0;
finalDepth = 0;
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
   #print(commandArray)
   if dir == "forward":
      print(commandArray)
      x += dis
      print("horizontal pos" , x)
      finalDepth += dis * aim
      print("depth ", finalDepth)
      print("aim", aim)
   elif dir == "down":
      print(commandArray)
      #z += dis
      aim += dis
      print("horizontal pos" , x)
      print("depth", finalDepth)
      print("aim", aim)
   elif dir == "up":
      #z -= dis
      print(commandArray)
      aim -= dis
      print("horizontal pos" , x)
      print("depth", finalDepth)
      print("aim", aim)


#print(sonarArray)
#print(commandArray)
print("final x: ", x)
#print("z: ", z)
print("final aim ", aim)
print("final depth:", finalDepth)
print(x*finalDepth)
#print(finalLocation)

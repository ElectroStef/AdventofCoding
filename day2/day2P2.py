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
for col in reader:
        sonarArray.append(col[0])
openFile.close

for i in sonarArray:
   commandArray = i.split(' ')
   dir = commandArray[0]
   dis = int(commandArray[1])
   if dir == "forward":
      x += dis
      finalDepth += dis * aim
   elif dir == "down":
      #z += dis
      aim += dis
   elif dir == "up":
      #z -= dis
      aim -= dis

print("final horizontal distance: ", x)
print("final aim ", aim)
print("final depth:", finalDepth)
print(x*finalDepth)

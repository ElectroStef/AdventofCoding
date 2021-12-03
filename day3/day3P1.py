import os
import sys
import array
import csv
import numpy as np
from pathlib import Path


currentDir = os.getcwd()
file = input("file (day3.txt): ")
filePath = os.path.normpath(os.path.join(currentDir, file))

openFile = open(filePath, 'r')
reader = csv.reader(openFile, delimiter = "\n")
for col in reader:
        sonarArray.append(col[0])
openFile.close

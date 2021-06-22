# Author: Cody McWilliams
# Updated: Jun 21, 2021
# Info:
#   Created to check for duplicate IP addresses across multiple text files
#   and locate the duplicates by line number.

import sys
import os
from os import listdir
from os.path import isfile, join

fileMap = {}
equalityMap = {}

# Info Prompt
if len(sys.argv) == 2:
    print("Not enough inputs...\n\nExecuting default behavior...\n")

elif len(sys.argv) > 2:
    print(f"Comparing {sys.argv[1:len(sys.argv)]}")

if len(sys.argv) <= 2:
    print(f"Comparing all files in the parent directory...")

# Get command line arguments or default to all files in parent directory
# Creates map with file names as keys and a list of strings as the value
# Each element of the list is a different line token in the file
if len(sys.argv) > 2:
    for index in range(len(sys.argv)):
        if index == 0:
            continue

        with open(sys.argv[index], 'r') as f:
            fileMap[sys.argv[index]] = f.readlines()
            f.close()
else:
    parentDir = os.getcwd()
    files = [f for f in listdir(parentDir) if isfile(join(parentDir, f))]

    for index in range(len(files)):
        if ".exe" in files[index]:
            continue

        with open(files[index], 'r') as f:
            fileMap[files[index]] = f.readlines()
            f.close()

# Trim each line token
for key in fileMap.keys():
    for index in range(len(fileMap[key])):
        fileMap[key][index] = fileMap[key][index].strip()

# Map file name and line number for each instance of each line token
for key in fileMap.keys():
    for index in range(len(fileMap[key])):
        key2 = str(fileMap[key][index])
        if key2 == '':
            continue

        if key2 not in equalityMap.keys():
            equalityMap[key2] = {}

        if key not in dict(equalityMap[key2]).keys():
            equalityMap[key2][key] = [index + 1]
        else:
            equalityMap[key2][key].append(index + 1)

# Purge mappings that did not appear in more than one file
keysToRemove = []
for key in equalityMap.keys():
    if len(dict(equalityMap[key]).keys()) == 1:
        keysToRemove.append(key)

for key in keysToRemove:
    del equalityMap[key]

# Create program output to display in terminal
message = "\n"

for key in equalityMap.keys():
    message += f"Instance of '{key}' found in:\n"
    for key2 in equalityMap[key]:
        message += f"\t{key2} on the following lines {equalityMap[key][key2]}\n\n"


print(message)

input("Press enter to exit.\n")

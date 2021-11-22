import os

root = os.path.dirname(os.path.abspath(__file__))

for i in range (25):
    folderName = "Day " + str(i + 1)
    os.chdir(root)
    print(os.path.abspath(folderName))
    os.mkdir(folderName)
    os.chdir(root + "/" + folderName)
    pythonFile = open("day" + str(i + 1) + ".py", "w")
    pythonFile.write('import os\nos.chdir("' + folderName + '")\ninput = open("input.txt").readlines()\nfor lineIndex in range(len(input)):\n    line = input[lineIndex].strip()\n    input[lineIndex] = line')
    inputFile = open("input.txt", "w")
    inputFile.write("")
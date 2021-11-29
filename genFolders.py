import os
root = os.path.dirname(os.path.abspath(__file__))

def generate(days):
    for i in days:
        folderName = "Day " + str(i + 1)
        os.chdir(root)
        os.mkdir(folderName)
        os.chdir(root + "/" + folderName)
        pythonFile = open("day" + str(i + 1) + ".py", "w")
        pythonFile.write('import os\nos.chdir("' + folderName + '")\ninput = open("input.txt", "r").readlines()\nfor lineIndex in range(len(input)):\n    line = input[lineIndex].strip()\n    input[lineIndex] = line')
        inputFile = open("input.txt", "w")
        inputFile.write("")

generate(range(10))
# generate(range(10, 25))
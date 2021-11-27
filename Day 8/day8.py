import os
os.chdir("Day 8")
input = open("input.txt", "r").readlines()
for lineIndex in range(len(input)):
    line = input[lineIndex].strip()
    input[lineIndex] = line
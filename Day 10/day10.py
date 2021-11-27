import os
os.chdir("Day 10")
input = open("input.txt", "r").readlines()
for lineIndex in range(len(input)):
    line = input[lineIndex].strip()
    input[lineIndex] = line
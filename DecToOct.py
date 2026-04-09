# --conding:utf-8--
import os

MAX_INT = 2 ** 32 - 1
bIsRightNum = False
strLine = ""
os.system("cls")
print("Input an unsigned integer number:")
try:
    nDecNum = int(input())
    bIsRightNum = nDecNum > 0 and nDecNum <= MAX_INT
except Exception:
    bIsRightNum = False
if (not bIsRightNum):
    print("Invalid number format")
    exit(0)
nTempVal = nDecNum
while (nTempVal > 0):
    strLine = str(nTempVal % 8) + strLine
    nTempVal //= 8
if (len(strLine) == 0):
    strLine = "0"
print(f"The octal equivalent of the decimal number {nDecNum} is {strLine}")

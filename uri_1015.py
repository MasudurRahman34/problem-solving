import math
line1 = input().split(" ")
line2 = input().split(" ")
x1, y1 = line1
x2, y2 = line2
result = math.sqrt((pow(float(x2) - float(x1), 2) + pow(float(y2) - float(y1), 2)))
print(f'{result:.4f}')

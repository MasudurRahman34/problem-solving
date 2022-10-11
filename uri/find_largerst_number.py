num =[1, 2, 3, 4, 5, 6, 7, 8]
max=num[0]
for i in range (len(num)):
    if num[i] > max:
        max = num[i]
print(max)
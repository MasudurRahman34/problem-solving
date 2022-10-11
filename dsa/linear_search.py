
num=[1,2 ,3, 4, 5, 6 ,7, 10, 11]
find=8
def linear_search(num, find):
    for i in range (0, len(num)):
        if num[i]==find :
            return i
    return -1
print(linear_search(num,find));


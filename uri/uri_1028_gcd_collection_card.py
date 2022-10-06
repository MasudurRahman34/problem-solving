
t= int(input())
for i in range(t):
    def computeGCD(a, b):
        if a % b == 0:
            return b
        return computeGCD(b, a % b)


    a, b = map(int, (input().split()))
    result = computeGCD(a, b)
    print(result)
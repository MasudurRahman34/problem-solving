
t=int(input())
for i in range(t):
    n1, divline1, d1, operator, n2, divline2, d2 = input().split()
    n1, d1, n2, d2 = int(n1), int (d1), int(n2),int(d2)
    def computeGCD(d1,d2) -> int:
        if(d1 % d2==0):
            return d2
        return computeGCD(d2, d1%d2)

    # lcd= (d1*d2)/gcd

    if operator=="+":
        numerator= (n1*d2)+(n2*d1)
        denominator = d1 * d2
    if operator=="-":
        numerator= (n1*d2)-(n2*d1)
        denominator = d1 * d2
    if operator=="*":
        numerator= n1*n2
        denominator = d1 * d2
    if operator=="/":
        numerator= n1*d2
        denominator = n2*d1
    gcd= computeGCD(numerator, denominator)
    numerator2=int(numerator/gcd)
    denominator2=int(denominator/gcd)
    print(f'{numerator}/{denominator} = {numerator2}/{denominator2}')
# 1 / 2 + 3 / 4

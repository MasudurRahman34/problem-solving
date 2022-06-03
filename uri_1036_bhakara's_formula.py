import math
a,b,c = list(map(float,input().split()))
formula = (b**2) - (4*a*c)
if formula<0 or a==0:
    print('Impossivel calcular')
else:
    x1 = (-b + math.sqrt(formula))/(2 * a)
    x2 = (-b - math.sqrt(formula))/(2 * a)
    print(f'R1 = {x1:.5f}')
    print(f'R1 = {x2:.5f}')

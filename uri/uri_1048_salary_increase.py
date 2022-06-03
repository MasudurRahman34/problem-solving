
salary = float(input())
if (salary >= 0) and (salary<= 400) :
    increaseRate=15
    interest= (salary*increaseRate)/100
elif (salary >= 400.01) and (salary <= 800):
    increaseRate = 12
    interest = (salary * increaseRate) / 100
elif (salary >= 800.01) and (salary <= 1200):
    increaseRate = 10
    interest = (salary * increaseRate) / 100
elif (salary >= 1200.01) and (salary <= 2000):
    increaseRate = 7
    interest = (salary * increaseRate) / 100
elif salary > 2000:
    increaseRate = 4
    interest = (salary * increaseRate) / 100
total_salary= salary+interest
print(f'''Novo salario: {total_salary:.2f}
Reajuste ganho: {interest:.2f}
Em percentual: {increaseRate} %''')
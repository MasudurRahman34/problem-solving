
taka= int(input())
print(taka)
bankNotes= [100,50,20,10,5,2,1]
for i in bankNotes:
    print(f'{taka // i} nota(s) de R$ {i},00')
    taka=taka % i
days=int(input())
year=days//365
reminder=days%365
month=reminder//30
reminDays=reminder%30
print(f'''{year} ano(s)
{month} mes(es)
{reminDays} dia(s)''')


def romanToInt(self, s: str) -> int:
    listRomanNumber=list(s)
    strlen=len(listRomanNumber)
    romanValue ={
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' :1000
    }
    total=0

    for i in range(strlen-1) :
        if (romanValue[listRomanNumber[i]]) < (romanValue[listRomanNumber[i+1]]) :
            total = total - romanValue[listRomanNumber[i]]
        else :
            total=total+romanValue[listRomanNumber[i]]
    total=total+romanValue[listRomanNumber[-1]]
    return total
# for key, value in romanValue.items():
#     print(key,value)


# for keys, value in romanValue.items() :
#     #if romanValue[keys]== "I" :
#     for romanSymbol in listRomanNumber :
#         if keys==romanSymbol :
#             total=total+value
print(romanToInt("MCMXCIV"))

# for i in listRomanNumber :
#     curr=romanValue[][i]
#     print(curr)

price=[7,6,4,3,1]
len=len(price);
min = price[0]
min_index=0

for i in range(len):

    if price[i] < min :
        min=price[i]
        min_index= i
    # for j in range(i+1,len):
    #     if price[j] < price[min]:
    #         min=j
max_price=price[min_index]
for j in range(min_index+1, len) :
    if price[j] > max_price:
        max_price=price[j]
    max_price = 0
print(max_price)



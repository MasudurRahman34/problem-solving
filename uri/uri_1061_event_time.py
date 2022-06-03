
d1=int(input().split()[-1])
h1,m1,s1=map(int,input().split(" : "))

d2=int(input().split()[-1])
h2,m2,s2=map(int,input().split(" : "))

total_sec1= (d1*24*3600)+(h1*3600)+(m1*60)+s1
total_sec2=(d2*24*3600)+(h2*3600)+(m2*60)+s2
final_sec= total_sec2 - total_sec1
d=final_sec//(24*3600)
rest_time=final_sec%(24*3600)
h=rest_time//3600
rest_time=rest_time%3600
m=rest_time//60
s=rest_time%60

print(f'''{d} dia(s)
{h} hora(s)
{m} minuto(s)
{s} segundo(s)''')

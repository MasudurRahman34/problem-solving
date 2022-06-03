
inputSecond=int(input())
hours= inputSecond//3600
reminder=inputSecond%3600
m=reminder //60
s=reminder % 60
print(f'{hours}:{m}:{s}')
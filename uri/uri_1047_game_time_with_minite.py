
iniHour,iniMinute, finHour, finMinute= map(int,input().split())

totalIniMinute= (iniHour*60)+iniMinute
totalFinMinute=(finHour*60)+finMinute
diffMinute= totalFinMinute-totalIniMinute
if (diffMinute <=0):
    diffMinute = diffMinute+24*60
resultHour = diffMinute // 60
resultMinute = diffMinute % 60
print(f'O JOGO DUROU {resultHour} HORA(S) E {resultMinute} MINUTO(S)')
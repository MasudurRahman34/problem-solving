A,B,C,D=list(map(int,input().split(" ")))

if B>C & D>A & (C+D)>(A+B) & C>0 & D>0 & A%2== 0:
    print('Valores aceitos')
else:
    print('Valores nao aceitos')

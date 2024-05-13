#BEECROWD 1016

d = int(input())
tempo = d * 2
print(f"{tempo} minutos")



#BEECROWD 1153

N = int(input())
FATORIAL = 1

for i in range(1, N+1):
    FATORIAL *= i

print(FATORIAL)



#BEECROWD 1281

N = int(input())
while N:
    N -= 1
    feira = {}
    final = 0.0

    M = int(input())
    while   M:
        M -= 1
        item, valor = input().split()
        feira[item] = float(valor)

    P = int(input())
    while P:
        P -= 1
        item, qt = input().split()
        final += feira[item] * int(qt)

    print(f'R$ {final:.2f}')



#BEECROWD 2006

T = int(input())
CONTAGEM = 0

A,B,C,D,E = map(int, input().split(" "))
numeros = [A,B,C,D,E]

print(numeros.count(T))




#BEECROWD 2339

C, P, F = (input().split())
if int(C) * int(F) <= int(P):
    print('S')
else:
    print('N')




#BEECROWD 2388

N = int(input())
distancia = 0

for i in range(N):
    t, v = map(int, input().split())
    distancia += t * v

print(distancia)



#BEECROWD 2413

t = int(input())

clicks = t * 4

print(clicks)



#BEECROWD 3084

N = int(input())
sequencia = [int(input()) for _ in range(N)]

x = [[0, 0] for _ in range(N+1)]
x[0][0] = 0
x[0][1] = 0

for i in range(1, N + 1):
    if sequencia[i - 1] == 1:
        x[i][0] = max(x[i - 1][0], x[i - 1][1])
        x[i][1] = x[i - 1][0] + 1
    else:
        x[i][1] = x[i - 1][0] + 1

print(max(x[N][0], x[N][1]))









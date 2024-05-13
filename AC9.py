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

C = int(input())
P = int(input())
F = int(input())

if P >= C * F:
    print('S')
else:
    print('N')








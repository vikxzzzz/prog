"""
Exercícios da AC7 no beecrowd em ordem 

"""



# BEECROWD 1048

a = float(input())

if 0 < a <= 400:
    novo_salario = ((a*15)/100 + a)
    porcento = 15 
    reajuste_ganho = novo_salario - a 
    print(f"Novo salario: {novo_salario:.2f}")
    print(f"Reajuste ganho: {reajuste_ganho:.2f}")
    print(f"Em percentual: {porcento} %")
elif 400 < a <= 800:
    novo_salario = ((a*12)/100 + a)
    porcento = 12
    reajuste_ganho = novo_salario - a
    print(f"Novo salario: {novo_salario:.2f}")
    print(f"Reajuste ganho: {reajuste_ganho:.2f}")
    print(f"Em percentual: {porcento} %")
elif 800 < a <= 1200:
    novo_salario = ((a*10)/100 + a)
    porcento = 10
    reajuste_ganho = novo_salario - a
    print(f"Novo salario: {novo_salario:.2f}")
    print(f"Reajuste ganho: {reajuste_ganho:.2f}")
    print(f"Em percentual: {porcento} %")
elif 1200 < a <= 2000:
    novo_salario = ((a*7)/100 + a)
    porcento = 7
    reajuste_ganho = novo_salario - a
    print(f"Novo salario: {novo_salario:.2f}")
    print(f"Reajuste ganho: {reajuste_ganho:.2f}")
    print(f"Em percentual: {porcento} %")
else:
    novo_salario = ((a*4)/100 + a)
    porcento = 4
    reajuste_ganho = novo_salario - a
    print(f"Novo salario: {novo_salario:.2f}")
    print(f"Reajuste ganho: {reajuste_ganho:.2f}")
    print(f"Em percentual: {porcento} %")



# BEECROWD 1065

num = 0

for i in range(5):
    n = float(input())
    if n % 2 == 0:
        num = num + 1
print(f"{num} valores pares")


# BEECROWD 1132

soma = 0

a = int(input())
b = int(input())
if b > a:
    for n in range(a,(b + 1)):
        if (n % 13 != 0):
            soma += n
if a > b:
    for n in range(b,(a + 1)):
        if n % 13 != 0:
            soma += n
print(soma)



# BEECROWD 1173

X = int(input())

for i in range(10):
   print(f"N[{i}] = {X}")
   X *= 2




# BEECROWD 1180

N = int(input())
x = []
a = list(map(int,input().split()))

for i in range (N):
    x.insert(i,a[i])
print(f"Menor valor: {min(x)}")

for i in range(N):
    if x[i] == min(x):
        pos = i
print(f"Posicao: {pos}")



# BEECROWD 1182
n = int(input())
op = input()
matriz = []
vetor = []
soma = 0 
for i in range(12):
    for j in range(12):
        valor = float(input())
        vetor.append(valor)
        if j == n:
            soma += valor
    matriz.append(vetor)
if op == "S":
    print(round(soma), 1)
if op == "M":
    print(round(soma/12), 1) 





       
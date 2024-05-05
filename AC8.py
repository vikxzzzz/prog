#BEECROWD 1028

N = int(input())

def MDC(a, b):
    return a if b == 0 else MDC(b, a % b)

for _ in range(N):
    F1, F2 = [int(x) for x in input().strip().split(' ')]
    print(MDC(F1, F2))


#BEECROWD 1087

while True:
    Z = input().split(" ")
    x1, y1, x2, y2 = Z

    x1 = int(x1)
    y1 = int(x1)
    x2 = int(x2)
    y2 = int(y2)

    if x1 + y1 + x2 + y2 == 0:
        break
    
    if x1 == x2 and y1 == y2:
        print(f"{0}")
        continue
    
    if x1 == x2 or y1 == y2:
        print(f"{1}")
        continue
    
    if (x1 - x2) == (y1 - y2):
        print(f"{1}")
        continue
    
    print(f"{2}")



# BEECROWD 1161

def fatorial(a):
    if a == 0 or a == 1:
        return 1 
    else:
        return fatorial(a - 1) * a

while True:
    try:
        a, b = map(int, input(). split())
        print(fatorial(a) + fatorial(b))
    except EOFError:
        break



# BEECROWD 1170

n = int(input())

for i in range(n):
    num = float(input())
    dias = 0
    
    while(num / 2 > 1):
        dias += 1
        num = num / 2
    print(f"{dias + 1} dias")


# BEECROWD 1171

n = int(input())
lista = []
for i in range(n):
    num = int(input())
    lista.append(num)
    
lista.sort()

while lista != []:
    n = lista.count(lista[0])
    print("{} aparece {} vez(es)".format(lista[0], n))
    for i in range(n):
        lista.remove(lista[0])
     


# BEECROWD 1221

from math import sqrt
x = int(input())
p = 0
primos = []

for numero in range(3, x):
    eprimo = 1
    for i in primos:
        if numero % i == 0:
            eprimo = 0
            print("Não é primo")
            break
        if i > sqrt(numero):
            break
    if eprimo:
        primos.append(numero)
        print ("Primo")
        p += 1


# BEECROWD 1329

while 1:
	N = int(input())

	if N == 0:
		break

	resultados = list(map(int,input().split()))
	m = 0
	j = 0
	for v in resultados:
		if v == 0:
			m += 1
		else:
			j += 1
	print(f"Mary won {m} times and John won {j} times")
     
    

# BEECROWD 1555

n = int(input())

for i in range(n):
    x, y = input().split(' ')
    x = int(x)
    y = int(y)

    a = 2*(x**2) + (5*y)**2
    b = -100*x + y**3
    c = (3*x)**2 + y**2

    if a > b and a > c:
        print ("Beto ganhou")
    elif b > a and b > c:
        print ("Carlos ganhou")
    else:
        print ("Rafael ganhou")


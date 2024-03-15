# EXERCÍCIO 1 

def teste_triangulo(a,b,c):
    return a + b > c

def determina_tipo_triangulo(a,b,c):
    if teste_triangulo(a,b,c):
        if a == b == c:
            return "Equilátero"
        elif  a == b or a == c or b == c:
            return "Isosceles"
        elif a != b != c:
            return "Escaleno"
    else:
        return "Não é um triângulo"
        

print(determina_tipo_triangulo(4, 4, 4)) # Equilátero
print(determina_tipo_triangulo(2, 4, 4)) # Isósceles
print(determina_tipo_triangulo(3, 4, 5)) # Escaleno
print(determina_tipo_triangulo(1, 1, 4)) # Não é um triângulo


"""
Nesse exercício utilizei a condição para a existência de um triângulo, 
que afirma se a soma das medidas de dois deles é sempre maior que a medida do terceiro eles formam um triângulo

"""


#EXERCÍCIO 2

def dia_semana(x):
    if x == 1:
        return "Domingo"
    elif x == 2:
        return "Segunda-feira"
    elif x == 3:
        return "Terça-feira"
    elif x == 4:
        return "Quarta-feira" 
    elif x == 5:
        return "Quinta-feira"
    elif x == 6:
        return "Sexta-feira"
    elif x == 7:
        return "Sábado"
    else:
        print("")

print(dia_semana(2)) # segunda-feira
print(dia_semana(6)) # sexta-feira
print(dia_semana(7)) # sábado
print(dia_semana(9)) # string vazia

"""
Usei o raciocínio do uso de decisao com if e elif

"""

# EXERCÍCIO 3

def soma(a,b):
    return float(a + b)

def subtracao(a,b):
    return float(a - b)

def multiplicacao(a,b):
    return float(a * b) 

def divisao(a,b):
    return float(round(a / b, 3))

def calculadora_simples():
    a = float(input("Informe um número:"))
    b = float(input("Informe outro número:"))
    operacao = input("Informe a operação:")
    if operacao == "soma":
            return print("Resultado:",soma(a,b))
    elif operacao == "subtração":
            return print("Resultado:",subtracao(a,b))
    elif operacao == "multiplicação":
            return print("Resultado:",multiplicacao(a,b)) 
    elif operacao == "divisão":
          return print("Resultado:",divisao(a,b))
    else:
          print("Operação inválida!")

calculadora_simples()

"""
Criei funçoes para as operaçoes pedidas na calculadora
e então usei os comandos de decisão para verificar qual das operaçoes está sendo pedida
"""
"""

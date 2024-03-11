# Equação do segundo grau
def eq_seg_grau(a, b, c):
    D = (b**2 - 4*a*c)
    x1 = (-b + D**(1/2)) / (2*a)
    x2 = (-b - D**(1/2)) / (2*a)
    print("A primeira raiz da equação é:",x1)
    print("A segunda raiz da equação é:",x2)

eq_seg_grau(4,8,9)


# Ano bissexto 

def bissexto(ano):
    return ano%4==0 and ano%100 !=0 or ano%400==0

print(bissexto(2000))

"""
Utilizei o mesmo raciocínio da AC1,na resolução dos problemas de equação de segundo grau e do ano bissexto.
Porém criando uma função para eles.

"""
a = float(input("Informe o parâmetro A da equação:"))
b = float(input("Informe o parâmetro B da equação:"))
c = float(input("Informe o parâmetro C da equação:"))
delta = (b**2)-4*a*c
x1 = (-b + delta**(1/2))/(2*a)
x2 = (-b - delta**(1/2))/(2*a)
print("A primeira raiz da equaçaõ é:", x1)
print("A segunda raiz da equção é:", x2 )

"""
Para calcular as raízes da equação é necessário da raiz quadrada de delta. 
Então para isso utilizei a operação matematica de transformar a raiz quadrada para ma exponenciação do número

"""
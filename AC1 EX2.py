ano = int(input("Informe o ano:"))
print(ano%4==0 and ano%100 !=0 or ano%400==0)
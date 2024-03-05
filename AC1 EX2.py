ano = int(input("Informe o ano:"))
print(ano%4==0 and ano%100 !=0 or ano%400==0)

"""
- Para o ano ser bissexto é preciso que seja múltiplo de 4 e isso significa que o módulo terá que dar 0 
E também, existe duas condições onde são bissextos todos os anos múltiplos de 400, exceto se for múltiplo de 100

"""

# EXERCÍCIO 2 

def calcula_salario(valor_hora, num_hora, irpf = 0.275):
    salario = float(round(valor_hora * num_hora))
    salario_liquido = salario * irpf
    total = salario - salario_liquido
    print("O valor do salário será:",total)
    

calcula_salario(10, 200)



"""
Nessa questão adicionei além do salário líquido pedido,
o imposto de renda que será descontado e também o salário bruto.
 
"""

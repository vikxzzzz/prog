def calcula_salario(valor_hora, num_hora):
    salario = float(round(valor_hora * num_hora))
    irpf = float(round(0.275 * salario,4))
    salario_liquido = float(round(salario - irpf))
    
    print("O salário líquido é:", salario_liquido)
    print("O imposto de renda será de:",irpf)
    print("O salário bruto será de:",salario)

calcula_salario(10, 200)



"""
Nessa questão adicionei além do salário líquido pedido,
o imposto de renda que será descontado e também o salário bruto.
 
"""
"""
Programação Estruturada
2024.1
15/03/2024

Estruturas de Decisão
AC4
"""

def ler_nome():
    """Retorna uma string com o nome do aluno."""
    return input("Informe o nome do aluno: ")

def ler_notas():
    """
    Retorna 4 notas das avaliações AP1, AP2, AS e AC, nesta ordem.
    As notas são do tipo float.
    """
    ap1 = float(input("Informe o valor da AP1: "))
    ap2 = float(input("Informe o valor da AP2: "))
    asub =  float(input("Informe o valor da AS: "))
    ac = float(input("Informe o valor da AC: "))
    return ap1, ap2, asub, ac


def notas_sao_validas(ap1, ap2, asub, ac):
    """
    Retorna True se todas as quatro notas estão entre 0 e 10, inclusive.
    Returna False caso contrário.
    """
    return 0 <= ap1 <= 10 and 0 <= ap2 <= 10 and 0 <= asub <=10 and 0 <= ac <=10


def selecionar_notas(ap1, ap2, asub):
    """
    Retorna as duas maiores notas, considerando que a AS pode substituir a
    AP1 ou a AP2, aquela que tiver a menor nota. Se a AS for menor que as duas,
    retorna apenas a AP1 e a AP2.
    """
    if ap1 < asub:
        return asub, ap2
    if ap2 < asub:
        return asub, ap1


def calcular_media(nota1, nota2, ac):
    """
    Retorna a média da disciplina, arredondada em duas casas decimais.
    M = (AP1 + AP2) * 0.4 + AC * 0.2
    """
    return round((nota1 + nota2) * 0.4 + 0.2 * ac,2)

def aluno_foi_aprovado(media):
    """
    Retorna True se o aluno foi aprovado, e False caso contrário.
    A média de aprovação é 7.0.
    """
    return media >= 7

def analisar_media(media):
    """
    Exibe a média na tela.
    Exibe se o aluno foi aprovado ou reprovado.
    """
    print(media)
    if aluno_foi_aprovado(media):
        print("Aluno foi aprovado.")
    else:
        print("Aluno foi reprovado.")

def main():
    nome = ler_nome()
    if nome:
        ap1, ap2, asub, ac = ler_notas()
        if notas_sao_validas(ap1, ap2, asub, ac):
            nota1, nota2 = selecionar_notas(ap1, ap2, asub)
            media = calcular_media(nota1, nota2, ac)
            analisar_media(media)


main()
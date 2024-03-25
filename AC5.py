import random

# AVENTUREIRO

"""
# Vida inicial = 100
# Ataque entre 10 e 20 aleatoriamente 
# Defesa entre 1 e 5 aleatoriamente
"""



# MONSTRO
"""
- Vida aletória entre 60 e 80 
- Ataque é um valor aleatório entre 20 e 30
- Não possui defesa 

"""

def main ():
    
    # ATRIBUTOS AVENTUREIRO 
    vida = 100                          
    att = random.randint(10,20)
    defesa = random.randint(1,5)
    
    # ATRIBUTOS MONSTRO
    vida2 = random.randint(60,80)
    att2 = random.randint(20,30)
    
    # DANO DO AVENTUREIRO NO MONSTRO 
    dano_aventureiro = random.randint(1, att)   
       
    
    # DANO DO MONSTRO NO AVENTUREIRO  
    dano_do_monstro = random.randint(1, att2) - defesa    
         
    
    print("Aventureiro:","vida", vida,"- att", att,"- defesa", defesa)
    print("Monstro:","vida",vida2,"- att", att2)
    
    rodada = 1
    
    while vida > 0 and vida2 > 0:
        print("Rodada",rodada)
        vida2 -= dano_aventureiro
        if vida2 <= 0:
            print("O monstro morreu!")
            break
        vida -= dano_do_monstro
        if vida <= 0:
            print("Você morreu!")
            break
            
        rodada += 1
        print("Aventureiro:","vida", vida,"- att", att,"- defesa", defesa)
        print("Monstro:","vida",vida2,"- att", att2)
    
    


main()
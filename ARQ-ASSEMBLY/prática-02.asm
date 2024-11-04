;Exercício 01
;Prática 02

.DEF par1 = r0
.DEF par2 = r1
.DEF par3 = r2
.DEF soma = r3
.DEF aux = r17

;Carregar a tabela inicial de dados nos registradores
inicio: ldi r16, 0xE
ldi aux, 0x6
mov par1,r16
mov par2,par1
inc par2
inc par2 
mov par3,par2
inc par3
inc par3


;Carregar a tabela de dados na memória 
loop: sts 0x200,par1
sts 0x201,par2
sts 0x0202,par3

;Ler os dados da memória, soma e armazena a soma em memória
lds par1,0x200
add soma,par1
lds par2,0x201
add soma,par2
lds par3,0x202
add soma,par3
sts 0x203,soma

;Atualizar os pares 
add par1,aux
add par2,aux
add par3,aux
rjmp loop

break


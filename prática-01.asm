;
; AssemblerApplication1.asm
;
; Created: 28/10/2024 17:00:19
; Author : 202402070134
;


; Replace with your application code
inicio:
    ldi r16,0x2 ; inicializo registrador
	mov r0,r16
	mov r1,r0
	inc r1
	inc r1
	mov r2,r1
	inc r2
	inc r2
	mov r3,r2
	inc r3
	inc r3
	mov r4,r3
	inc r4
	inc r4
	mov r5,r4
	inc r5
	inc r5

	; somando os dados
	add r6,r0
	add r6,r1
	add r6,r2
	add r6,r3
	add r6,r4
	add r6,r5

	; tabela de dados
	sts 0x200,r0
	sts 0x201,r1
	sts 0x202,r2
	sts 0x203,r3
	sts 0x204,r4
	sts 0x205,r5
	sts 0x206,r6


	

	break

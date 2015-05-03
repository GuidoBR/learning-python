import random
numeroAleatorio = random.randint(1, 20) # rodar um dado para saber o número
numeroTentativas = 0
while(True):
	print('Tente acertar')
	numero = int(input())
	numeroTentativas += 1
	if (numero > numeroAleatorio):
		print('Você errou, tente um número menor')
	if (numero < numeroAleatorio):
		print('Você errou, tente um número maior')
	if (numero == numeroAleatorio):
		print('Você acertou!')
		print('Você usou ' + str(numeroTentativas) + ' tentativas')
		break

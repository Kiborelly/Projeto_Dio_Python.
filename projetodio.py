#pylint:disable=W1309
valor_montante_final = 0.0
extrato = []
contador = 0
	
while True:
	menu = (
	 f'''	Seja bem vindo ao banco Nosso Banco!
	  #################################
	  Seu saldo é R${valor_montante_final:.2f}
	      
	      Digite a opção desejada: 
	      
	      (1) - Para deposito
	      (2) - Para saque
	      (3) - Para extrato
	      (0) - Para sair
	      R:  '''
)


	opcao_escolhida = int(input(menu))
	
	if opcao_escolhida == 1:
		valor_deposito = float(input(f'''
	Informe o valor do deposito.
	R$: '''))
	
		if valor_deposito > 0:
			valor_montante_final += valor_deposito
		
			extrato.append(f'''Deposito de R${valor_deposito}''')
		
			print(f'''	Realizando deposito...
     	O valor de R${valor_deposito} foi
     	adicionado a sua conta
     	
     	''')
     	
		elif valor_deposito <= 0:
			print(f'''	Insira um valor positivo para operação.
		''')
	
	elif opcao_escolhida == 2:
		
		valor_saque = float(input(f'''
	Informe o valor do saque.
	R$: '''))
		if valor_saque <= valor_montante_final and valor_saque > 0 and valor_saque <= 500 and contador < 3:
			
			contador += 1
			
			valor_montante_final -= valor_saque
		
			extrato.append(f'''Saque de R${valor_saque}''')
		
			print(f'''	Realizando saque...
	O valor de R${valor_saque} foi
	Retirado da sua conta''')
	
		elif valor_saque <= 0:
			print(f'''	Insira um valor positivo para operação.
		''')
			
		elif valor_saque > valor_montante_final:
			print(f'''	Saldo insuficiente.
			''')
		
		elif contador == 3:
			print(f'''	Limite de saques diarios excedido.
			''')
			
		elif valor_saque > 500:
			print(f'''	O limite por saque é de R$500.00 reais.
			''')
		
		else:
			print(f'''	Erro indefinido.
			''')
			
	elif opcao_escolhida == 3:
		if extrato:
			print(f''' 
		Olá  seja bem vindo
					
		Segue o resumo de suas transacões
		------------------------------------------''')
			for transacao in extrato:
					print (f'''		{transacao}
					--------------''')
					
			print(f'''		saldo - R${valor_montante_final:.2f}
			###################
			
			''')
			
		else: print(f'''	Não há movimentações.
		''')
		
	elif opcao_escolhida == 0:
		print(f'''	Saindo...
		''')
		break
		
	else:
		print(f'''	Opição invalida''')
		
	

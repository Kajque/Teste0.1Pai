
print("Bem vindo.")

refs = {
	# 'motorista' : '',

	# 'cidade' : '',

	# 'petroleo': '',

	# 'quantidade' : ''
}

def motorista():
	passs = '1'
	while passs == '1':
		cont_motor = 4

		opcoes = {

		'1': 'Gustavo',
		'2': 'Denis',
		'3': 'Glebio',
		'4': 'Voltar',
		}
		print(f''' 
			[1] Gustavo
			[2] Denis
			[3] Glebio
			[4] Voltar

			''')
		op = input()
		if op not in opcoes:
			print('opcao invalida tente novamente')
		if op == '1':
			motor = 'Gustavo'
			passs = 3
		if op == '2':
			motor = 'Denis'
			passs = 3
		if op == '3':
			motor = 'Glebio'
			passs = 3
		if op == '4':
			print('saindo')
			passs = 3
			break
		refs[0] = motor


def cidade():
	passs = '1'
	while passs == '1':

		cont_cidade = 3
		opcoes = {
		'1', 'Santa fe',
		'2', 'Ibia',
		'3', 'Uberaba',}
		print(f''' 
			[1]	Santa fe
			[2] Ibia
			[3] Uberaba
			[4] Sair
			''')
		op = input()
		if op not in opcoes:
			print('opcao invalida tente novamente')
		if op == '4':
			passs = 3
			break
		if op == '1':
			passs = 3
			cidade = 'santa fe'
		if op == '2':
			passs = 3
			cidade = 'ibia'
		if op == '3':
			passs = 3
			cidade = 'uberaba'
		refs[1] = cidade
def petroleo():
	petroleo = input("Qual o tipo de combustivel? ")
	refs[2] = petroleo
	quant = float(input("Quantidade: "))
	refs[3] = quant

from func1 import *

def menu():
	print(f''' 
	--- GED ---
	[1] Iniciar
	[2] Adicionar
	[3] Creditos

 	''')

	esc = input('Opcao: ')

	if esc == '1':
		motorista()
		cidade()
		petroleo()
		print(f''' 
			Motorista: {refs[0]}
			Cidade: {refs[1]}
			tipo de carga: {refs[2]}
			quantidade: {refs[3]}

			''')
	elif esc == '2':
		print('2')
	elif esc == '3':
		print("@Kajque")
	else:
		print("Algo deu errado tente novamente")
		menu()
menu()


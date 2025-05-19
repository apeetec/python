"""Informações de entrada do usuário """
print('Sejam bem vindo, preencha os dados abaixo')
nome = input('Digite seu nome ')
email = input('Digite seu e-mail ')
""" fim das informações de entrada do usuário """

""" Loop de repetição que verifica se o e-mail foi preenchido """
while email == '':
    print('O campo de e-mail é obrigatório')
    email = input('Digite seu e-mail: ')
""" fim do loop de repetição que verifica se o e-mail foi preenchido """
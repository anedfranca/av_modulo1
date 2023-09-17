'''Crie um exemplo de cada uma das principais tipagens de variáveis.'''

#string
nome = (input('Digite seu nome: '))
print(f'Olá {nome}')
#int
hora = int (input ("Digite quanto voce ganha por hora: "))
mes = int (input ("Digite o numero de horas trabalhadas no mês: "))
total = hora*mes
print (f"seu salario referido no mes {total}")
print('Proxima pergunta..')
#float
nota1 = float (input ("Digite sua priemra nota: "))
nota2 = float (input ("Digite sua 2 nota: "))

media = (nota1 + nota2)/2

if (media==10):
    print ("Aprovado com distinção")

elif (media>=7):
    print ("Aprovado")

elif (media<7):
    print ("Reprovado")

'''Crie uma solicitação de dados ao usuário.
Imprima a solicitação anterior na tela com uma mensagem personalizada'''
nome = input('Digite seu nome: ')
cor = input( 'Digite sua cor favorita: ')
ano = int(input('Digite o ano em que nasceu: '))
idade = 2023-ano

print(f'Olá {nome}, sua cor favorita é {cor} e a sua idade é {idade}')
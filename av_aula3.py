''''Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. 
O usuário deve informar de qual número ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo'''

num = int(input('Informe o numero de 1 a 10 que você deseja ver a tabuada: '))

for i in range (1,11):
    print(f'{num} x {i} = {num*i}')
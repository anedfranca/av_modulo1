'''Escreva um programa em python que pergunte ao usuário a velocidade de um carro. Caso ultrapasse 80 km/h, 
 exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba o valor da multa, 
 cobrando R$20,00 por cada km que exceder 80 km/h.'''
velocidade = int(input('Qual a velocidade de um carro? '))
if velocidade>80:
     print(f'''Você ultrapassou o limite de velocidade 80Km/h, portanto você foi multado.
           Sua multa é no valor de R${(velocidade - 80)*20 :.2f}''')
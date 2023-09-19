'''Escreva um programa em python que leia números inteiros do teclado.
O programa deve ler os números até que o usuário digite 0 (zero). No final da execução, 
exiba a quantidade de números digitados, assim como a soma e a média aritmética.'''

soma = 0
quantidade = 0
while True:
    n = int(input("Digite um número inteiro: "))
    if n == 0:
        break
    soma = soma + n
    quantidade = quantidade + 1
    media = soma / quantidade
print(f''' A quantidade de números digitados é {quantidade}
      A soma dos números resultam em {soma}
      A média aritmétrica é {media:10.2f}''')

from os import system

while True:
    n1 = input('Digite um número: ')
    n2 = input('Digite outro número: ')
    operador = input('Digite um operador (+-*/): ')
    operadores_permitidos = '+-*/'

    numeros_validos = None
    n1_float = 0
    n2_float = 0
    
    try:    
        n1_float = float(n1)
        n2_float = float(n2)
        numeros_validos = n1_float, n2
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        system('pause')
        system('cls')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador')

    if operador not in operadores_permitidos:
        print('Operador Inválido.')

    print('Realizando a sua conta. Confira o resultado abaixo:')    
    if operador == '+':
        print(f'{n1_float} + {n2_float} =', n1_float + n2_float)
    elif operador == '-':
        print(f'{n1_float} - {n2_float} =', n1_float - n2_float)
    elif operador == '*':
        print(f'{n1_float} * {n2_float} =', n1_float * n2_float)
    elif operador == '/':
        print(f'{n1_float} / {n2_float} =', n1_float / n2_float)
    else:
        print('Nunca deveria chegar aqui!')
    
    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    if sair is True:
        break
    system('cls') 
    
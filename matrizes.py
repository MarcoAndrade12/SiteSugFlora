import numpy as np
import os


while True:
    Matriz = []
    Ind = []

    def clear():
        os.system('clear')
        
    def intMatriz(Matriz):
        MatrizFinal = []
        for i in Matriz:
            MatrizFinal.append([float(i[0]),float(i[1]),float(i[2])])
        return MatrizFinal

    def int_Ind(i):
        MatrizFinal = [float(i[0][0]),float(i[0][1]),float(i[0][2])]
        return MatrizFinal


    while len(Matriz) < 3:
        clear()
        print('CRIAÇÃO DA MATRIZ')
        print('\n'.join(map(str,Matriz)))
        linha = input(f'Digite a {len(Matriz)+1}° linha da matriz separado por vírgula, ex: 1,2,3\n')
        
        if len(linha.split(',')) == 3:
            Matriz.append(linha.split(','))

    while len(Ind) < 1:
        clear()
        print('CRIAÇÃO DO INDEPENDENTE')
        print('\n'.join(map(str,Ind)))
        linha = input(f'Digite os itens do independente separado por vírgula, ex: 1,2,3\n')
        
        if len(linha.split(',')) == 3:
            Ind.append(linha.split(','))

    Matriz = intMatriz(Matriz)
    Ind = int_Ind(Ind)

    clear()
    print(f'{" Matriz ":^25}')
    print('\n'.join(map(str,Matriz)))
    print('\nMatriz independente:\n ', Ind)
    
    try:
        MatrizInv = np.linalg.inv(Matriz)
        print('\nMatriz invertida: \n', MatrizInv)
        print('\nResultado final: ', np.dot(MatrizInv,Ind))
    except:
        print('\nA Matriz informada é singular e não existe inversa!!.')
        print(Ind)

    resp = input('\n\nDeseja tentar novamente? S/N: ').upper()
    if resp == 'N':
        clear()
        print('Obrigado por usar esse programa!')
        break

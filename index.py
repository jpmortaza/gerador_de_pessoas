import gerador

print('''
    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
       ............GERADOR DE PESSOAS............
    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
''')

print(
'''
[ 1 ] - MULHER - NOME SIMPLES
[ 2 ] - HOMEM - NOME SIMPLES
[ 3 ] - RANDOM
''')

escolha = input("DIGITE SUA ESCOLHA:")
escolha = int(escolha)

while(escolha != 3):
    if(escolha == 1):
        print("GERADOR DE MULHERES")
        gerador.ger_mulher()

    else:
        print("GERADOR DE HOMENS")
        gerador.ger_homem()
        break


#IMPLEMENTANDO - [1.5] - MULHER - NOME COMPOSTO, [2.5] - HOMEM - NOME COMPOSTO,

# DESCEDENCIA - SOBRENOMES ITALIANOS



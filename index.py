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
[ 3 ] - SAIR
''')

escolha = input("DIGITE SUA ESCOLHA:")
escolha = int(escolha)

while(escolha != 3):
    if(escolha == 1):
        print("GERADOR DE MULHERES")
        gerador.ger_mulher()

    elif(escolha == 2):
        print("GERADOR DE HOMENS")
        gerador.ger_homem()
        break
print('''
--- OBRIGADO POR UTILIZAR NOSSO SITEMA --- 
by JPMortaza
''')
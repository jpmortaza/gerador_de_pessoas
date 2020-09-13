import random
from unidecode import unidecode

def ger_homem():
    qtd = input("QUANTIDADE:")
    qtd = int(qtd)
    arquivo_nomes = open('resultado.csv', 'a') #CRIA O ARQUIVO
    impresso = 1

# SORTEIA UM NOME
    while (impresso <= qtd):
#RANDOM NOME
        arquivo_list_nome = open('_listas/list_nomes_hom.txt', 'r')
        nome = []
        for nome_linha in arquivo_list_nome:
            nome_linha = nome_linha.strip()
            nome.append(nome_linha)
        nome_numero = random.randrange(0, len(nome))
        nome_result = nome[nome_numero].title()

#SORTEIA UM SOOBRENOME DA LISTA
        arquivo_sobrenome = open('_listas/list_sobrenomes.txt', 'r')
        sobrenome = []
        for sobrenome_linha in arquivo_sobrenome:
            sobrenome_linha = sobrenome_linha.strip()
            sobrenome.append(sobrenome_linha)
        sobrenome_numero = random.randrange(0, len(sobrenome))
        sobrenome_resul = sobrenome[sobrenome_numero].title()

# SORTEIA UMA CIDADE
        arquivo_list_cidades = open('_listas/list_cidades_rs.txt', 'r')
        cidade = []
        for cidade_linha in arquivo_list_cidades:
            cidade_linha = cidade_linha.strip()
            cidade.append(cidade_linha)
            numero_cidade = random.randrange(0, len(cidade))
            cidade_result = cidade[numero_cidade].title()

# SORTEIA UMA DATA DE NASCIMENTO
        ano = random.randrange(1980, 2002)
        ano = str(ano)
        dia = random.randrange(1, 30)
        dia = str(dia)
        mes = random.randrange(1, 12)
        mes = str(mes)
        data_nasc_result = (dia + '/' + mes + '/' + ano)

# GERADOR DE SENHAS
        gera_senha = random.randrange(1000, 9999)
        gera_senha = str(gera_senha)
        senha_resul = ano + nome_result + '@' + gera_senha


# E-MAIL
        link_email = "https://www.invertexto.com/gerador-email-temporario?email="
        email = unidecode(nome_result + sobrenome_resul + ano + gera_senha + '@uorak.com')
        email_link_result = link_email + email.replace(" ", "")

# SALVA NO ARQUIVO
        arquivo_nomes.write(
            nome_result + ' ' + sobrenome_resul + ',' + data_nasc_result + ',' + cidade_result + ',' + senha_resul + ',' + email_link_result + '\r\n')

#IMPRIME OS DADOS GERADOS
        print(nome_result + ' ' + sobrenome_resul + ',' + data_nasc_result + ',' + cidade_result + ',' + senha_resul + ',' + email_link_result)
        impresso = impresso + 1

    else:
        print("*** NOMES GERADOS ***")

    arquivo_list_nome.close()
    arquivo_sobrenome.close()
    arquivo_list_cidades.close()

def ger_mulher():
    qtd = input("QUANTIDADE:")
    qtd = int(qtd)
    arquivo_nomes = open('resultado.csv', 'a') #CRIA O ARQUIVO
    impresso = 1

# SORTEIA UM NOME
    while (impresso <= qtd):
#RANDOM NOME
        arquivo_list_nome = open('_listas/list_nomes.txt', 'r')
        nome = []
        for nome_linha in arquivo_list_nome:
            nome_linha = nome_linha.strip()
            nome.append(nome_linha)
        nome_numero = random.randrange(0, len(nome))
        nome_result = nome[nome_numero].title()

#SORTEIA UM SOOBRENOME DA LISTA
        arquivo_sobrenome = open('_listas/list_sobrenomes.txt', 'r')
        sobrenome = []
        for sobrenome_linha in arquivo_sobrenome:
            sobrenome_linha = sobrenome_linha.strip()
            sobrenome.append(sobrenome_linha)
        sobrenome_numero = random.randrange(0, len(sobrenome))
        sobrenome_resul = sobrenome[sobrenome_numero].title()

# SORTEIA UMA CIDADE
        arquivo_list_cidades = open('_listas/list_cidades_rs.txt', 'r')
        cidade = []
        for cidade_linha in arquivo_list_cidades:
            cidade_linha = cidade_linha.strip()
            cidade.append(cidade_linha)
            numero_cidade = random.randrange(0, len(cidade))
            cidade_result = cidade[numero_cidade].title()

# SORTEIA UMA DATA DE NASCIMENTO
        ano = random.randrange(1980, 2002)
        ano = str(ano)
        dia = random.randrange(1, 30)
        dia = str(dia)
        mes = random.randrange(1, 12)
        mes = str(mes)
        data_nasc_result = (dia + '/' + mes + '/' + ano)

# GERADOR DE SENHAS
        gera_senha = random.randrange(1000, 9999)
        gera_senha = str(gera_senha)
        senha_resul = ano + nome_result + '@' + gera_senha

#E-MAIL
        arquivo_email = open('_listas/list_e-mail.txt', 'r')
        email = []
        for email_linha in arquivo_email:
            email_linha = email_linha.strip()
            email.append(email_linha)
            email_numero = random.randrange(0, len(email))
            link_email = "https://generator.email/"
            email_resul = email[email_numero]
            email_email = unidecode(nome_result + sobrenome_resul + ano + email_resul)
            email_link_result = link_email + email_email.replace(" ", "")  # link do email

#SALVA NO ARQUIVO
        arquivo_nomes.write(nome_result + ' ' + sobrenome_resul + ',' + data_nasc_result + ',' + cidade_result + ',' + senha_resul + ',' + email_email + ',' + email_link_result + '\r\n' )

        # -- imprime os nomes gerados - tem que ser as ultimas linhas do arquivo
        print(nome_result + ' ' + sobrenome_resul + ',' + data_nasc_result + ',' + cidade_result + ',' + senha_resul + ',' + email_email + ',' + email_link_result)
        impresso = impresso + 1

#FINAL
    else:
        print("*** NOMES GERADOS ***")

    arquivo_list_nome.close()
    arquivo_sobrenome.close()
    arquivo_list_cidades.close()

def ger_fotos():
    print('''
       [] Idade
       [] Cor do cabelo
       [] Sexo
    ''')


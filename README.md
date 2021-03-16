# GERADOR DE PESSOAS
O anonimato em redes sociais é um direito de todo Brasileiro, visando a não utilização de dados de pessoas reais, criei esse script simples em Python que gera alguns dados.

O script gera dados para perfis em redes sociais.

Módulos adicionados:
- [x] Nome;
- [x] Data de nascimento;
- [x] Cidade;
- [x] E-mail;
- [x] Senha;
- [x] Link da caixa de e-mail;
- [x] Bio;
- [ ] Instagram.
- [ ] Twitter.


Na pasta _listas estão os dados para gerar os usuários:
<img width="1228" alt="Captura de Tela 2020-09-13 às 19 22 06" src="https://user-images.githubusercontent.com/13164359/93030084-c68b4f80-f5f6-11ea-8d2e-c4a80d2015dd.png">
Para adicionar mais dados abra os links e adicione os dados:
- list_cidades.txt (adicione cidades).
- list_email.txt (esse arquivo não deve ser editado).
- list_nomes.txt (nomes femininos, pode ser adicionados mais nomes ou editar os existentes).
- list_nomes_hom.txt (nomes masculinos, pode ser adicionados mais nomes ou editar os existentes).
- list_profissoes.txt (não criado ainda as profissões dos perfis).
- list_sobrenomes.txt (sobrenomes, pode ser adicionados mais nomes ou editar os existentes).
- list_sobrenomes_italianos.txt (sobrenomes italianos, não criado ainda modo de escolha de sobrenomes).

## INSTALAÇÃO 
```
git clone https://github.com/JPMORTAZA/gerador_de_pessoas.git
cd gerador_de_pessoas
pip install -r requirements.txt
python index.py
```


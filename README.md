Primeiramente eu gostaria de agradecer a oportunidade de participar desse desafio.

Fiz a automação utilizando Python + cucumber + gherkin. Para rodar os testes, basta rodar: behave feature/aluguel_livros.feature --no-capture

Para que possa ser exibido os prints de cada etapa que está sendo validada, é necessário rodar o --no-capture

Foi utilizado programação orientada a objeto, onde foi dividido um arquivo para os endpoints, outro para os requests. Também foi criado um arquivo para os livros afim de conseguir acessar com facilidade os itens dentro de cada um deles. O arquivo user.py foi criado para poder manipular o json do usuário e conseguir validar que de fato tem o isbn validado.

Para que não fosse necessário utilizar de uma aleatoriedade todas as vezes que fosse criar um novo usuário e não encher o banco, criei o step de deletar após os testes, contudo está retornando 204 que na api definida mostra que é 'Unauthorized', mas 204 é sucesso em retorno http.

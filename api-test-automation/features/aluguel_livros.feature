Feature: Aluguel de livros por um novo usuário

  Scenario Outline: Criar usuário, autenticar, listar livros, alugar dois livros e validar dados do usuário
    Given que um novo usuário é criado com o username "<username>" e a senha "<password>"
    And o usuário realiza login com sucesso
    When o usuário acessa a listagem de livros disponíveis
    And seleciona dois livros para alugar
    Then o sistema deve mostrar os detalhes do usuário
    And os dois livros alugados devem estar associados a esse usuário

    Examples:
      | username   | password      |
      | Holanda    | Senha@123     |
      | Goncalves  | Senha@123     |
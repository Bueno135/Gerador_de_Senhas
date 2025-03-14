## Gerador de Senhas Aleatórias
Este projeto contém um gerador de senhas aleatórias que permite ao usuário personalizar a senha gerada de acordo com suas preferências. A senha gerada pode incluir letras maiúsculas, minúsculas, números e símbolos, com controles de comprimento mínimo e máximo.

## Funcionalidades
Personalização: O usuário pode escolher o número de letras, números e símbolos na senha.
Maiúsculas e Símbolos: O código permite que o usuário decida se deseja incluir letras maiúsculas e símbolos especiais na senha.
Comprimento da Senha: O usuário pode definir tanto o comprimento mínimo quanto o máximo da senha gerada.
Aleatoriedade: A senha é gerada de forma aleatória e embaralhada para aumentar a segurança.

## Como Funciona
O usuário é solicitado a inserir o número de letras, números e símbolos desejados na senha.
O comprimento mínimo e máximo da senha também são informados.
O código gera a senha com base nas preferências fornecidas:
Letras: Pode incluir letras maiúsculas ou minúsculas.
Números: Inclui números de 0 a 9.
Símbolos: Inclui caracteres especiais como !, @, #, entre outros.
O código garante que a senha tenha o comprimento mínimo especificado e não ultrapasse o comprimento máximo.
A senha gerada é embaralhada para maior segurança e convertida em uma string final.

## Como Usar
Execute o código.
Insira os parâmetros solicitados, como a quantidade de letras, números e símbolos, além do comprimento mínimo e máximo.
A senha gerada será exibida no final.

##Exemplo de Saída

```bash
Bem-vindo ao gerador de senhas!
Digite a quantidade de letras da senha desejada: 8
Digite a quantidade de números da senha desejada: 3
Digite a quantidade de símbolos da senha desejada: 2
Digite o comprimento mínimo da senha: 12
Digite o comprimento máximo da senha: 16
Incluir letras maiúsculas? (s/n): s
Incluir símbolos? (s/n): s

Senha gerada: G9k@vB3j8!zP

import random
import string

def gerar_senha(nr_letters, nr_numbers, nr_symbols, min_length, max_length, incluir_maiusculas=True, incluir_simbolos=True):
    """
    Gera uma senha baseada nas preferências do usuário.
    
    Parameters:
    nr_letters (int): Quantidade de letras na senha.
    nr_numbers (int): Quantidade de números na senha.
    nr_symbols (int): Quantidade de símbolos na senha.
    min_length (int): Comprimento mínimo da senha.
    max_length (int): Comprimento máximo da senha.
    incluir_maiusculas (bool): Incluir letras maiúsculas (opcional).
    incluir_simbolos (bool): Incluir símbolos (opcional).
    
    Returns:
    str: Senha gerada.
    """
    # Definir os tipos de caracteres possíveis
    letras_minusculas = string.ascii_lowercase
    letras_maiusculas = string.ascii_uppercase
    numeros = string.digits
    simbolos = string.punctuation

    # Gerar as partes da senha
    letras = letras_minusculas
    if incluir_maiusculas:
        letras += letras_maiusculas
    
    caracteres = []

    # Adicionar letras
    caracteres += [random.choice(letras) for _ in range(nr_letters)]
    
    # Adicionar números
    caracteres += [random.choice(numeros) for _ in range(nr_numbers)]
    
    # Adicionar símbolos
    if incluir_simbolos:
        caracteres += [random.choice(simbolos) for _ in range(nr_symbols)]
    
    # Verificar o comprimento mínimo e máximo
    while len(caracteres) < min_length:
        caracteres.append(random.choice(letras + numeros + simbolos))  # Preencher até o mínimo com caracteres aleatórios

    # Garantir que a senha não ultrapasse o comprimento máximo
    if len(caracteres) > max_length:
        caracteres = caracteres[:max_length]

    # Embaralhar a senha para aumentar a aleatoriedade
    random.shuffle(caracteres)
    
    # Converter para string
    senha = ''.join(caracteres)
    
    return senha

# Solicitar dados do usuário
print("Bem-vindo ao gerador de senhas!")
nr_letters = int(input("Digite a quantidade de letras da senha desejada: "))
nr_numbers = int(input("Digite a quantidade de números da senha desejada: "))
nr_symbols = int(input("Digite a quantidade de símbolos da senha desejada: "))
min_length = int(input("Digite o comprimento mínimo da senha: "))
max_length = int(input("Digite o comprimento máximo da senha: "))
incluir_maiusculas = input("Incluir letras maiúsculas? (s/n): ").lower() == 's'
incluir_simbolos = input("Incluir símbolos? (s/n): ").lower() == 's'

# Gerar a senha
senha = gerar_senha(nr_letters, nr_numbers, nr_symbols, min_length, max_length, incluir_maiusculas, incluir_simbolos)

print(f"Senha gerada: {senha}")

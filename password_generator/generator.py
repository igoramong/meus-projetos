
import random
import string

def gerar_senha(tamanho=12, incluir_maiusculas=True, incluir_numeros=True, incluir_especiais=True):
    # Definir os conjuntos de caracteres a serem usados
    caracteres = string.ascii_lowercase  # Letras minúsculas
    
    if incluir_maiusculas:
        caracteres += string.ascii_uppercase  # Letras maiúsculas
    
    if incluir_numeros:
        caracteres += string.digits  # Números
    
    if incluir_especiais:
        caracteres += string.punctuation  # Caracteres especiais

    # Gerar a senha
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    
    return senha

# Teste da função
if __name__ == "__main__":
    senha_gerada = gerar_senha()
    print("Senha gerada:", senha_gerada)

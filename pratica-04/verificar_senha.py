def verificar_senha(senha):
    # Verifica se a senha tem pelo menos 8 caracteres
    if len(senha) < 8:
        return False
    # Verifica se a senha contém pelo menos um número
    if not any(char.isdigit() for char in senha):
        return False
    return True

while True:
    senha = input("Digite uma senha forte (ou 'sair' para encerrar): ")
    if senha.lower() == 'sair':
        print("Encerrando o programa. Até mais!")
        break
    if verificar_senha(senha):
        print("Senha forte aceita!")
        break
    else:
        print("Senha fraca. Tente novamente.")
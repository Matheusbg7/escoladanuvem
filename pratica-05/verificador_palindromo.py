def is_palindromo(texto):
    # Remover os espaços e converte para minúsculas
    texto_limpo = ''.join(char.lower()
                          for char in texto
                          if char.isalum())
    
    return texto_limpo == texto_limpo[::-1]




expressao = set(print("Insira uma expressão para verificação: "))
resultado = is_palindromo(expressao)

if resultado == True:
    resposta = "Sim"
else:
    resposta = "Não"

print(f"A expressão {expressao} é uma palindromo? {resposta}")
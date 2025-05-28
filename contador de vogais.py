
def conta_vogais(texto):
# TODO: Defina um conjunto de vogais tanto minúsculas quanto maiúsculas:
    vogais = set('aeiouAEIOU')
    
# TODO: Inicialize um contador para contar as vogais:
    contador = 0

# Iteramos pelos caracteres da string
    for char in texto:
# TODO: Verifique se o caractere atual é uma vogal e incremente o valor do contador:
        if char in vogais:
            contador += 1
    
    return contador
while True:
    # Solicitamos ao usuário que insira uma string
    texto = input("Digite a Palavra: ")

    # Chamamos a função conta_vogais e exibimos o resultado
    resultado = conta_vogais(texto)
    print(f"O número de vogais na string '{texto}' é: {resultado}")

    continuar = input("Deseja Continuar? (s/n):  ")
    
    if continuar != "s":
        break
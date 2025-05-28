# 📝 Contador de Vogais em Python

Este é um projeto simples desenvolvido em Python com o objetivo de contar a quantidade de vogais em uma string informada pelo usuário. É o meu primeiro projeto focado em lógica de programação e estou em constante evolução na área! 🚀

---

## 💡 Descrição do Projeto

A aplicação solicita ao usuário que insira uma palavra ou frase e, em seguida, calcula e exibe a quantidade de vogais presentes no texto. 

Este projeto tem como objetivo reforçar conceitos básicos de:

- Estruturas de repetição (`for`)
- Condicionais (`if`)
- Conjuntos (`set`)
- Manipulação de strings
- Funções em Python

---

## 🛠️ Tecnologias Utilizadas

- Python 3.x

---

## 📄 Código Principal

```python
def conta_vogais(texto):
    # Define um conjunto de vogais (maiúsculas e minúsculas)
    vogais = set('aeiouAEIOU')
    
    # Inicializa o contador
    contador = 0

    # Itera pelos caracteres do texto
    for char in texto:
        # Verifica se o caractere é uma vogal
        if char in vogais:
            contador += 1
    
    return contador
```
# Solicita a entrada do usuário
texto = input("Digite a Palavra: ")

# Chama a função e exibe o resultado
resultado = conta_vogais(texto)
print(f"O número de vogais na string '{texto}' é: {resultado}")

🚀 Como Executar

1- Certifique-se de ter o Python instalado na sua máquina.

2- Copie o código acima para um arquivo com a extensão .py, por exemplo: conta_vogais.py.

3- Execute o script via terminal ou prompt de comando:

```bash
python conta_vogais.py
```
4- Insira a palavra ou frase desejada quando solicitado.

## 🎯 Objetivos de Aprendizado

✅ Praticar a criação de funções
✅ Trabalhar com estruturas de controle e conjuntos
✅ Aprender boas práticas na escrita de código

## 📄 Licença

Este projeto é livre para uso pessoal e educacional, Faz Parte do Projeto [Estudos Python](https://github.com/ei-Gih/Estudos_Python), cofira os outros.

##  ✨ Contribuição
Esse é o meu primeiro projeto na área de programação e estou sempre buscando melhorar! Feedbacks e sugestões são muito bem-vindos. 🚀


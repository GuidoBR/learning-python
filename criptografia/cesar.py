import string


def cesar(frase, encripta):
    alfabeto = string.ascii_uppercase
    saida = ""

    for letra in frase:
        if encripta:
            busca = alfabeto.find(letra) + 3
        else:
            busca = alfabeto.find(letra) - 3
        modulo = busca % 26
        saida += str(alfabeto[modulo])

    return saida


entrada = input('Informe o texto a ser criptografado: ')
print(cesar(entrada.upper(), True))

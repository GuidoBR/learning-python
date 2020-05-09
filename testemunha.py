import random

suspeitos = ["Charles B. Abbage", "Donald Duck Knuth", "Ada L. Ovelace", "Alan T. Uring", "Ivar J. Acobson", "Ras Mus Ler Dorf"]
locais = ["Redmond", "Palo Alto", "San Francisco", "Tokio", "Restaurante no Fim do Universo", "São Paulo", "Cupertino", "Helsinki", "Maida Vale", "Toronto"]
armas = ["Peixeira", "DynaTAC 8000X (o primeiro aparelho celular do mundo)", "Trezoitão", "Trebuchet", "Maça", "Gládio"]

armas_id = [num for num in range(len(armas))]
suspeitos_id = [num for num in range(len(suspeitos))]
locais_id = [num for num in range(len(locais))]

"""
Gera uma lista com um número para um suspeito, um para o local, e um para a arma
Pode ser usado para gerar o assassinato e pra gerar uma teoria
"""
def gerar_aleatorio():
    return [suspeitos_id[random.randint(0, len(suspeitos_id) - 1)],
            locais_id[random.randint(0, len(locais_id) - 1)], 
            armas_id[random.randint(0, len(armas_id) - 1)]]

def testemunha(teoria, resposta):

    if (teoria[0] != resposta[0]) and (teoria[1] != resposta[1]) and (teoria[2] != resposta[2]):
        retornos = [1, 2, 3]

    if (teoria[0] != resposta[0]) and (teoria[1] != resposta[1]):
        retornos = [1, 2]

    if (teoria[0] != resposta[0]) and (teoria[2] != resposta[2]):
        retornos = [1, 3]
        return retornos[random.randint(0, len(retornos) - 1)]

    if (teoria[1] != resposta[1]) and (teoria[2] != resposta[2]):
        retornos = [2, 3]
        return retornos[random.randint(0, len(retornos) - 1)]

    if teoria[0] != resposta[0]:
        retornos = [1]

    if teoria[1] != resposta[1]:
        retornos = [2] 

    if teoria[2] != resposta[2]:
        retornos = [3]

    if teoria == resposta:
        retornos = [0]

    return retornos[random.randint(0, len(retornos) - 1)]

def investigacao(resultado):
    resposta = -1

    while resposta != 0:
        teoria = gerar_aleatorio()
        print(f"Teoria: {teoria}")
        resposta = testemunha(teoria, resultado)
        print(f"Resposta da testemunha: {resposta}")

        if (resposta == 1):
            suspeitos_id.remove(teoria[0])
        if (resposta == 2):
            locais_id.remove(teoria[1])
        if (resposta == 3):
            armas_id.remove(teoria[2])



if __name__ == "__main__":
    assassinato = gerar_aleatorio()
    investigacao(assassinato)



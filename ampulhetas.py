"""
Recebe um valor de preparo do miojo, e os tempos de duas ampulhetas

Retorna o tempo mínimo necessário para o miojo ficar pronto, ou se não é possível cozinhar
no tempo exato com as ampulhetas disponíveis

>>> miojo(3, 3, 7)
3
>>> miojo(3, 5, 7)
10
>>> miojo(3, 7, 11)
14
>>> miojo(6, 8, 10)
16
>>> miojo(3, 1, 2)
'Erro: valores das ampulhetas devem ser maiores do que o tempo de preparo'
>>> miojo(3, 9, 7)
'Impossível cozinhar no tempo exato com ampulhetas disponíveis'
>>> miojo(3, 5, 6)
'Impossível cozinhar no tempo exato com ampulhetas disponíveis'
>>> miojo(3, 4, 7)
'Impossível cozinhar no tempo exato com ampulhetas disponíveis'
"""
def miojo(tempo, amp1, amp2):
    if (amp1 == tempo) or (amp2 == tempo):
        return tempo
    if min(amp1, amp2, tempo) != tempo:
        return "Erro: valores das ampulhetas devem ser maiores do que o tempo de preparo"

    tempoTotal = tempo + max(amp1, amp2)
    numeroVoltas = tempoTotal / min(amp1, amp2)

    if (numeroVoltas.is_integer()):
        return tempoTotal
    else:
        return "Impossível cozinhar no tempo exato com ampulhetas disponíveis"


if __name__ == "__main__":
    import doctest
    doctest.testmod()

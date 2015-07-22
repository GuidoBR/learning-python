def is_anagram(word1, word2):
    """
    Retorna true se duas strings são anagramas
    (ignora espaços e é case-insensitive)
    >>> is_anagram('The Alias Men', 'Alan Smithee')
    True
    >>> is_anagram('The Alias Men', 'Guido Luz Percu')
    False
    >>> is_anagram('Amor', 'Roma')
    True
    >>> is_anagram('Amor', 'o Mar')
    True
    >>> is_anagram('Amor', 'o Ar!')
    False
    """
    list1 = sorted(list(word1.upper().replace(" ", "")))
    list2 = sorted(list(word2.upper().replace(" ", "")))

    return list1 == list2

if __name__ == '__main__':
    import doctest
    doctest.testmod()

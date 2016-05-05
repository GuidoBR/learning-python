def fizzbuzz(numero):
    """
    Função fizzbuzz
    - Retorna 'Fizz' quando a entrada é um múltiplo de 3.
    - Retorna 'Buzz' quando a entrada é um múltiplo de 5.
    - Retorna 'FizzBuzz' quando a entrada é múltipla de 3 e 5.

    >>> print(fizzbuzz(-1))
    None
    >>> print(fizzbuzz(1))
    None
    >>> print(fizzbuzz(3))
    Fizz
    >>> print(fizzbuzz(5))
    Buzz
    >>> print(fizzbuzz(6))
    Fizz
    >>> print(fizzbuzz(7))
    None
    >>> print(fizzbuzz(15))
    FizzBuzz
    >>> print(fizzbuzz(30))
    FizzBuzz
    """
    if (numero % 3 == 0 and numero % 5 == 0):
        return 'FizzBuzz'
    if (numero % 3 == 0):
        return 'Fizz'
    if (numero % 5 == 0):
        return 'Buzz'

def better_fizzbuzz(number):
    """
    Based on: https://medium.com/@sbichenko/the-wrong-fizzbuzz-81cb8e67ef4a
    Função fizzbuzz
    - Retorna 'Fizz' quando a entrada é um múltiplo de 3.
    - Retorna 'Buzz' quando a entrada é um múltiplo de 5.
    - Retorna 'FizzBuzz' quando a entrada é múltipla de 3 e 5.

    >>> print(better_fizzbuzz(-1))
    None
    >>> print(better_fizzbuzz(1))
    None
    >>> print(better_fizzbuzz(3))
    Fizz
    >>> print(better_fizzbuzz(5))
    Buzz
    >>> print(better_fizzbuzz(6))
    Fizz
    >>> print(better_fizzbuzz(7))
    None
    >>> print(better_fizzbuzz(15))
    FizzBuzz
    >>> print(better_fizzbuzz(30))
    FizzBuzz
    """
    def better_fizzbuzz(number):
        text = '';
        if number % 3 == 0:
            text += 'Fizz'
        elif number % 5 == 0:
            text += 'Buzz'
        return text

if __name__ == "__main__":
    import doctest
    doctest.testmod()

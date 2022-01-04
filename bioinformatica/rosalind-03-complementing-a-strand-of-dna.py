import doctest


def reverse_complement(dna_string):
    """
    Problem

    In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

    The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

    Given: A DNA string s

    of length at most 1000 bp.

    Return: The reverse complement sc of s
    >>> reverse_complement('AAAACCCGGT')
    'ACCGGGTTTT'
    >>> reverse_complement('GATTACA')
    'TGTAATC'
    """
    return dna_string.replace('A', 't').replace('T', 'a').replace('C', 'g').replace('G', 'c').upper()[::-1]

if __name__ == "__main__":
    doctest.testmod()

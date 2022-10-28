import doctest


def reverse_complement(dna_string):
    """
    Find the Reverse Complement of a String
    https://rosalind.info/problems/ba1c/

    Given: A DNA string Pattern.
    Return: Pattern, the reverse complement of Pattern.
    >>> reverse_complement('AAAACCCGGT')
    'ACCGGGTTTT'
    """
    reverse = dna_string[::-1]
    dna_translate = {'A': 'T', 'C': 'G', 'T': 'A', 'G': 'C'}
    complement = ''
    for nucleotide in reverse:
        complement += dna_translate[nucleotide]
        
    return complement


if __name__ == '__main__':
    doctest.testmod()

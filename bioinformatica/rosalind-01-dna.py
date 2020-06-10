import doctest


def letters_count(dna_string):
    """
    A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; the length of a string is the number of symbols that it contains.

    An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

    Given: A DNA string dna_string

    of length at most 1000 nt.

    Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in dna_string

    >>> letters_count("AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC")
    '20 12 17 21'
    """
    return f"{dna_string.count('A')} {dna_string.count('C')} {dna_string.count('G')} {dna_string.count('T')}"

if __name__ == "__main__":
    doctest.testmod()
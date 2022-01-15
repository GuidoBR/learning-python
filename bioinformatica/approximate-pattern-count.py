import doctest


def hamming_distance(s1, s2):
    """
    >>> hamming_distance('ACGT', 'ACGTB')
    -1
    >>> hamming_distance('ACGT', 'ACGU')
    1
    >>> hamming_distance('GGGCCGTTGGT', 'GGACCGTTGAC')
    3
    >>> hamming_distance('CAGAAAGGAAGGTCCCCATACACCGACGCACCAGTTTA', 'CACGCCGTATGCATAAACGAGCCGCACGAACCAGAGAG')
    23
    >>> hamming_distance('TGACCCGTTATGCTCGAGTTCGGTCAGAGCGTCATTGCGAGTAGTCGTTTGCTTTCTCAAACTCC', 'GAGCGATTAAGCGTGACAGCCCCAGGGAACCCACAAAACGTGATCGCAGTCCATCCGATCATACA')
    50
    """
    if len(s1) == len(s2):
        return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))

    return -1

def approximate_pattern_count(text, pattern, d):
    """
    Computing COUNTd(Text, Pattern) simply requires us to compute the Hamming distance between Pattern and every k-mer substring of Text, as follows.

    >>> approximate_pattern_count('AACAAGCATAAACATTAAAGAG', 'AAAAA', 2)
    17
    >>> approximate_pattern_count('ATGCCATTCGCATTGTCCCAGTGA', 'CCC', 2)
    20
    >>> approximate_pattern_count('CATGCCATTCGCATTGTCCCAGTGA', 'CCC', 2)
    """
    count = 0
    for i in range(len(text) - len(pattern)):
        new_pattern = text[i: len(pattern)]
        if hamming_distance(pattern, new_pattern) < d:
            count += 1
    return count

if __name__ == '__main__':
    doctest.testmod()

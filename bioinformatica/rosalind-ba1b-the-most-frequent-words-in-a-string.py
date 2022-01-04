import doctest
import collections

from itertools import islice


def unique_list(array):
    return list(dict.fromkeys(sorted(array)))

def sliding_window(string, integer):
    """
    >>> sliding_window("ACTG", 2)
    ['AC', 'CT', 'TG']
    >>> sliding_window("ACGTTGCATGTCGCATGATGCATGAGAGCT", 4)
    ['ACGT', 'AGAG', 'AGCT', 'ATGA', 'ATGC', 'ATGT', 'CATG', 'CGCA', 'CGTT', 'GAGA', 'GAGC', 'GATG', 'GCAT', 'GTCG', 'GTTG', 'TCGC', 'TGAG', 'TGAT', 'TGCA', 'TGTC', 'TTGC']
    """
    windows = []
    for position, letter in enumerate(string):
        window = (string[position: position + integer])
        windows.append(window)

        if (position + integer) >= len(string):
            break

    return unique_list(windows)


def most_frequent_kmers(dna_string, k):
    """
    We say that Pattern is a most frequent k-mer in Text if it maximizes Count(Text, Pattern) among all k-mers. For example, "ACTAT" is a most frequent 5-mer in "ACAACTATGCATCACTATCGGGAACTATCCT", and "ATA" is a most frequent 3-mer of "CGATATATCCATAG".

    Frequent Words Problem
    Find the most frequent k-mers in a string.

    Given: A DNA string Text and an integer k.
    Return: All most frequent k-mers in Text (in any order).


    >>> most_frequent_kmers("ACGTTGCATGTCGCATGATGCATGAGAGCT", 4)
    'CATG GCAT'
    >>> most_frequent_kmers("TAAACGTGAGAGAAACGTGCTGATTACACTTGTTCGTGTGGTAT", 3)
    'CGT GTG'
    """
    all_kmers = sliding_window(dna_string, k)
    max_kmer_value = 0
    max_kmer = []
    for kmer in all_kmers:
        kmer_count = dna_string.count(str(kmer))
        if kmer_count > max_kmer_value:
            max_kmer_value = kmer_count
            max_kmer = [str(kmer)]
        if kmer_count == max_kmer_value:
            max_kmer.append(str(kmer))

    return " ".join(unique_list(max_kmer))

if __name__ == "__main__":
    doctest.testmod()

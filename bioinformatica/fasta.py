from Bio import SeqIO

for i in SeqIO.parse('teste.fasta', 'fasta'):
    print(i.id)
    print(i.seq)

from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

sequencia = 'ACTCCACTG'

s = Seq(sequencia, IUPAC.unambiguous_dna)
complementar = s.complement()
reverso_complementar = s.reverse_complement()

rna = s.transcribe()
proteina = s.translate()

print("DNA: {} | RNA: {} | Proteina: {} \nComplemento: {} | Complemento Reverso: {}".format(s, rna, proteina, complementar, reverso_complementar))

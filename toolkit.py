#  step 1 : count  nucleotides  in  a  DNA 
dna   =    "ATGCGGTACGTTAGCACGT"
count_A = dna.count("A")
count_T = dna.count("T")
count_G = dna.count("G")
count_C = dna.count("C")

print("A:", count_A)
print("T:", count_T)
print("G:", count_G)
print("C:", count_C)

# step 2 : GC content
length = len(dna)
gc_count = count_G + count_C
gc_content = (gc_count / length) * 100
print("Length:", length)
print("GC content:", gc_content, "%")

# step 3 : transcription (DNA -> RNA)
rna = dna.replace("T","U")
print("RNA:", rna)

# step 4 : reverse complement 
complement_map = {"A": "T","T": "A", "G": "C", "C": "G"}
complement = ""
for base in dna:
    complement = ""
    for base in dna:
        complement = complement + complement_map[base]

reverse_complement = complement[::-1]

print("complement:",  complement)
print("Reverse complement:", reverse_complement)

# step 5 : translation (DNA -> protein)
codon_table = {
    "TTT": "F", "TTC": "F", "TTA": "L", "TTG": "L",
    "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L",
    "ATT": "I", "ATC": "I", "ATA": "I", "ATG": "M",
    "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V",
    "TCT": "S", "TCC": "S", "TCA": "S", "TCG": "S",
    "CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "TAT": "Y", "TAC": "Y", "TAA": "*", "TAG": "*",
    "CAT": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
    "AAT": "N", "AAC": "N", "AAA": "K", "AAG": "K",
    "GAT": "D", "GAC": "D", "GAA": "E", "GAG": "E",
    "TGT": "C", "TGC": "C", "TGA": "*", "TGG": "W",
    "CGT": "R", "CGC": "R", "CGA": "R", "CGG": "R",
    "AGT": "S", "AGC": "S", "AGA": "R", "AGG": "R",
    "GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G",
}

protein = ""
for i in range(0, len(dna) - 2, 3):
    codon = dna[i:i+3]
    protein = protein + codon_table[codon]

print("Protein:", protein)
# expand single-letter codes to full amino acid names
aa_names = {
    "A": "Alanine", "R": "Arginine", "N": "Asparagine", "D": "Aspartate",
    "C": "Cysteine", "E": "Glutamate", "Q": "Glutamine", "G": "Glycine",
    "H": "Histidine", "I": "Isoleucine", "L": "Leucine", "K": "Lysine",
    "M": "Methionine", "F": "Phenylalanine", "P": "Proline", "S": "Serine",
    "T": "Threonine", "W": "Tryptophan", "Y": "Tyrosine", "V": "Valine",
    "*": "STOP",
}

print("Protein (full names):")
for letter in protein:
    print("  ", letter, "->", aa_names[letter])

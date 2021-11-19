"""
Student: Nimrod Machlav
ID: 315230185
Assignment no. 3
Program: genes.py
"""


def next_gene(i, s):
    s = str(s[i:])
    gene_start = s.find("ATG")
    if gene_start == -1:
        return None, None
    j = 0
    for j in range(gene_start, len(s), 3):
        if s[j:j + 3] == "TAA" or s[j:j + 3] == "TAG" or s[j:j + 3] == "TGA":
            break
    return i + gene_start, i + j + 3


def get_genes(s):
    genes = []
    first_index, last_index = next_gene(0, s)
    while first_index is not None:
        genes.append(s[first_index:last_index])
        first_index, last_index = next_gene(last_index + 1, s)
    return genes


def gene_to_protein(gene):
    gene_text = ""
    for i in range(0, len(gene) - 3, 3):
        gene_text += symbols_by_codons[gene[i: i + 3]]
    return gene_text


def get_proteins(genes):
    amino_acids = []
    for gene in genes:
        amino_acids.append(gene_to_protein(gene))
    return amino_acids


def main():
    file_name = input("Type file name to translate: ")
    with open(file_name + ".txt") as f:
        text = f.read()
        genes = get_genes(text)
        proteins = get_proteins(genes)
        print("Found", len(proteins), "genes")
        with open(file_name + "_proteins.txt", "w") as output:
            for protein in proteins:
                output.write(protein + "\n")


if __name__ == '__main__':
    main()

symbols_by_codons = {
    "GCT": "A",
    "GCC": "A",
    "GCA": "A",
    "GCG": "A",
    "TGT": "C",
    "TGC": "C",
    "GAT": "D",
    "GAC": "D",
    "GAA": "E",
    "GAG": "E",
    "TTT": "F",
    "TTC": "F",
    "GGT": "G",
    "GGC": "G",
    "GGA": "G",
    "GGG": "G",
    "CAT": "H",
    "CAC": "H",
    "ATT": "I",
    "ATC": "I",
    "ATA": "I",
    "AAA": "K",
    "AAG": "K",
    "CTT": "L",
    "CTC": "L",
    "CTA": "L",
    "CTG": "L",
    "TTA": "L",
    "TTG": "L",
    "ATG": "M",
    "AAT": "N",
    "AAC": "N",
    "CCT": "P",
    "CCC": "P",
    "CCA": "P",
    "CCG": "P",
    "CAA": "Q",
    "CAG": "Q",
    "CGT": "R",
    "CGC": "R",
    "CGA": "R",
    "CGG": "R",
    "AGA": "R",
    "AGG": "R",
    "TCT": "S",
    "TCC": "S",
    "TCA": "S",
    "TCG": "S",
    "AGT": "S",
    "AGC": "S",
    "ACT": "T",
    "ACC": "T",
    "ACA": "T",
    "ACG": "T",
    "GTT": "V",
    "GTC": "V",
    "GTA": "V",
    "GTG": "V",
    "TGG": "W",
    "TAC": "Y",
    "TAT": "Y",
}

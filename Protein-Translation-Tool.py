def transcription (cDNA):
    if cDNA=='A':
        return "U"
    elif cDNA=="C":
        return "G"
    elif cDNA=="G":
        return "C"
    elif cDNA=="T":
        return "A"
    else:
        return "*"
        
def codon_conversion (mRNA):
    codon=[]
    for i in range(0,len(mRNA),3):
        codon.append(mRNA[i:i+3])
    return codon

def translation(codon):
    # Convert the codon into corresponding amino acid if it matches any of the codons in the dictionary
    for amino_acid, codons in AminoAcid_dict.items():
        if codon in codons:
            return amino_acid
    return None  # Return None if no matching codon is found
    
#Convert all form in mRNA      
info=input("Type of nucleic acid: ")
if info=="cDNA":
    mRNA=[]
    cDNA=input("cDNA sequence: ")
    i=0
    for nucleotide in cDNA:
        mRNA.append(transcription(nucleotide))
elif info=="mRNA":
    mRNA=input("mRNA sequence: ")
    mRNA=list(mRNA)
else:
    print("Error")
    
#Judgement of mRNA
for nucleotide in mRNA:
    if nucleotide=="T" or nucleotide =="*":
        print("Error in producing mRNA")
        break
else:
    mRNA="".join(mRNA)

mRNA=codon_conversion(mRNA)
print(f'mRNA: {mRNA}')

#Amino Acid list
AminoAcid_dict={
    'A': ['GCG','GCA','GCC','GCU'],
    'C': ['UGC','UGU',],
    'D': ['GAC','GAU'],
    'E': ['GAG','GAA'],
    'F': ['UUC','UUU'],
    'G': ['GGG','GGA','GGC','GGU'],
    'H': ['CAC','CAU'],
    'I': ['AUA','AUC','AUU'],
    'K': ['AAG','AAA'],
    'L': ['UUG','UUA','CUG','CUA','CUC','CUU'],
    'M': ['AUG'],
    'N': ['AAC','AAU'],
    'P': ['CCG','CCA','CCC','CCU'],
    'Q': ['CAG','CCA'],
    'R': ['CCG','CGA','CGC','CGU','AGG','AGA'],
    'S': ['UCG','UCA','UCC','UCU','AGC','AGU'],
    'T': ['ACG','ACA','ACC','ACU'],
    'V': ['GUG','GUA','GUG','GUU'],
    'W': ['UGG'],
    'Y': ['UAC','UAU'],
    '$': ['UAA','UAG','UGA'],
}

#translation
polypeptide = []
for codon in mRNA:
    amino_acid = translation(codon)
    if amino_acid == "$":  # Stop codon
        break
    elif amino_acid is not None:
        polypeptide.append(amino_acid)

polypeptide=str(''.join(polypeptide
                       ))
print(f'Polypeptide: {polypeptide}')

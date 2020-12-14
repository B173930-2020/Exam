# judge DNA fasta or protein fasta
def judge_dna_protein(input_path):
    names = []
    seqs = []

    for i in SeqIO.parse(input_path, "fasta"):
        names.append(i.name)
        seqs.append(str(i.seq))

    if len(set(seqs[0])) > 5:
        result = 'prot'
    else:
        result = 'nucl'
    return result

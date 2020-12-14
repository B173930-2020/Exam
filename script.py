from Bio import SeqIO
import os

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

# judge blast class
def judge_blast(input_class, database_class):
    if input_class == 'prot':
        if database_class == 'prot':
            result = 'blastp'
        else:
            result = 'tblastn'
    else:
        if database_class == 'prot':
            result = 'blastx'
        else:
            result = 'blastn'
    
    return result

# user input
input_path = str(input("please input the sequence file name (used to blast):\n"))
database_path = str(input("please input your sequene (used to make a database) file's name or path here:\n"))
database_file_name = str(input("please input the database name you wanted:\n"))
output_file_name = str(input("what name of the output file do you want:\n"))

# get dna or protein fasta
input_class = judge_dna_protein(input_path)
database_class = judge_dna_protein(database_path)

# get blast class
blast = judge_blast(input_class, database_class)

# make blast database
os.system(f'makeblastdb -in {database_path} -input_type fasta -dbtype {database_class} -title {database_file_name} -out {database_file_name}')

# blast
os.system(f'{blast} -query {input_path} -db {database_file_name} -out {output_file_name}')


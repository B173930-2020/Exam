from Bio import SeqIO
import os

# judge DNA fasta or protein fasta
def judge_dna_protein(input_path):
    names = []
    seqs = []

    # use biopython to search whether there are more than ACTGN 5 bases
    for i in SeqIO.parse(input_path, "fasta"):
        names.append(i.name)
        seqs.append(str(i.seq))

    if len(set(seqs[0])) > 5:
        print('Protein sequence(s)!')
        result = 'prot'
    else:
        print('DNA sequence(s)')
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

# user input the sequences files, database name and output name
input_path = str(input("please input the blast file name:\n"))
database_path = str(input("please input your sequene (used to make a database) file's name or path here:\n"))
database_name = str(input("please input the database name you wanted:\n"))
output_name = str(input("what name of the output file do you want:\n"))

# call the function and get dna or protein fasta
input_class = judge_dna_protein(input_path)
database_class = judge_dna_protein(database_path)

# call the function and get blast class
blast = judge_blast(input_class, database_class)

# make blast database
os.system(f'makeblastdb -in {database_path} -input_type fasta -dbtype {database_class} -title {database_name} -out {database_name}')

# blast
os.system(f'{blast} -query {input_path} -db {database_name} -out {output_name}')

# use a while loop to make the code repeatably
while True:
    answer = str(input('Do you want to continue blast other sequences?: y/n?'))
    if answer == 'y':
        os.system('python3 script.py')
    elif answer == 'n':
        exit()
    else:
        print('Please input the right choices!')
        continue

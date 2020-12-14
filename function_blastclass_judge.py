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


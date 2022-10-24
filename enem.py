import pandas as pd


def select_column(file,
                  cols=('SG_UF_PROVA', 'NU_NOTA_REDACAO'),
                  chunksize=100000):

    reader = pd.read_csv(file,
                         sep=';',
                         encoding="ISO-8859-1",
                         chunksize=chunksize,
                         usecols=cols)
    for chunk in reader:
        yield chunk

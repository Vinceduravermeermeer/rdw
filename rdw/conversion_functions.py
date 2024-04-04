import pandas


def convert_list_to_df(items_list):
    '''
    Converts the list of dictionaries to a pandas DataFrame
    '''

    # convert
    df = pandas.DataFrame(items_list)

    # specify the columns
    columns = ['kenteken', 'merk', 'handelsbenaming', 'catalogusprijs', 'eerste_kleur', 'datum_tenaamstelling']

    # filter the DataFrame for only the specified columns
    df_filtered = df[columns]
    
    return df_filtered
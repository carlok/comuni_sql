import pandas as pd

def pandas_sql(df, table_name, sql_fields, pandas_fields):
    sql_str = "INSERT INTO {} ({}) VALUES\n".format(table_name, ', '.join(sql_fields))

    for idx, row in df.iterrows():
        sql_str += '({}, "{}"'.format(row[pandas_fields[0]], row[pandas_fields[1]])
        if len(pandas_fields) == 3:
            sql_str += ', {}'.format(row[pandas_fields[2]])
        sql_str += ')'

        if idx == df.index[-1]:
            sql_str += ';\n'
        else:
            sql_str += ',\n'

    return sql_str

def pandas_unique(df, columns):
    return df.groupby(columns).size().reset_index().rename(columns={0:'count'})

df = pd.read_csv('./comuni.csv', sep=';', encoding='ISO-8859-1') # utf-8')
df.columns = [x.replace("\n", "") for x in df.columns.to_list()]

codici = {
    'regioni': ['Codice Regione', 'Denominazione Regione'],
    'province': [
        "Codice dell'Unità territoriale sovracomunale (valida a fini statistici)",
        "Denominazione dell'Unità territoriale sovracomunale (valida a fini statistici)",
        'Codice Regione'
    ],
    'comuni': [
        'Codice Comune formato numerico',
        'Denominazione (Italiana e straniera)',
        "Codice dell'Unità territoriale sovracomunale (valida a fini statistici)"
    ]
}

df_regioni = pandas_unique(df, codici['regioni'])
df_province = pandas_unique(df, codici['province'])
df_comuni = pandas_unique(df, codici['comuni'])

print(pandas_sql(df_regioni, 'regioni', ['id', 'nome'], codici['regioni']))
print(pandas_sql(df_province, 'province', ['id', 'nome', 'id_regione'], codici['province']))
print(pandas_sql(df_comuni, 'comuni', ['id', 'nome', 'id_provincia'], codici['comuni']))
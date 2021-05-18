import pandas as pd

df = pd.read_csv('data.csv')
#print(df.to_string())

list_of_column_names = list(df.columns)
print(list_of_column_names)

#for i in list_of_column_names:
     #print(type(df[i][0]))

#print(type(df['Pulse'][0]))
col_type = df.dtypes
print(dict(col_type))

print(df.dtypes)
print(type(df.dtypes))


obj_type = 'csv'
obj_header = 'True'
obj_separtor = ','
obj_location = 'data.csv'

def column_names(object_type,object_header,object_separator,object_location):
    df = pd.read_csv(obj_location)
    list_of_column_names = list(df.columns)

    col_type = dict(df.dtypes)

    return list_of_column_names, col_type

print(column_names(obj_type,obj_header,obj_separtor,obj_location))
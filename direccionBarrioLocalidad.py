import pandas as pd

# cargar data2.csv como un DataFrame
df = pd.read_csv('data2.csv')

'''
Funcion para extraer la columna location del dataframe
retornar una lista con los valores de la columna
'''
def get_location(df):
    return df['location'].tolist()

'''
Funcion que reciba la lista de get_location
y retorne una lista de lista con los valores de split
'''
def split_location(location):
    # lista de listas
    lista = []
    for i in location:
        # split por coma
        lista.append(i.split(','))
    return lista

'''
Funcion que reciba la lista de listas de split_location
recorra cada elemento de la lista interna y si coincide con ' UPZ' extraiga el valor y lo guarde en una lista nueva
llamada UPZ. Si no se encuentra el valor ' UPZ' en la lista interna, guarde el valor 'No UPZ' en la lista UPZ
retornar la lista UPZ
'''
def get_upz(lista):
    # lista de UPZ
    upz = []
    for i in lista:
        for j in i:
            if ' UPZ' in j:
                upz.append(j)
                break
        else:
            upz.append('No UPZ')
    return upz

'''
Funcion que reciba la lista de listas de split_location
recorra cada elemento de la lista interna y si coincide con ' Localidad' extraiga el valor y lo guarde en una lista nueva
llamada Localidad. Si no se encuentra el valor ' Localidad' en la lista interna, guarde el valor 'No Localidad' en la lista UPZ
retornar la lista Localidad
'''
def get_localidad(lista):
    # lista de Localidad
    localidad = []
    for i in lista:
        for j in i:
            if ' Localidad' in j:
                localidad.append(j)
                break
        else:
            localidad.append('No Localidad')
    return localidad
def main():
    # obtener la columna location del dataframe
    location = get_location(df)

    # obtener la lista de listas
    lista = split_location(location)


    # obtener la lista de UPZ
    upz = get_upz(lista)

    # obtener la lista de Localidad
    localidad = get_localidad(lista)

    # aregar las listas upz y localidad al dataframe
    df['UPZ'] = upz
    df['Localidad'] = localidad
    print(df.head())

    # guardar el dataframe como un archivo csv
    df.to_csv('data3.csv', index=False)

if __name__ == '__main__':
    main()

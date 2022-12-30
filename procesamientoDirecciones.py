import re
import pandas as pd

# cargamos el dataframe
df = pd.read_csv('Phidias_Address.csv')
# Funcion para separar un numero de una letra
def split_number_letter(lista):
    for i in range(len(lista)):
        if re.search(r'\d+[A-Z]', lista[i]):
            lista[i] = re.sub(r'(\d+)([A-Z])', r'\1 \2', lista[i])
    return lista

# Funcion para extraer la columna 'Dirección' del dataframe
def get_address(df):
    address = []
    for i in df['Dirección']:
        address.append(i)
    return address

# Funcion para dividir el string de la direccion en una lista
def split_address(address):
    direcciones_split = []
    for i in address:
        direcciones_split.append(i.split())
    return direcciones_split

# Funcion para reemplazar las palabras de la direccion
def replace_address(direcciones_split):
    for i in direcciones_split:
        if i[0] == 'AC':
            i[0] = 'Avenida Calle'
        elif i[0] == 'AK':
            i[0] = 'Avenida Carrera'
        elif i[0] == 'Ak':
            i[0] = 'Avenida Carrera'
        elif i[0] == 'AV':
            i[0] = 'Avenida'
        elif i[0] == 'Av':
            i[0] = 'Avenida'
        elif i[0] == 'CL':
            i[0] = 'Calle'
        elif i[0] == 'Cl':
            i[0] = 'Calle'
        elif i[0] == 'Cll':
            i[0] = 'Calle'
        elif i[0] == 'CR':
            i[0] = 'Carrera'
        elif i[0] == 'Cr':
            i[0] = 'Carrera'
        elif i[0] == 'Cra':
            i[0] = 'Carrera'
        elif i[0] == 'Kr':
            i[0] = 'Carrera'
        elif i[0] == 'DG':
            i[0] = 'Diagonal'
        elif i[0] == 'TV':
            i[0] = 'Transversal'
        elif i[0] == 'Tv':
            i[0] = 'Transversal'
        else:
            i[0] = '*'
    return direcciones_split

# Funcion que retorna el indice del segundo numero de la lista interna
def get_second_number_index(lista):
    index = []
    for i in range(len(lista)):
        if lista[i].isdigit():
            index.append(i)
    return index[1]

# Funcion que agrega #
def add_number(direcciones_split):
    for i in direcciones_split:
        if i[0] != '*':
            try:
                i.insert(get_second_number_index(i), '#')
            except IndexError:
                pass
    return direcciones_split

# Funcion que retorna el indice del tercer numero de la lista interna
def get_third_number_index(lista):
    index = []
    for i in range(len(lista)):
        if lista[i].isdigit():
            index.append(i)
    return index[2]

# funcion que agrega '-'
def add_number2(direcciones_split):
    for i in direcciones_split:
        if i[0] != '*':
            try:
                i.insert(get_third_number_index(i), '-')
            except IndexError:
                pass
    return direcciones_split


# Funcion que elimina las palabras innecesarias de la direccion
def delete_after_third_number(direcciones_split):
    for i in direcciones_split:
        if i[0] == '*':
            i[i.index('*'):] = ['Fuera de Bogota']
        else:
            try:
                del i[get_third_number_index(i)+1:]
            except IndexError:
                pass

    return direcciones_split

# Funcion para concatenar los elementos de la lista interna
def concatenate_list(direcciones_split):
    direcciones = []
    for i in direcciones_split:
        direcciones.append(' '.join(i))
    return direcciones

# Funcion que agrega la ciudad y pais a la direccion
def add_text(direcciones):
    for i in range(len(direcciones)):
        direcciones[i] = direcciones[i] + ', Bogotá, Colombia'
    return direcciones

# Funcion que agrega la columna 'Dirección' al dataframe
def add_column(direcciones):
    df['Direcciones'] = direcciones
    df.to_csv('Direcciones.csv', index=False)
    return df

def main():
    address = get_address(df)
    address_split = split_number_letter(address)
    address_split = split_address(address_split)
    address_split = replace_address(address_split)
    address_split = add_number(address_split)
    address_split = add_number2(address_split)
    address_split = delete_after_third_number(address_split)
    address = concatenate_list(address_split)
    address = add_text(address)
    data = add_column(address)
    data.to_csv('data1.csv', index=False)

if __name__ == '__main__':
    main()

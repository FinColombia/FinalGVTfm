import pandas as pd
#xxxxxxxxxxx

df = pd.read_csv('data3.csv')

# Extraer la columna 'Profesión' y guardarla en una lista nueva
def get_profesion():
    profesion = []
    for i in df['Profesión']:
        profesion.append(i)
    return profesion


'''
Funcion que reciba la lista de get_profesion
y convierta todo a minusculas
retorne la lista con los valores en minusculas
si no se puede convertir, retorne el valor original

'''
def get_profesion_lower(profesion):
    profesion_lower = []
    for i in profesion:
        try:
            profesion_lower.append(i.lower())
        except:
            profesion_lower.append(i)
    return profesion_lower

'''
Funcion que reciba la lista de get_profesion_lower
y retorne una lista con los valores reemplazados siguiente las siguientes indicaciones:
# Si el valor es nan o float se reemplaza por 'No especificado'
# Si empieza por 'ing' o 'arq' se reemplaza por 'Ingenierias y Arquitecturas'
# Si empieza por 'cir', 'med' o 'psic' se reemplaza por 'Ciencias de la Salud'
# Si empieza por 'educ' se reemplaza por 'Educacion'
# Si empieza por 'adm', 'fin', 'cont' o 'econ' se reemplaza por 'Administracion y Economia'
# Si empieza por 'abog' se reemplaza por 'Derecho'
# Si empieza por 'com' o 'pub' se reemplaza por 'Comunicacion y Publicidad'
# Si empieza por 'qui', 'mat', 'fis', 'bio', 'geo', 'inf' o 'est' se reemplaza por 'Ciencias Exactas'
# Si empieza por 'soc', 'ant', 'his', 'pol', 'fil' o 'tur' se reemplaza por 'Ciencias Sociales'
# Si empieza por 'art', 'mus', 'dib', 'fot', 'vid' o 'dis' se reemplaza por 'Artes y Diseño'
# Si empieza por otros valores se reemplaza por 'Otros'
'''

def get_profesion_replace(profesion):
    profesion_replace = []
    for i in profesion:
        if i == 'nan' or type(i) == float:
            profesion_replace.append('No especificado')
        elif i.startswith('ing') or i.startswith('arq'):
            profesion_replace.append('Ingenierias y Arquitecturas')
        elif i.startswith('cir') or i.startswith('med') or i.startswith('psic'):
            profesion_replace.append('Ciencias de la Salud')
        elif i.startswith('educ'):
            profesion_replace.append('Educacion')
        elif i.startswith('adm') or i.startswith('fin') or i.startswith('cont') or i.startswith('econ'):
            profesion_replace.append('Administracion y Economia')
        elif i.startswith('abog'):
            profesion_replace.append('Derecho')
        elif i.startswith('com') or i.startswith('pub'):
            profesion_replace.append('Comunicacion y Publicidad')
        elif i.startswith('qui') or i.startswith('mat') or i.startswith('fis') or i.startswith('bio') or i.startswith('geo') or i.startswith('inf') or i.startswith('est'):
            profesion_replace.append('Ciencias Exactas')
        elif i.startswith('soc') or i.startswith('ant') or i.startswith('his') or i.startswith('pol') or i.startswith('fil') or i.startswith('tur'):
            profesion_replace.append('Ciencias Sociales')
        elif i.startswith('art') or i.startswith('mus') or i.startswith('dib') or i.startswith('fot') or i.startswith('vid') or i.startswith('dis'):
            profesion_replace.append('Artes y Diseño')
        else:
            profesion_replace.append('Otros')
    return profesion_replace
def main():
    profesion = get_profesion()
    profesion_lower = get_profesion_lower(profesion)
    profesion_replace = get_profesion_replace(profesion_lower)

    # Agrega una columna Profesion 1 a df con los valores de profesion_replace
    df['Profesion 1'] = profesion_replace

    # Guardar el nuevo dataframe en un archivo csv
    df.to_csv('data4.csv', index=False)

if __name__ == '__main__':
    main()

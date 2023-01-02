import pandas as pd
import time
from geopy.exc import GeocoderTimedOut
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="FiyinK", timeout=10)
data = pd.read_csv('data1.csv')

def get_direcciones(data):
    direcciones = []
    for i in data['Direcciones']:
        direcciones.append(i)
    return direcciones

def get_lotes(direcciones):
    lotes = []
    for i in range(0, len(direcciones), 10):
        lotes.append(direcciones[i:i+10])
    return lotes

def get_geolocator(lotes):
    location = []
    numeroLote = 0
    count = 0
    for lote in lotes:
        # imprimir el numero de lote
        print(f'Lote {numeroLote}')
        numeroLote += 1
        for i in lote:
            try:
                locator = geolocator.geocode(i)
                if locator is not None:
                    location.append(locator.raw['display_name'])
                    print(count)
                    count += 1
                else:
                    location.append('None')
                    print('No se encontro la direccion')
                    print(count)
                    count += 1
            except GeocoderTimedOut:
                time.sleep(1)
                locator = geolocator.geocode(i)
                if locator is not None:
                    location.append(locator.raw['display_name'])
                    print(count)
                    count += 1
                else:
                    location.append('None')
                    print('No se encontro la direccion')
                    print(count)
                    count += 1
            print(location[count-1])
    return location

def add_column(location):
    data['location'] = location
    return data

def main():
    direcciones = get_direcciones()
    lotes = get_lotes(direcciones)
    location = get_geolocator(lotes)
    datos = add_column(location)
    datos.to_csv('data2.csv', index=False)

if __name__ == '__main__':
    main()

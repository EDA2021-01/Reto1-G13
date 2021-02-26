"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.DataStructures import singlelinkedlist as sl
from DISClib.DataStructures import arraylist as al
assert cf

default_limit = (1000)
sys.setrecursionlimit(default_limit*10)

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar la información sobre los videos")
    print("2- Consultar los 'n' videos con más vistas por país según categoría")
    print("3- Consultar los libros de un autor")
    print("4- Libros por género")
    print("0- Salir")

def initLinkedCatalog():
    """
    Inicializa el catalogo de libros
    """
    return controller.initLinkedCatalog()


def initArrayCatalog():
    """
    Inicializa el catalogo de libros
    """
    return controller.initArrayCatalog()


def loadData(catalog):
    """
    Carga los libros en la estructura de datos
    """
    controller.loadData(catalog)


def printTendencyVideosByCountry(list_of_videos):
    """
    Imprime los videos que se encontraron al buscar por cantidad de views, país de
    tendencia, y categoría de tendencia.
    """



catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        catalog_type = input("¿Con qué tipo de lista quiere trabajar?: ")
        print("Cargando información de los archivos ...\n")
        if catalog_type == 'Encadenada':
            catalog = initLinkedCatalog()
            loadData(catalog)
            first_video = sl.firstElement(catalog['videos'])
            print('Registros de videos cargados:', str(lt.size(catalog['videos'])), '\n')
            print('Primer registro de video cargado:\n')
            print('Título del vídeo:', first_video['title'], '\n',
            'Nombre del canal:', first_video['channel_title'], '\n',
            'Fecha de tendencia:', first_video['trending_date'], '\n',
            'País de tendencia:', first_video['country'], '\n',
            'Cantidad de vistas:', first_video['views'], '\n',
            'Cantidad de likes:', first_video['likes'], '\n',
            'Cantidad de dislikes:', first_video['dislikes'], '\n',)
            print('\nCatálogo de categorías: \n', catalog['categories'])
        elif catalog_type == 'Arreglo':
            catalog = initArrayCatalog()
            loadData(catalog)
            first_video = al.firstElement(catalog['videos'])
            print('Registros de videos cargados:', str(lt.size(catalog['videos'])), '\n')
            print(catalog['videos']['elements'][0])
            print('Primer registro de video cargado:\n')
            print('Título del vídeo:', first_video['title'], '\n',
            'Nombre del canal:', first_video['channel_title'], '\n',
            'Fecha de tendencia:', first_video['trending_date'], '\n',
            'País de tendencia:', first_video['country'], '\n',
            'Cantidad de vistas:', first_video['views'], '\n',
            'Cantidad de likes:', first_video['likes'], '\n',
            'Cantidad de dislikes:', first_video['dislikes'], '\n',)
            print('\nCatálogo de categorías: \n', catalog['categories']['elements'])
        
        
    elif int(inputs[0]) == 2:
        ammount = input("¿Cuántos videos quiere listar?: ")
        tendency_country = input("Ingrese el país a consultar: ")
        tendency_category = input("Ingrese la categoría a consultar: ")
        sort_type = input("¿Qué tipo de sort desea usar?: ")
        best_videos = controller.loadSortingByCountryAndCategory(catalog, ammount, tendency_country, tendency_category, sort_type)
        printTendencyVideosByCountry(best_videos)


    else:
        sys.exit(0)
sys.exit(0)

"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos


def newCatalog():
    """
    Inicializa el catálogo de videos. Crea una lista vacía para guardar
    todos los videos, y una lista vacía para las categorías de los mismos.
    
    """
    catalog = {'videos': None,
               'categories': None}

    catalog['videos'] = lt.newList('ARRAY_LIST',
                                cmpfunction=None)
    catalog['categories'] = lt.newList('ARRAY_LIST',
                                 cmpfunction=None)

    return catalog


# Funciones para agregar informacion al catalogo

def addVideo(catalog, video):
    # Se adiciona el libro a la lista de libros
    lt.addLast(catalog['videos'], video)


def addCategory(catalog, category):
    """
    Adiciona una categoría a la lista de categorías
    """
    lt.addLast(catalog['categories'], category)


# Funciones para creacion de datos

def newCategory(category_data):
    """
    Crea una nueva estructura para modelar los libros de
    un autor y su promedio de ratings
    """
    category = {'name': "", "videos": None,  "average_rating": 0}
    category['name'] = category_data['name']
    category['videos'] = lt.newList('ARRAY_LIST')
    return category


def newBookTag(tag_id, book_id):
    """
    Esta estructura crea una relación entre un tag y
    los libros que han sido marcados con dicho tag.
    """
    booktag = {'tag_id': tag_id, 'book_id': book_id}
    return booktag


# Funciones de consulta
def getViews(e):
    return e.get('views')

def sortByCountryAndCategory(catalog, ammount, tendency_country, ca_id):
    """
    Devuelve una lista con los videos con más vistas, según país de
    tendencia, y la categoría de tendencia.
    """
    video_list = catalog['videos']['elements']
    videos_by_country_and_category = []
    for video in video_list:
        if video['country'] == tendency_country:
            if video['category_id'] == ca_id:                
                videos_by_country_and_category.append(video)
    
    

# Funciones utilizadas para comparar elementos dentro de una lista

def compareCategoryName(catalog, category_name):
    """
    Entra el nombre de una categoría, y se consigue su ID.
    """
    for category in catalog['categories']['elements']:
        if category['name'] == category_name:
            category_id = category['id']

    return category_id


# Funciones de ordenamiento

"""def addVideoToCategory(catalog, category_id, video):
    categories = catalog['categories']
    poscategory = lt.isPresent(categories, category_id)
    if poscategory > 0:
        category = lt.getElement(categories, poscategory)
    else:
        category = newCategory(category_id)
        lt.addLast(categories, category)
    lt.addLast(tag['videos'], video) """
            
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
import time
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import selectionsort as ss
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import mergesort as mg
from DISClib.Algorithms.Sorting import quicksort as qs

assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos Array
def newCatalog_Array():
    catalog = {'videos': None,
               'country': None,
               'tagvideos': None,
               'categories': None}
    catalog['videos'] = lt.newList()
    catalog['country'] = lt.newList("ARRAY_LIST",
                                    cmpfunction=cmpcountry)
    catalog['tagvideos'] = lt.newList('ARRAY_LIST',
                                    cmpfunction=cmptags)
    catalog['categories'] = lt.newList('ARRAY_LIST',
                                    cmpfunction=cmpcategories)

    return catalog
#Construcción modelo linked
def newCatalog_Linked():
    """
    Inicializa el catálogo de videos. Crea una lista vacia para guardar
    todos los videos, adicionalmente, crea una lista vacia para los canales,
    una lista vacia para la fecha de tendencia, el país, las visitas, los likes, 
    los dislikes y adicionalmente el id de la categoría.
    . Retorna el catalogo inicializado.
    """
    catalog = {'videos': None,
               'country': None,
               'tagvideos': None,
               'categories': None}
    catalog['videos'] = lt.newList()
    catalog['country'] = lt.newList("SINGLE_LINKED",
                                    cmpfunction=cmpcountry)
    catalog['tagvideos'] = lt.newList("SINGLE_LINKED",
                                    cmpfunction=cmptags)
    catalog['categories'] = lt.newList("SINGLE_LINKED",
                                    cmpfunction=cmpcategories)
    return catalog


# Funciones para agregar informacion al catalogo
def addVideo(catalog, videos):
    # Se adiciona el video a la lista de videos
    lt.addLast(catalog['videos'], videos)
    #Se adicionan los tags en la lista de tagvideos
    tagvideo_info = videos['tags'].split("|")
    for tag_info in tagvideo_info:
        lt.addLast(catalog['tagvideos'], tag_info)
    #Adiciona los países en su respectiva llave
    country_info = videos['country']
    lt.addLast(catalog['country'], country_info)
    

def addCountry(catalog, n_country, video):
    list_country = catalog['country']
    post_country = lt.isPresent(list_country,n_country)
    if post_country > 0:
        country = lt.getElement(list_country, post_country)
    else: 
        country = newCountry(n_country)
        lt.addLast(list_country, video['country'])
    lt.addLast(country['videos'], video)


def addTagsVideo(catalog, n_tag, video):
    videotag = catalog['tagvideos']
    post_tagvideo = lt.isPresent(tagvideos, n_tag)
    if post_tagvideo > 0:
        videotag = lt.getElement(tagvideos, post_tagvideo)
    else:
        videotag = newVideo_Tag(n_tag)
        lt.addLast(tagvideos, videotag)
    lt.addLast(video_tag['videos'], video)


def addCategories(catalog, categories_videos):
    category = NewCategories(categories_videos['name'], categories_videos['id'])
    lt.addLast(catalog['categories'], category)


# Funciones para creacion de datos
# Estas funciones son precisamente para hacer la creación 
# De las llaves y sus respectivos valores (llaves vacías, la idea es crear la llave y en las funciones
# de agregar información al catálogo se completan)


def newCountry(n_country):
    country = {'name': "", 'videos': None}
    country['name'] = n_country
    country['videos'] = lt.newList('ARRAY_LIST')
    return country

def newVideo_Tag(tag_name):
    video_tag = {'name': "", 'videos': None}
    video_tag['name'] = tag_name
    video_tag['videos'] = lt.newList('ARRAY_LIST')
    return video_tag

def NewCategories(name, id):
    categories_videos = {'name': "", 'id': ""}
    categories_videos['name'] = name
    categories_videos['id'] = id
    return categories_videos

# Funciones utilizadas para comparar elementos dentro de una lista

def cmpcountry(country1, country2):
    if (country1.lower() in country2['country'].lower()):
        return 0
    return -1

def cmptags(tag1,tag2):
    if (tag1.lower() in tag2['name'].lower()):
        return 0
    return -1

def cmpcategories(n_category, categories_videos):
    return (n_category == categories_videos['name'])

def cmpVideosByViews(video1, video2):
    if video1['views'] < video2['views']:
        return True
    return False

# Funciones de ordenamiento

def sortVideos(catalog, size, sortType):
    sub_list = lt.subList(catalog['videos'], 0, size)
    start_time = time.process_time()
    if sortType == 1:
        sorted_list = ss.sort(sub_list, cmpVideosByViews)
    elif sortType == 2:
        sorted_list = ins.sort(sub_list, cmpVideosByViews)
    elif sortType == 3:
        sorted_list = sa.sort(sub_list, cmpVideosByViews)
    elif sortType == 4:
        sorted_list = mg.sort(sub_list, cmpVideosByViews)
    else:
        sorted_list = qs.sort(sub_list, cmpVideosByViews)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return elapsed_time_mseg, sorted_list
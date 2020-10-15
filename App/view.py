"""
 * Copyright 2020, Departamento de sistemas y Computación
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
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

import sys
import config
from DISClib.ADT import list as lt
from DISClib.DataStructures import arraylistiterator as it
from DISClib.ADT import orderedmap as om
from DISClib.ADT import map as m
from App import controller
assert config

"""
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones  y  por cada seleccion
hace la solicitud al controlador para ejecutar la
operación seleccionada.
"""
def impresor_de_datos_elefante_de_batalla_psiquico_ancestral(lista):
    A = it.newIterator(lista)
    while it.hasNext(A):
        B = it.next(A)
        print(B)
        print("🍞🍞🍞🍞🍞🍞🍞🍞🍞🍞🍞🍞🍞🍞🍞🍞🍞🍞🍞🍞🍞🍞🍞🍞🍞🍞🍞🍞🍞🍞🍞🍞🍞🍞🍞🍞🍞🍞🍞🍞🍞🍞🍞🍞🍞🍞🍞🍞🍞🍞🍞🍞🍞🍞🍞🍞🍞🍞🍞🍞🍞🍞🍞🍞🍞🍞🍞🍞🍞🍞🍞🍞🍞🍞")

# ___________________________________________________
#  Ruta a los archivos
# ___________________________________________________


#crimefile = "us_accidents_small.csv"
crimefile = "US_Accidents_Dec19.csv"

# ___________________________________________________
#  Menu principal
# ___________________________________________________


def printMenu():
    print("\n")
    print("*******************************************")
    print("Bienvenido")
    print("1- Inicializar Analizador")
    print("2- Cargar información de accidentes")
    print("3- Requerimento 1")
    print("4- Requerimento 2")
    print("0- Salir")
    
    print("*******************************************")


"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n>')

    if int(inputs[0]) == 1:
        print("\nInicializando....")
        # analyzer es el controlador que se usará de acá en adelante
        analyzer = controller.init()
        print("\nAnalizador cargado.")

    elif int(inputs[0]) == 2:
        print("\nCargando información de accidentes ....")
        controller.loadData(analyzer, crimefile)
        print("\nInformacion caragada exitosamente")
        print("Se cargaron",m.size(analyzer["crimenes"]),"elementos.")
        print("tamaño del arbol",om.height(analyzer["index"]))


    elif int(inputs[0]) == 3:
        criterio = input(str("\nBuscando accidentes en un rango de fechas: "))
        Monika = controller.obtener_crimenes_por_fecha(analyzer, criterio)
        impresor_de_datos_elefante_de_batalla_psiquico_ancestral(Monika)

    elif int(inputs[0]) == 4:
        print("\nRequerimiento No 1 del reto 3: ")

    else:
        sys.exit(0)
sys.exit(0)

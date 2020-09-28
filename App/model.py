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
import config
from DISClib.ADT import list as lt
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.DataStructures import arraylistiterator as it
from DISClib.ADT import map as m
from DISClib.Algorithms.Sorting import insertionsort as ins
import datetime
assert config

"""
En este archivo definimos los TADs que vamos a usar,
es decir contiene los modelos con los datos en memoria


"""


# -----------------------------------------------------
# API del TAD Catalogo de accidentes
def analyzer():
    analyzer = {"crimenes":None,
                "index":None}
    analyzer["crimenes"] = m.newMap(numelements=999,
                                 prime=109345121, 
                                 maptype="CHAINING", 
                                 loadfactor=1.0, 
                                 comparefunction=comparer)
    
    analyzer["index"] = om.newMap(omaptype="BST",
                                  comparefunction=compareDates)
    return analyzer
# -----------------------------------------------------
def fecha_convertidor(dato):
    crimedate = datetime.datetime.strptime(dato, '%Y-%m-%d %H:%M:%S')
    return crimedate.date()
def fecha_convertidor_consultas(dato):
    crimedate = datetime.datetime.strptime(dato, '%Y-%m-%d')
    return crimedate.date()

def lessfunction(ele1, ele2):
    if int(ele1["Severity"]) < int(ele2["Severity"]):
        return True
    return False

# Funciones para agregar informacion al catalogo

def cargaridcrimen(analyzer, crimen):
    listac = analyzer["crimenes"]
    index = analyzer["index"]
    fecha = fecha_convertidor(crimen["Start_Time"])
    m.put(listac, crimen["ID"], crimen)
    if om.contains(index, fecha)==True:
        agregarid(index, crimen, fecha)
    else:
        agregarfecha(index, crimen, fecha) 
"""
def añadircrimen(analyzer, a):
    Monika = {ID
            "Source":a["Source"]
            "TMC":a["TCM"]
            "Severity":a["Severity"]
            "Start_Time":a["Start_Time"]
            "End_Time":a["End_Time"]
            "Start_Lat":a["Start_Lat"]
            "Start_Lng":a["Start_Lng"]
            "End_Lat":a["End_Lat"]
            "End_Lng":a["End_Lng"]
            "Distance(mi)":a["Distance(mi)"]
            "Description":a["Description"]
            "Number":a["Number"]
            "Street":a[" Street"]
            Side
            City
            County
            State
            Zipcode
            Country
            Timezone
            Airport_Code
            Weather_Timestamp
            Temperature(F)
            Wind_Chill(F)
            Humidity(%)
            Pressure(in)
            Visibility(mi)
            Wind_Direction
            Wind_Speed(mph)
            Precipitation(in)
            Weather_Condition
            Amenity
            Bump
            Crossing
            Give_Way
            Junction
            No_Exit
            Railway
            Roundabout
            Station
            Stop
            Traffic_Calming
            Traffic_Signal
            Turning_Loop
            Sunrise_Sunset
            Civil_Twilight
            Nautical_Twilight
            Astronomical_Twilight
}
    m.put(analyzer["crimenes"], crimen["ID"], Monika)
    """
def agregarid(index, crimen, fecha):
    a = om.get(index, fecha)
    b = me.getValue(a)
    lt.addLast(b, crimen["ID"])

def agregarfecha(index, crimen, fecha):
    N = lt.newList(datastructure="ARRAY_LIST")
    lt.addLast(N, crimen["ID"])
    om.put(index, fecha, N)

# ==============================
# Funciones de consulta
# ==============================
def obtener_accidentes_en_una_fecha(analyzer, criterioa):
    criterio = fecha_convertidor_consultas(criterioa)
    d = lt.newList("ARRAY_LIST")
    a = om.get(analyzer["index"], criterio)
    b = me.getValue(a)
    c = it.newIterator(b)
    while it.hasNext(c):
        n = it.next(c)
        A = m.get(analyzer["crimenes"], n)
        B = me.getValue(A)
        lt.addLast(d, B)
    ins.insertionSort(d, lessfunction)
    return d
    
    
    





# ==============================
# Funciones de Comparacion
# ==============================
def compareDates(date1, date2):
    """
    Compara dos ids de libros, id es un identificador
    y entry una pareja llave-valor
    """
    if (date1 == date2):
        return 0
    elif (date1 > date2):
        return 1
    else:
        return -1

def comparer(keyname, value):
    entry = me.getKey(value)
    if (keyname == entry):
        return 0
    elif (keyname > entry):
        return 1
    else:
        return -1
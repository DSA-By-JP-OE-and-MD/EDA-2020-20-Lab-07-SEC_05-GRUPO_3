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
from DISClib.DataStructures import linkedlistiterator as lit
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
    analyzer = {"accidentes":None,
                "index":None}
    analyzer["accidentes"] = m.newMap(numelements=999,
                                 prime=109345121, 
                                 maptype="CHAINING", 
                                 loadfactor=1.0, 
                                 comparefunction=comparer)
    
    analyzer["index"] = om.newMap(omaptype="RBT",
                                  comparefunction=compareDates)
    return analyzer
# -----------------------------------------------------
def fecha_convertidor(dato):
    accidentdate = datetime.datetime.strptime(dato, '%Y-%m-%d %H:%M:%S')
    return accidentdate.date()
def fecha_convertidor_consultas(dato):
    accidentdate = datetime.datetime.strptime(dato, '%Y-%m-%d')
    return accidentdate.date()

def lessfunction(ele1, ele2):
    if int(ele1["Severity"]) < int(ele2["Severity"]):
        return True
    return False

# Funciones para agregar informacion al catalogo

def cargaridaccidente(analyzer, accidente):
    listac = analyzer["accidentes"]
    index = analyzer["index"]
    fecha = fecha_convertidor(accidente["Start_Time"])
    m.put(listac, accidente["ID"], accidente)
    if om.contains(index, fecha)==True:
        agregarid(index, accidente, fecha)
    else:
        agregarfecha(index, accidente, fecha) 

def agregarid(index, accidente, fecha):
    a = om.get(index, fecha)
    b = me.getValue(a)
    lt.addLast(b, accidente["ID"])

def agregarfecha(index, accidente, fecha):
    N = lt.newList(datastructure="ARRAY_LIST")
    lt.addLast(N, accidente["ID"])
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
        A = m.get(analyzer["accidentes"], n)
        B = me.getValue(A)
        lt.addLast(d, B)
    ins.insertionSort(d, lessfunction)
    return d
def crear_lista_con_fechas(index, accidentes, fecha1, fecha2):
    d = {}
    A = om.values(index, fecha1, fecha2)
    M = lit.newIterator(A)
    while lit.hasNext(M):
        L = lit.next(M)
        N = it.newIterator(L)
        while it.hasNext(N):
            D = it.next(N)
            R = m.get(accidentes, D)
            K = me.getValue(R)
            if fecha_convertidor(K["Start_Time"]) in d:
                d[fecha_convertidor(K["Start_Time"])] += 1
            else:
                d[fecha_convertidor(K["Start_Time"])] = 1
    return d

def crear_lista_con_estados(index, accidentes, fecha1, fecha2):
    d = {}
    A = om.values(index, fecha1, fecha2)
    M = lit.newIterator(A)
    while lit.hasNext(M):
        L = lit.next(M)
        N = it.newIterator(L)
        while it.hasNext(N):
            D = it.next(N)
            R = m.get(accidentes, D)
            K = me.getValue(R)
            if K["State"] in d:
                d[K["State"]] += 1
            else:
                d[K["State"]] = 1
    return d

def fecha_con_mas_casos(analyzer, fecha1, fecha2):
    index = analyzer["index"]
    accidentes = analyzer["accidentes"]
    fecha1 = fecha_convertidor_consultas(fecha1)
    fecha2 = fecha_convertidor_consultas(fecha2)
    A = crear_lista_con_fechas(index, accidentes, fecha1, fecha2)
    contadorF = 0
    mayorfecha = None
    for a in A:
        if A[a] > contadorF:
            contadorF = A[a]
            mayorfecha = a
    return mayorfecha


def estado_con_mas_casos(analyzer, fecha1, fecha2):
    index = analyzer["index"]
    accidentes = analyzer["accidentes"]
    fecha1 = fecha_convertidor_consultas(fecha1)
    fecha2 = fecha_convertidor_consultas(fecha2)
    B = crear_lista_con_estados(index, accidentes, fecha1, fecha2)
    mayorestado = None
    contadorE = 0
    for b in B:
        if B[b] > contadorE:
            contadorE = B[b]
            mayorestado = b
    return mayorestado
    

    
    





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
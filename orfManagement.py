import os
import re
import util.textOperations as ops
from model.Function import Function
from model.Class import OrfClass


def __findClassByDescription(classList, description):
    for clas in classList:
        if description in clas.description:
            return clas.classId


def __getClasses(path):
    classes = list()
    with open(path) as orfFile:
        for line in orfFile:
            classProps = __findClassProperties(line)
            if classProps is not None:
                classes.append(OrfClass(classProps[0], classProps[1]))
    return classes

def __findClassProperties(line):
    if ops.matchText("class", line) is not None:
        content = ops.getInsideText(line)
        classId = ops.getOrfClassId(content)
        description = ops.extractClassId(content)
        description = description[2:len(description) - 1]
        return (classId, description)

def __findFunctionProperties(line):
    """
    Devuelve una lista con los parámetros de la linea del archivo de texto tb_functions
    :param line: Texto con el formato adecuado para extraer las propiedades del orf
    :return: una lista con el siguiente orden idClase,orf,nombre,description
    """
    if ops.matchText("function", line) is not None:
        # Primero recuperamos todos los parámetros de las línea
        content = ops.getInsideText(line)
        # Obtenemos la clase
        classId = ops.getOrfClassId(line)
        # Una vez obtenida la clase,la eliminamos y spliteamos el texto para sacar el resto de campos
        # properties = re.sub(CLASS_ID_PATTERN, '', properties).split(",")
        content = ops.extractClassId(content).split(",")
        description = ""

        # Creamos la description por si hubiera sido cortada en el paso anterior
        for item in content[3:]:
            description = description + item
        description=description[1:-1]
        return Function(classId, content[0], content[1], description)

def countClassByOrfDescription(path, textToFind, textLengh=None):
    """

    :param path: ruta del archivo
    :param textToFind: texto que debe estar contenido en la descripcion
    :param textLengh: longitud de la palabra que incluye el texto
    :return:  el numero de clases relacionadas con orfs cuya descripcion contiene el texto requerido
    """
    foundClass = list()
    with open(path) as orfFile:
        for line in orfFile:
            orfData = __findFunctionProperties(line)
            # Si la linea contiene los datos correspondientes y además su descripcion contiene la palabra que buscamos
            # lo cuenta
            if orfData is not None and textToFind in orfData.description and orfData.classId not in foundClass:
                if textLengh is not None:
                    word = [word for word in orfData.description.split(" ") if textToFind in word]
                    if len(word[0]) == textLengh:
                        foundClass.append(orfData.classId)
                else:
                    foundClass.append(orfData.classId)
    return len(foundClass)


def countOrfByClassDescription(path, textToFind):
    """
    Cuenta los orf que pertenecen a la clase que en su description contenga el texto
    :param path: la ruta del archivo de datos
    :param textToFind: el texto que debe contener el campo description
    :return: un entero con el numero de casos que contienen el texto buscado
    """
    count = 0
    classes = __getClasses(path)
    classId = __findClassByDescription(classes, textToFind)
    with open(path) as orfFile:
        for line in orfFile:
            orfData = __findFunctionProperties(line)
            # Si la linea contiene los datos correspondientes y además su descripcion contiene la palabra que buscamos
            # lo cuenta
            if orfData is not None and orfData.classId == classId:
                count += 1
    return count

def countOrfByClass(dirPath):
    """
    Cuanta cuantos orf tiene cada clase
    :param dirPath: ruta al directorio o archivo donde se encuentran los archivos a leer
    :return: el numero de orf que pertenecen a cada clase
    """
    orfCount = dict()

    def readAndCount(path, orfDict):
        orfCountCopy = orfDict.copy()
        with open(path) as orfFile:
            for line in orfFile:
                orfClass = __findFunctionProperties(line)
                if orfClass is not None:
                    classId = orfClass.classId
                    if classId not in orfCountCopy:
                        orfCountCopy[classId] = 1
                    else:
                        orfCountCopy[classId] += 1
        return orfCountCopy

    if (os.path.isdir(dirPath)):
        for file in os.listdir(dirPath):
            return readAndCount(file, orfCount)
    else:
        return readAndCount(dirPath, orfCount)


PATH = "data/tb_functions.pl"

# print(countOrfByClass("data/tb_functions.pl"))
# print(countOrfByClassDescription("data/tb_functions.pl", "Respiration"))
# print(countClassByOrfDescription(PATH, "ferredoxin"))
# print(countClassByOrfDescription(PATH, "hydro",13))

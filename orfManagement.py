import os
import re


def countOrfByDescription(path, description):
    count = 0
    with open(path) as orfFile:
        for line in orfFile:
            orfData = findFunctionProperties(line)
            if orfData is not None and description in orfData[3]:
                count += count
    return count


def findFunctionProperties(line):
    """
    Devuelve una lista con los parámetros de la linea del archivo de texto tb_functions
    :param line: Texto con el formato adecuado para extraer las propiedades del orf
    :return: una lista con el siguiente orden idClase,orf,nombre,description
    """
    if re.match("function(.*)", line) is not None:
        # Primero recuperamos todos los parámetros de las línea
        properties = re.search("\((.*)\)", line).group(1)
        # Obtenemos la clase
        classId = re.search("\[(\d,\d,\d,\d)\]", properties).group(1)
        # Una vez obtenida la clase,la eliminamos y spliteamos el texto para sacar el resto de campos
        properties = re.sub(",\[(\d,\d,\d,\d)\]", '', properties).split(",")

        description = ""
        # Creamos la description por si hubiera sido cortada en el paso anterior
        for item in properties[2:]:
            description = description + item

        return classId, properties[0], properties[1], description


def countOrf(dirPath):
    orfCount = dict()

    def readAndCount(path, orfDict):
        orfCountCopy = orfDict.copy()
        with open(path) as orfFile:
            for line in orfFile:
                orfClass = findFunctionProperties(line)
                if orfClass is not None:
                    classId = orfClass[0]
                    orf = orfClass[1]
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


#print(countOrf("data/tb_functions_sample.pl"))
print(countOrfByDescription("data/tb_functions_sample.pl", "Respiration"))

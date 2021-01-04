
import os
import re

def countOrf(dirPath):
    orfCount=dict()


    def findFunctionProperties(line):
        """
        Devuelve una lista con los parámetros de la linea
        :param line:
        :return:
        """
        if re.match("function(.*)", line) is not None:
            #function(tb186,[1,1,1,0],'bglS',"beta-glucosidase").
            #orf,idClass,genName,description
            #Primero recuperamos todos los parámetros de las líneas functions
            properties=re.search("\((.*)\)", line).group(1)
            #Obtenemos la clase
            classId=re.search("\[(\d,\d,\d,\d)\]",properties).group(1)
            #Una vez obtenida la clase,la eliminamos y spliteamos el texto para sacar el resto de campos
            properties=re.sub(",\[(\d,\d,\d,\d)\]", '', properties).split(",")
            #Finalmente volvemos a insertar la clase para crear una lista con todos los parámetros
            properties.insert(0,classId)
            return (properties)

    def readAndCount(path,orfDict):
        orfCountCopy=orfDict.copy()
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


    if(os.path.isdir(dirPath)):
        for file in os.listdir(dirPath):
            orfCount=readAndCount(file,orfCount)
    else:
        orfCount=readAndCount(dirPath,orfCount)

    print(orfCount)



countOrf("data/tb_functions_sample.pl")

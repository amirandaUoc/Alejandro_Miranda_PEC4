
import orfManagement as orfMng

description="Respiration"
DIR_PATH="data/tb_functions.pl"

#1.1
print(orfMng.countOrfByClass(DIR_PATH))
#1.2
print("Orf que pertenecen a la clase con Respiration en la descripcion : {}".format(orfMng.countOrfByClassDescription(DIR_PATH,description)))
#2.1
print("Numero de clases que tienen algún ORF con protein en su description: {}".format(orfMng.countClassByOrfDescription(DIR_PATH,"protein")))
#2.2
print("Numero de clases que tienen algún ORF con hydro en una palabra de 13 caracteres en su descripcion: {}".format(orfMng.countClassByOrfDescription(DIR_PATH,"hydro",13)))

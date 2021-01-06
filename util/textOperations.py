import re

CLASS_ID_PATTERN="\[(\d+,\d+,\d+,\d+)\]"
CLASS_PATTERN="class({})"
FUNCTION_PATTERN="function(.*)"

def matchText(type,text,textToFind=""):
    return re.match("{}(.*{}.*)".format(type, textToFind), text)

def extractClassId(text):
    return re.sub(CLASS_ID_PATTERN, '', text)

def getOrfClassId(text):
    return re.search(CLASS_ID_PATTERN, text).group(1)

def getInsideText(text):
    return re.search("\((.*)\)", text).group(1)

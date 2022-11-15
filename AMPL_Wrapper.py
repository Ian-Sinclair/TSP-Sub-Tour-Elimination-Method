import json


def test() :
    print('hi')

def readJsonData(filename) :
    with open(filename, 'r') as f :
        data = json.load(f)
    return data

def AMPLT_Result_to_path(inputFile : str) :
    city_info = []
    with open(inputFile, 'r') as f:
        city_info += f.readline()
    print(city_info)

def makeDatFile(data : dict, outfile='TSP_DATA.dat') :
    if type(data) == type(' ') :
        data = readJsonData(data)
    
    #  Generate SET
    datFileString = 'set ORIG := \n'
    nextSET = 'set DEST := \n'
    for city in data.keys() :
        datFileString += '\t' + city.replace(" ", "_") + ' \n'
        nextSET += '\t' + city.replace(" ", "_") + ' \n'
    datFileString += ';\n'
    nextSET += ';\n'
    datFileString += nextSET
    paramString = 'param DISTANCE := \n'
    for origin, travel_info in data.items() :
        paramString += '\t[' + str(origin.replace(" ", "_")) + ',*] '
        for dest, info in travel_info.items() :
            paramString += dest.replace(" ", "_") + ' ' + str(info['duration']) + ' '
        paramString += '\n'
    paramString += ';\n'
    datFileString += paramString

    with open(outfile, 'w', encoding='utf-8') as f:
        f.write(datFileString)





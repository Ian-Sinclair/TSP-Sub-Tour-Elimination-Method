'''
    Ian Sinclair
    11/15/2022
    This is a wrapper around AMPL code.
    In particular, this file includes methods to generate a .dat
    AMPL file from a JSON file.
    This method assume a special format for .dat files
    that directly corresponds to the requirements of the
    pre-written .mod AMPL files.
    And so will encode .dat in the same way every time
    except with different cities.
'''

import json

#  Reads Json data to dictionary
def readJsonData(filename) :
    with open(filename, 'r') as f :
        data = json.load(f)
    return data

#  Reads a file of city names (one name per line) returns list.
def AMPLT_Result_to_path(inputFile : str) :
    city_info = []
    with open(inputFile, 'r') as f:
        city_info += f.readline()
    print(city_info)


#  Makes a .dat file in the style of an AMPL file.
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





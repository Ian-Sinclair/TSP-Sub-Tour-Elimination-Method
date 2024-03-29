'''
    Ian Sinclair
    11/15/2022
    This file includes API request resources to query coordinate information, 
    and distance metric information for a list of cities.
'''

from src.AMPL_Wrapper import *
import requests
import json
import os
from dotenv import load_dotenv
from geopy.geocoders import Nominatim



def LocationToCoordinate(loc1 : str ) -> tuple :
    '''
        Inputs a city location as a string,
        returns the longitude and latitude coordinates of the city location.
        (lat, long)
    '''
    geocoder = Nominatim(user_agent="TSP Sub Tour Application")
    coord = geocoder.geocode(loc1)
    return (coord.latitude , coord.longitude)

    
#  API call to convert list of cities to a distance matrix dictionary. 
def citiesToDistanceMatrix(location : dict) -> list[list] :
    '''
    string = 'https://api.distancematrix.ai/maps/api/distancematrix/json?origins=<origin_location_1|origin_location_2|...|origin_location_n> \
                &destinations=<destination_location_1|destination_location_2|...|destination_location_n> \
                &key=' API_KEY
    '''
    load_dotenv()
    API_KEY = os.getenv('PROTECT_DISTANCE_MATRIX_API_KEY')
    DistanceMatrix = {}

    for city in location.keys() :
        DistanceMatrix[city] = {}

    for name_1 in location.keys() :
        coor_1 = location[ name_1 ]
        for name_2 in list(location.keys()) :
            coor_2 = location[name_2]
            origin = str(coor_1[0]) + ',' + str(coor_1[1])
            destination = str(coor_2[0]) + ',' + str(coor_2[1])
            API_Request = ('https://api.distancematrix.ai/maps/api/distancematrix/json?' +
                            'origins=' + origin + 
                            '&destinations=' + destination + 
                            '&key=' + API_KEY
                            )
            response = requests.get(API_Request)
            if response.json()['rows'][0]['elements'][0]['status'] != 'ZERO_RESULTS' :
                DistanceMatrix[name_1][name_2] = {
                    'duration' :  response.json()['rows'][0]['elements'][0]['duration']['value']/60,
                    'origin' : name_1,
                    'destination' : name_2
                }
            else :
                print('Route Not Found:  ' + name_1 + ' --> ' + name_2)
                DistanceMatrix[name_1][name_2] = {
                    'duration' :  100000,
                    'origin' : name_1,
                    'destination' : name_2
                }
    return DistanceMatrix

    
#  Writes dictionary to JSON
def writeToJSON(data, filename = 'DistanceMatrix.json') :
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)



#  Reads JSON to dictionary
def JsonToDict(filename) :
    with open(filename, 'r') as f :
        data = json.load(f)
    return data


#  Creates distance matrix for list of cities (distance from any city to any other city.)
def Collect_data(cities = None, filename = 'DistanceMatrix.json') :
    if cities == None :
        cities = [
            'Denver',
            'New York',
            'Houston',
            'Dallas',
            'Philadelphia'
            ]
    locations = {}
    for city in cities :
        locations[city] = LocationToCoordinate(city)

    #print(locations)
    DistanceMatrix = citiesToDistanceMatrix(locations)

    writeToJSON(DistanceMatrix,filename)
    return DistanceMatrix


if __name__ == "__main__":
    print('Testing main.py functions --> LocationToCoordinate , citiesToDistanceMatrix , writeToJSON , JsonToDict')
    Collect_data()
    print(JsonToDict('DistanceMatrix.json'))

    #makeDatFile('DistanceMatrix.json')








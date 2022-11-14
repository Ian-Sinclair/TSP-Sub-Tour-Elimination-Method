import requests
import json
import os
from dotenv import load_dotenv
from geopy.geocoders import Nominatim
from geopy import distance


def LocationToCoordinate(loc1 : str ) -> tuple :
    '''
        Inputs a city location as a string,
        returns the longitude and latitude coordinates of the city location.
        (lat, long)
    '''
    geocoder = Nominatim(user_agent="TSP Sub Tour Application")
    coord = geocoder.geocode(loc1)
    return (coord.latitude , coord.longitude)

    
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

    for i , name_1 in enumerate(location.keys()) :
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

            DistanceMatrix[name_1][name_2] = {
                'duration' :  response.json()['rows'][0]['elements'][0]['duration']['value']/60,
                'origin' : name_1,
                'destination' : name_2
            }
    return DistanceMatrix

    

def writeToJSON(data) :
    with open('DistanceMatrix.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)




cites = [
    'Denver',
    'New York',
    'Houston'
]

locations = {}
for city in cites :
    locations[city] = LocationToCoordinate(city)

#print(locations)
DistanceMatrix = citiesToDistanceMatrix(locations)

writeToJSON(DistanceMatrix)











import googlemaps
import pprint
import time
import json
import pandas as pd
import pandas_gbq

#Declare the API key
API_KEY = 'AIzaSyAdH-a3k5fBy-_DyNhygTAtaqzNkhw_rVk'

#Call places API and pass the lattitude longitude of a place and the type of information wanted.
my_fields = ['name','type','formatted_phone_number','formatted_address']
#my_fields = ['name']
def main_api_places(latlong,type1):
  gmaps = googlemaps.Client(key = API_KEY)
  places_result = gmaps.places_nearby(location = latlong,radius = 40000, open_now = False, type =type1)
  places_endresults = []
  for x in places_result['results']:
    places_details = gmaps.place(place_id = x['place_id'], fields = my_fields)
    places_endresults.append(places_details)
  return(places_endresults)
  
  powai_places = (main_api_places('19.1197,72.9052','cafe'))
  
  def places_name_intent():
  for places in powai_places:
    #return(places['result']['name'])
    return(places['result'])    
  
  rows_to_insert = pd.DataFrame(places_name_intent())
  
  pandas_gbq.to_gbq(rows_to_insert, 'New.Powai_Places', project_id='api-new-242611',if_exists ='replace')

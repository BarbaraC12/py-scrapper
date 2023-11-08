import requests
import sys
from decouple import config

# api_to_test = {
#   "https://www.themoviedb.org/documentation/api",
#   "https://fr.openfoodfacts.org/data",
#   "https://randomuser.me/",
#   "http://countrylayer.com/",
#   "https://www.countryflags.io/",
#   "http://www.zippopotam.us/",
#   "https://developers.giphy.com/"
#   }
# https://talks.freelancerepublik.com/api-publiques-gratuites-developpement-site-app/
api_url = config('API_URL')

auth_data = {
    'uid': config('API_UID'),
    'secret': config('API_SECRET')
}


response = requests.get(api_url, params=auth_data) if auth_data['uid'] or auth_data['secret'] else requests.get(api_url)

if response.status_code != 200:
    print("Failed to get data from API")
else:
    data = response.json()
    print(data)

import requests
# from decouple import Config

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
api_url = "https://api.zippopotam.us/fr/31530"

# That don't work with .env I've to search why
# config = Config('.env')
# api_url = config.get('API_URL')
# api_uid = config.get('API_UID')
# api_secret = config.get('API_SECRET')

# auth_data = {
#     'uid': api_uid,
#     'secret': api_secret
# }

response = requests.get(api_url)

if response.status_code != 200:
    print("Failed to get data from API")
else:
    data = response.json()
    print(data)

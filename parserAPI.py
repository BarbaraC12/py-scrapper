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
try:
    api_url = config('API_URL')
    if api_url:
        auth_data = {
            'uid': config('API_UID'),
            'secret': config('API_SECRET')
        }
    else:
        raise ValueError("No API found check .env file")
    response = requests.get(api_url, params=auth_data) if auth_data['uid'] or auth_data['secret'] else requests.get(api_url)
    response.raise_for_status()  # Check for HTTP status code errors
    if response.status_code != 200:
        raise ValueError(f"Failed and get info from {api_url} API.\n")
    data = response.json()
    print(data)
except requests.exceptions.ConnectionError as ce:
    print(f"Connection Error: {ce}\n",
          "Check yout connection. End of program.")
except requests.exceptions.RequestException as re:
    print(f"Request Exception: {re}")
except ValueError as e:
    print(f"Error: {e}")
except KeyboardInterrupt:
    print("\nInput interrupted. End of program.")

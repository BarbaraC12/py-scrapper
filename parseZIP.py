import requests
from decouple import config

valid_zip = {
    'AD': 'AD100 and AD700 with 7 posibility',
    'AR': '1601 and 9431 with 20260 posibility',
    'AS': '96799 and 96799 with 1 posibility',
    'AT': '1010 and 9992 with 4877 posibility',
    'AU': '0200 and 9726 with 10161 posibility',
    'BD': '1000 and 9461 with 1323 posibility',
    'BE': '1000 and 9992 with 3386 posibility',
    'BG': '1000 and 9974 with 5304 posibility',
    'BR': '01000-000 and 99990-000 with 5526 posibility',
    'CA': 'A0A and Y1A with 1621 posibility',
    'CH': '1000 and 9658 with 4614 posibility',
    'CZ': '100 00 and 798 62 with 15507 posibility',
    'DE': '01067 and 99998 with 16482 posibility',
    'DK': '0800 and 9990 with 1182 posibility',
    'DO': '10101 and 11906 with 546 posibility',
    'ES': '01001 and 52080 with 56542 posibility',
    'FI': '00002 and 99999 with 4637 posibility',
    'FO': '100 and 970 with 130 posibility',
    'FR': '01000 and 98799 with 51129 posibility',
    'GB': 'AB1 and ZE3 with 27769 posibility',
    'GF': '97300 and 97390 with 25 posibility',
    'GG': 'GY1 and GY9 with 8 posibility',
    'GL': '2412 and 3992 with 33 posibility',
    'GP': '97100 and 97190 with 33 posibility',
    'GT': '01001 and 22027 with 548 posibility',
    'GU': '96910 and 96932 with 23 posibility',
    'GY': '97312 and 97360 with 9 posibility',
    'HR': '10000 and 53296 with 6943 posibility',
    'HU': '1011 and 9985 with 4041 posibility',
    'IM': 'IM1 and IM9 with 86 posibility',
    'IN': '110001 and 855126 with 15226 posibility',
    'IS': '101 and 902 with 148 posibility',
    'IT': '00010 and 98168 with 19940 posibility',
    'JE': 'JE1 and JE3 with 4 posibility',
    'JP': '0001	100-0001 and 999-8531 with 94388 posibility',
    'LI': '9485 and 9498 with 13 posibility',
    'LK': '* and 96167 with 1832 posibility',
    'LT': '00001 and 99069 with 20558 posibility',
    'LU': '1009	L-1009 and L-9999 with 4334 posibility',
    'MC': '98000 and 98000 with 29 posibility',
    'MD': '2000	MD-2000 and MD-7731 with 1753 posibility',
    'MH': '96960 and 96970 with 2 posibility',
    'MK': '1000 and 7550 with 220 posibility',
    'MP': '96950 and 96952 with 4 posibility',
    'MQ': '97200 and 97290 with 34 posibility',
    'MX': '01000 and 99998 with 75203 posibility',
    'MY': '01000 and 98859 with 2818 posibility',
    'NL': '1000 and 9999 with 5314 posibility',
    'NO': '0001 and 9991 with 4574 posibility',
    'NZ': '0110 and 9893 with 1737 posibility',
    'PH': '0400 and 9811 with 2232 posibility',
    'PK': '10010 and 97320 with 11847 posibility',
    'PL': '001	00-001 and 99-440 with 21980 posibility',
    'PM': '97500 and 97500 with 2 posibility',
    'PR': '00601 and 00988 with 187 posibility',
    'PT': '001	1000-001 and 9980-999 with 204006 posibility',
    'RE': '97400 and 97490 with 37 posibility',
    'RU': '101000 and 901993 with 43538 posibility',
    'SE': '10005 and 98499 with 16079 posibility',
    'SI': '1000 and 9600 with 557 posibility',
    'SJ': '8099 and 9178 with 8 posibility',
    'SK': '010 01 and 992 01 with 4152 posibility',
    'SM': '47890 and 47899 with 26 posibility',
    'TH': '10100 and 96220 with 902 posibility',
    'TR': '01000 and 81950 with 51379 posibility',
    'US': '00210 and 99950 with 43624 posibility',
    'VA': '00120 and 00120 with 2 posibility',
    'VI': '00801 and 00851 with 16 posibility',
    'YT': '97600 and 97680 with 17 posibility',
    'ZA': '0002 and 9992 with 3920 posibility',
}


valid_city = [
    'AD', 'AR', 'AS', 'AT', 'AU',
    'BD', 'BE', 'BG', 'BR',
    'CA', 'CH', 'CZ',
    'DE', 'DK', 'DO',
    'ES',
    'FI', 'FO', 'FR',
    'GB', 'GF', 'GG', 'GL', 'GP', 'GT', 'GU', 'GY',
    'HR', 'HU',
    'IM', 'IN', 'IS', 'IT',
    'JE', 'JP',
    'LI', 'LK', 'LT', 'LU',
    'MC', 'MD', 'MH', 'MK', 'MP', 'MQ', 'MX', 'MY',
    'NL', 'NO', 'NZ',
    'PH', 'PK', 'PL ', 'PM', 'PR', 'PT',
    'RE', 'RU',
    'SE', 'SI', 'SJ', 'SK', 'SM',
    'TH', 'TR',
    'US',
    'VA', 'VI',
    'YT',
    'ZA']


def check_city_code(value):
    if value not in valid_zip:
        raise ValueError(f"City code '{value}' unknow. " +
                         f"Valids city codes are :\n{', '.join(valid_zip)}.")
    return value


def print_data(data):
    for key, value in data.items():
        if key != 'places':
            print(f"{key.capitalize()} : {value}")
        else:
            print("Places data:")
            if isinstance(value, dict):
                for k_val, val in value.items():
                    print(k_val, val)
            if isinstance(value, list):
                for item in value:
                    for k_val, val in item.items():
                        print(f"   - {k_val.capitalize()} : {val}")


try:
    api_url = config('ZPP_URL')
    if api_url:
        city_code = input("Enter City Code (2 letters): ")
        zip_code = input("Enter code Zip: ")
    else:
        raise ValueError("No API found check .env file")
    city_code = check_city_code(city_code.upper())
    api_url += '/' + city_code + '/' + zip_code
    response = requests.get(api_url)
    response.raise_for_status()  # Check for HTTP status code errors
    if response.status_code != 200:
        raise ValueError(
            "Failed and get info from API.\n" +
            f"Zip of '{city_code}' must be between {valid_zip[city_code]}.")
    data = response.json()
    print_data(data)
except requests.exceptions.ConnectionError as ce:
    print(f"Connection Error: {ce}\n",
          "Check yout connection. End of program.")
except requests.exceptions.RequestException as re:
    print(f"Request Exception: {re}")
except ValueError as e:
    print(f"Error: {e}")
except KeyboardInterrupt:
    print("\nInput interrupted. End of program.")

# Python scrapper
version: python3.8

## [API zippopotam](https://www.zippopotam.us/#)
Postal Codes and Zip Codes made easy, it's aFree API with JSON Response Format.  
There have over 60 Countries Supported. And this API is perfect for Form Autocompletion.  
```
Structure classic:         -> api.zippopotam.us/country/postal-code
    Example: api.zippopotam.us/us/90210
Structure with city name:  -> api.zippopotam.us/country/state-abr/city
    Example: api.zippopotam.us/us/b3/toulouse
```
- How to use: 
```/bin/bash
py-scrapper $> python parseZIP.py
> Enter country(2 letters): fr
> Enter zip or state/city: 31200
-------------------------------------
Post code : 31200
Country : France
Country abbreviation : FR
Places data:
   - Place name : Toulouse
   - Longitude : 1.4437
   - State : Midi-Pyrénées
   - State abbreviation : B3
   - Latitude : 43.6043
```

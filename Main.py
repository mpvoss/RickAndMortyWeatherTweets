from TwitterAPI import TwitterAPI
import pyowm
import random
from memegenerator import memegenerator
import WeatherToMemeUtil
import time
import configparser
import sys, getopt

# ------------------------------------------------------
# Did we get passed a config file via command line?
# ------------------------------------------------------
optlist, args = getopt.getopt(sys.argv[1:], ':c:')
if len(optlist) > 0 and optlist[0][0] == '-c':
    config_file = optlist[0][1]
else:
    config_file = 'config/api_keys'

# ------------------------------------------------------
# Read in our api keys
# ------------------------------------------------------
Config = configparser.ConfigParser()
Config.read(config_file)

consumer_key = Config.get('Twitter', 'consumer_key')
consumer_secret = Config.get('Twitter', 'consumer_secret')
access_token_key = Config.get('Twitter', 'access_token_key')
access_token_secret = Config.get('Twitter', 'access_token_secret')

weatherAPI = Config.get('OpenWeatherMap', 'apiKey')

# ------------------------------------------------------
# Set up API access
# ------------------------------------------------------
twitterAPI = TwitterAPI(consumer_key,
                        consumer_secret,
                        access_token_key,
                        access_token_secret)

owm = pyowm.OWM(weatherAPI)

# ------------------------------------------------------
# Read List of Cities
# ------------------------------------------------------
cities = []
with open('canada.csv', 'r') as f:
    counter = 0
    for x in f:
        # x = x.encode('utf-8').strip()
        counter += 1
        x = x.rstrip()
        parts = x.split(",")
        cities.append(parts[0].strip() + ", " + parts[1])

# ------------------------------------------------------
# Main loop
# ------------------------------------------------------
for city in cities:
    # time.sleep(1)
    city = random.choice(cities)
    observation = owm.weather_at_place("Dease Lake, BC")
    w = observation.get_weather()
    status = w._status
    tempF = w.get_temperature('fahrenheit')['temp']
    tempC = w.get_temperature('celsius')['temp']
    print(city + " " + status + " " + str(tempF))
    meme_tuple = WeatherToMemeUtil.get_strings(status, tempF, tempC, city)

    if meme_tuple is None:
        continue

    print(meme_tuple)

    filename = memegenerator.make_meme(meme_tuple[0], meme_tuple[1], 'img/' + meme_tuple[2])

    file = open(filename, 'rb')
    data = file.read()
    r = twitterAPI.request('media/upload', None, {'media': data})
    print('UPLOAD MEDIA SUCCESS' if r.status_code == 200 else 'UPLOAD MEDIA FAILURE')

    # STEP 2 - post tweet with reference to uploaded image
    if r.status_code == 200:
        media_id = r.json()['media_id']
        r = twitterAPI.request('statuses/update', {'status': 'Uuuuuurrrpppp! Rick and Morty Weather update for ' + city,
                                                   'media_ids': media_id})
        print('UPDATE STATUS SUCCESS' if r.status_code == 200 else 'UPDATE STATUS FAILURE')

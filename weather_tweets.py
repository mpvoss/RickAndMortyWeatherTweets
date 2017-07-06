from TwitterAPI import TwitterAPI
import pyowm
import random
from memegenerator import memegenerator
import meme_template_util
import time
import configparser
import sys, getopt


def generate_weather_tweets(twitter_api, open_weather_api, cities):
    usedImages = []
    for city in cities:
        time.sleep(5)
        city = random.choice(cities)
        observation = open_weather_api.weather_at_place(city)
        w = observation.get_weather()
        status = w._status
        tempF = w.get_temperature('fahrenheit')['temp']
        tempC = w.get_temperature('celsius')['temp']

        print(city + " " + status + " " + str(tempF))
        meme_tuple = meme_template_util.get_strings(status, tempF, tempC, city)

        if meme_tuple is None or meme_tuple[2] in usedImages:
            print('Skipping {} because we\'ve already seen it'.format(city))
            continue

        usedImages.append(meme_tuple[2])
        print(meme_tuple)

        filename = memegenerator.make_meme(meme_tuple[0], meme_tuple[1], 'img/' + meme_tuple[2])

        post_weather_update(filename, city,twitter_api)


def post_weather_update(filename, city, twitter_api):

    file = open(filename, 'rb')
    data = file.read()
    r = twitter_api.request('media/upload', None, {'media': data})

    if r.status_code != 200:
        print("Unable to upload image to Twitter")
        return

    media_id = r.json()['media_id']
    r = twitter_api.request('statuses/update', {'status': 'Uuuuuurrrpppp! Rick and Morty Weather update for ' + city,
                                                   'media_ids': media_id})

    if r.status_code == 200:
        print("Weather update success for {}".format(city))
    else:
        print("Unable to post weather update for {}".format(city))




def loadConfig():
    optlist, args = getopt.getopt(sys.argv[1:], ':c:')
    if len(optlist) > 0 and optlist[0][0] == '-c':
        config_file = optlist[0][1]
    else:
        config_file = 'config/api_keys'

    config = configparser.ConfigParser()
    config.read(config_file)

    return config

def load_twitter_api(config):
    consumer_key = config.get('Twitter', 'consumer_key')
    consumer_secret = config.get('Twitter', 'consumer_secret')
    access_token_key = config.get('Twitter', 'access_token_key')
    access_token_secret = config.get('Twitter', 'access_token_secret')

    twitterAPI = TwitterAPI(consumer_key,
                            consumer_secret,
                            access_token_key,
                            access_token_secret)

    return twitterAPI

def load_open_weather_api(config):
    weatherAPI = config.get('OpenWeatherMap', 'apiKey')
    owm = pyowm.OWM(weatherAPI)
    return owm

def load_cities():
    cities = []
    with open('data/cities.csv', 'r') as f:
        for x in f:
            # x = x.encode('utf-8').strip()
            x = x.rstrip()
            parts = x.split(",")
            cities.append(parts[0].strip() + ", " + parts[1])

    return cities


if __name__ == '__main__':
    config = loadConfig()

    twitter_api = load_twitter_api(config)
    open_weather_api = load_open_weather_api(config)

    cities = load_cities()

    generate_weather_tweets(twitter_api, open_weather_api, cities)


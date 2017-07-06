import random

def get_hot_tuples(tempC, tempF, city):
    result = []
    result.append(('{} Degrees F in {}?'.format(tempF, city), 'BOOOOO! NOT COOL!', 'head_boo.png'))
    result.append(('{} Degrees F in {}?'.format(tempF, city), 'Woweeeeeee! Sure is getting toasty!', 'wowee.jpg'))
    result.append(('{} Degrees F in {} again?'.format(tempF, city),'Thanks a lot, SUMMER','thanks_summer.jpg'))
    result.append(('{} Degrees F in {} again?'.format(tempF, city),'It\'s time to get schweaty in here','schwifty.png'))
    result.append(('{} Degrees F in {}?'.format(tempF, city),'So how familiar are you with non-brimstone climates, exactly?','gearhead.jpg'))
    result.append(('{} Degrees F in {}?'.format(tempF, city), 'KEEP SUMMER SAFE','summer_safe.jpg'))
    result.append(('{} Degrees F in {}?  Alright sun....'.format(tempF, city), 'You\'re growing into a real big thorn right up into my ass', 'thorn.jpg'))
    result.append(('{} Degrees F in {}?'.format(tempF, city), 'Just send me to Canada. I want to be with the cold.', 'garry.png'))
    result.append(('Pleasantly cool outdoor weather?', 'Oh we\'re well past that {}'.format(city), 'past_that.png'))
    result.append(('{} Degrees F in {}?'.format(tempF, city), 'I don\'t get nice weather and I don\'t need to', 'dont_need_to.jpg'))
    result.append(('{} Degrees F in {}?'.format(tempF, city), 'That just sounds like normal weather, but with extra sweat', 'slavery.jpg'))
    result.append(('{} Degrees F in {}?'.format(tempF, city), 'My body is dying in a vat under the sun', 'tiny_rick_sings.jpg'))
    result.append(('{} Degrees F in {} again?'.format(tempF,city),'In bird culture this is considered a dick move','birdperson.jpg'))
    result.append(('{} Degrees F in {} again?'.format(tempF,city),'I JUST WANNA DIE!','want_to_die.jpg'))
    result.append(('{} Degrees F in {}?'.format(tempF,city), 'Oh jeez Rick...','oh-geez-rick.jpg'))
    return result


def get_nice_weather_tuples(tempC, tempF, city):
    result = []
    result.append(('{} Degrees F in {}?'.format(tempF, city), 'I LIKE WHAT YOU GOT','goodjob.png'))
    result.append(('{} Degrees F and nice outside in {}?'.format(tempF, city), 'Five more minutes of this and I\'m gonna get mad','gonna_get_mad.png'))
    result.append(('When you want to go outside but it\'s {} Degrees F in {}'.format(tempF, city),'','jerry.png'))
    result.append(('When you thought it would be nice today but it\'s {} Degrees F in {}'.format(tempF, city),'','sun.jpg'))
    result.append(('When you want to go outside but it\'s {} Degrees F in {}'.format(tempF, city),'','go_outside.jpg'))
    result.append(('{} Degrees C in {}?'.format(tempC,city), 'I-I-I don\'t even know is that a lot? Is that a little?', 'is_that_a_lot.jpg'))
    result.append(('{} Degrees F in {}'.format(tempF,city),'And that\'s the way the news goes'.format(tempF,city),'news_goes.jpg'))
    result.append(('{} Degrees F in {}?'.format(tempF,city), 'YES','yes.png'))

    return result


def get_cold_weather_tuples(tempC, tempF, city):
    result = []
    result.append(('{} Degrees F in {}?'.format(tempF,city), 'Woweeeeeee! Sure is getting chilly!', 'wowee.jpg'))
    result.append(('{} Degrees F in {}?'.format(tempF,city), 'I\'m not Looking for judgement, just a yes or a no. Am I ever going to see the sun again?','assimilate.jpg'))
    result.append(('{} Degrees F in {}?'.format(tempF, city),'Isn\'t it obvious Morty? I froze them','frozethem.jpg'))
    return result


def get_clear_weather_tuples(tempC, tempF, city):
    result = []
    result.append(('Clear skies in {} today!'.format(city), 'LOOKING GOOD', 'looking_good.jpg'))
    result.append(('Not raining in {} today!'.format(city), 'Don\'t even drip, dawg', 'dawg.jpg'))
    result.append(('{} Degrees F and clear skies in {}?'.format(tempF, city), 'Ooooooohhhhhh can doo!', 'can_do.jpg'))
    result.append(('{} Degrees F and clear skies in {}?'.format(tempF, city), 'Nice Miss Pancakes, real nice!', 'pancakes.jpg'))

    return result


def get_snow_weather_tuples(tempC, tempF, city):
    result = []
    result.append(('{} was my slave name'.format(city), 'You can call me snowball because everything is covered in snow and frozen','where_are_my_testicles.jpg'))
    return result


def get_cloud_tuples(tempC, tempF, city):
    result = []

    result.append(('Cloudy in {} again?'.format(city), 'I\'m bummed I didn\'t get to give that sun a try','alien.jpg'))
    result.append(('Cloudy in {} again?'.format(city), 'There is no sun, Summer; gotta rip that band-aid off now you\'ll thank me later','nogod.jpg'))
    result.append(('Cloudy in {} again?'.format(city), 'Snuffles want to see the sun again. Snuffles need to see the sun again.','snufflesWants.jpg'))
    result.append(('Cloudy again in {} again?'.format(city),'Where is my sun, {}?'.format(city),'where_are_my_testicles.jpg'))
    return result


def get_rain_tuples(tempC, tempF, city):
    result = []

    result.append(('', 'It\'s about to Riggity Riggity Rain in {}!'.format(city), 'riggity.jpg'))
    result.append(('', 'Oh boy here I go raining in {} again'.format(city), 'killing.jpg'))
    result.append(('I\'d like to order a large Rain with extra water for {}'.format(city), 'Actually make it a monsoon. No, a flood!', 'pizza.png'))
    result.append(('It doesn\'t usually rain for this long in {}.'.format(city), '', 'getting_weird.jpg'))
    result.append(('Now look {} is going to be dealing with some real serious stuff today.'.format(city),'You might have heard of it it\'s called RAIN','math.png'))
    result.append(('Would you like to ride the rain train, {}?'.format(city),'','rain_train.jpg'))
    result.append(('What is my purpose in life? nYou\'re from {}, you sit in the rain.'.format(city),'Oh my God','butter.png'))

    return result

# Known values: Clear,Clouds,Haze,Rain

#unused images:
#drunk.png, Fart.jpg, ice_t.jpg, one_true_morty.jpg, praying.jpg, rap.jpg, north_pole.png, santa.jpg, sun.jpg


def test_driver():
    tempC = 75
    tempF = 75
    city = 'Dallas, TX'

    options = []
    options.extend(get_cold_weather_tuples(tempC,tempF,city))
    options.extend(get_nice_weather_tuples(tempC, tempF, city))
    options.extend(get_hot_tuples(tempC, tempF, city))
    options.extend(get_clear_weather_tuples(tempC, tempF, city))
    options.extend(get_rain_tuples(tempC, tempF,city))
    options.extend(get_cloud_tuples(tempC,tempF,city))
    options.extend(get_snow_weather_tuples(tempC, tempF, city))

    return options

def get_strings(status, tempF, tempC, city):
    options = []

    if tempF < 40:
        options.extend(get_cold_weather_tuples(tempC,tempF,city))
    elif tempF < 75:
        options.extend(get_nice_weather_tuples(tempC, tempF,city))
    else:
        options.extend(get_hot_tuples(tempC,tempF,city))

    if status == 'Clear':
        options.extend(get_clear_weather_tuples(tempC,tempF,city))
    elif status == 'Rain':
        options.extend(get_rain_tuples(tempC, tempF,city))
    elif status == 'Haze':
        pass
    elif status == 'Clouds':
        options.extend(get_cloud_tuples(tempC,tempF,city))
    elif status == 'Snow':
        options.extend(get_snow_weather_tuples(tempC,tempF,city))
    if len(options) == 0:
        return None

    return random.choice(options)

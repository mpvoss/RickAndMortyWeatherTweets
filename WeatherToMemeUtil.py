import random

hot_strings = [
    ('{} Degrees F in {}?', 'BOOOOO! NOT COOL!', 'head_boo.png'),
    ('{} Degrees F in {}?', 'Woweeeeeee! Sure is getting toasty!', 'wowee.jpg')
]

# tepid_strings_C = [
#     ('{} Degrees C in {}?', 'I-I-I don\'t even know is that a lot? Is that a little?', 'is_that_a_lot.jpg')
#
# ]
# tepid_strings_F = [
# ('{} Degrees F and clear skies in {}?','Ooooooohhhhhh can doo!','can_do.jpg')
# ]

# Cold
cold_strings = [
    ('{} Degrees F in {}?', 'Woweeeeeee! Sure is getting chilly!', 'wowee.jpg'),
    ('{} Degrees F in {}?', 'I\'m not Looking for judgement, just a yes or a no. Am I ever going to see the sun again?',
     'assimilate.jpg')

]

# 15 Degrees F in _______? Isn't it obvious Morty? I Froze him"

# Nice Temperature
# Nice Ms Pancakes. Real nice.


# Condition: Snow
# Snowing again in ______?  In bird culture that is considered a jerk move
# Snowing again in ______? I JUST WANNA DIE! (Meseeks)
# More snow in _____? Oh geez Rick
# Snuffles was my slave name, you can call me snowball because my fur is pretty and white.

# Condition: Cloud
# What is my purpose in life? \n You're from _____, you sit in the rain\n Oh my god
# Where is my Sun, {City name} Dog meme with testicles
# Fart monster?
# Cloudy in ______ again? I'm bummed I didn't get to give that sun a try
# Cloudy in ______ again? There is no sun, Summer; gotta rip that band-aid off now you'll thank me later
# Cloudy in ______ again? Snuffles want to see the sun again. Snuffles need to see the sun again.


# Condition: Rain
rain_strings = [
    ('', 'It\'s about to Riggity Riggity Rain in {}!', 'riggity.jpg'),
    ('', 'Oh boy here I go raining in {} again', 'killing.jpg'),
    ('I\'d like to order a large Rain with extra water for {}', 'Actually make it a monsoon. No, a flood!', 'pizza.png'),
    ('It doesn\'t usually rain for this long in {}.', '', 'getting_weird.jpg')

]


# Known values: Clear,Clouds,Haze,Rain


def buildListOneLine(text,list):
    result = []
    for string in list:
        line1 = string[0].format(text)
        line2 = string[1].format(text)
        result.append((line1, line2, string[2]))

    return result



def get_strings(status, tempF, tempC, city):
    options = []

    if tempF < 40:
        for string in cold_strings:
            line1 = string[0].format(tempF, city)
            line2 = string[1]
            options.append((line1, line2, string[2]))

    # elif tempF > 80:
    #     for string in hot_strings:
    #         line1 = string[0].format(tempF, city)
    #         line2 = string[1]
    #         options.append((line1, line2, string[2]))

    # else:
    #     for string in tepid_strings_C:
    #         line1 = string[0].format(tempC, city)
    #         line2 = string[1]
    #         options.append((line1, line2, string[2]))
        # for string in tepid_strings_F:
        #     line1 = string[0].format(tempF, city)
        #     line2 = string[1]
        #     options.append((line1, line2, string[2]))

    if status == 'Clear':
        pass
    elif status == 'Rain':
        # options.extend(buildListOneLine(city,rain_strings))
        pass
    elif status == 'Haze':
        pass
    elif status == 'Clouds':
        pass

    if len(options) == 0:
        return None
    return random.choice(options)




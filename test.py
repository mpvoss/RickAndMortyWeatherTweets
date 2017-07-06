import WeatherToMemeUtil
from memegenerator import memegenerator

things = WeatherToMemeUtil.test_driver()
for meme_tuple in things:

    print(meme_tuple)
    filename = memegenerator.make_meme(meme_tuple[0], meme_tuple[1], 'img/' + meme_tuple[2])

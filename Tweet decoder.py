'''The following program decodes a few common abbreviations in online communication such as messages
in Twitter ("tweets") or email, and provides the corresponding English phrase.
'''
# tweet = input('Enter abbreviation from tweet:\n')
#
# if tweet == 'LOL':
#     print('LOL = laughing out loud')
# elif tweet == 'BFN':
#     print('BFN = bye for now')
# elif tweet == 'FTW':
#     print('FTW = for the win')
# elif tweet == 'IRL':
#     print('IRL = in real life')
# elif tweet == 'BFFR':
#     print('BFFR = be freakin for real')
# elif tweet == 'ikyfl':
#     print('ikyfl = I know you\'re freaking lying')
# elif tweet == 'GURL':
#     print('GURL = GIRL')
# else:
#     print("Sorry, don't know that one")

abbreviations = {
    'LOL': 'laughing out loud',
    'BFN': 'bye for now',
    'FTW': 'the win',
    'IRL': 'in real life',
    'BFFR': 'be freakin for real',
    'ikyfl': 'I know you\'re freaking lying',
    'GURL': 'GIRL'
}

custom_tweet = input('Enter your tweet (less than 160 characters:\n')
if len(custom_tweet) <= 160:
    for abbreviation in abbreviations:
        if abbreviation in custom_tweet:
            print(abbreviations[abbreviation])
else:
    print('Tweet too long')


''' 1. Expand the number of abbreviations that can be decoded. Add support for abbreviations you 
    commonly use or search the internet for some.
    2. Allow the user to enter a complete tweet (160 characters or less) as a single line of text. 
    Search the resulting string for abbreviations and print a list of each abbreviation along with its decoded meaning.'''
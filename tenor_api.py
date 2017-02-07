"""
Tenor GIF API Python Wrapper
"""

import urllib.parse
import requests
from settings import API_KEY
from static import *

def parse_code(item, codemap, default=None):
    try:
        return codemap[item]
    except KeyError:
        for key in codemap:
            if item in key:
                return codemap[item]
    return default

def parse_locale(locale):
    try:
        lang, country = locale.split('_')
    except ValueError:
        lang = locale.lower()
        country = ''

    if lang not in LANGUAGE_CODES:
        lang = parse_code(lang, LANGUAGE_CODEMAP, 'en')
    if country:
        country = parse_code(country, COUNTRY_CODEMAP, 'US')
        return '_'.join([lang, country])
    return lang


def gif_search(tag,
               country=None,
               limit=20,
               locale='en_US',
               pos=None,
               safesearch='off'):

    """
    search for gifs by tags

    params:

    tag: string:
         tag or search string
    country: string: format YY
             2 character uppercase country code; default None
    limit: int:
           number of results; default 20; max 50
    locale: string: format xx_YY
            xx 2 character lowercase language;
            YY (optional) 2 character country code
    pos: string/float/int:
         get results starting at position "value"
         Use a non-zero "next" value returned by API results to get the next set of results
         pos is not an index and may be an integer, float, or string
    safesearch: string:
         (values:off|moderate|strict) specify the content safety filter level
    """

    safesearch = safesearch.lower()
    
    if country:
        country = country.upper().strip()
        if country not in COUNTRY_CODES:
            country = parse_code(country, COUNTRY_CODEMAP)

    if safesearch not in ('off', 'moderate', 'strict'):
        safesearch = 'off'

    tag = urllib.parse.quote(tag, safe='/:)({}')

    locale = parse_locale(locale)

    limit = max(1, min(limit, 50))

    base_url = 'https://api.tenor.co/v1/search'
    params = {'tag': tag,
              'key': API_KEY,
              'country': country,
              'limit': limit,
              'locale': locale,
              'pos': pos,
              'safesearch': safesearch}
    req = requests.get(base_url, params=params)
    req.raise_for_status()

    return req.json()
    
def get_tags(type_='featured'):
    """
    Get a list of popular or promoted tags and categories.

    params:
    type: string:
          default featured;
          specify a category of tags to retrieve.
          Possible values: "featured", "explore".
          Multiple types can be specified, each type separated with a comma
    """

    base_url = 'https://api.tenor.co/v1/tags'

    type_ = set(type_.lower().strip().split(','))
    type_ = ','.join([item for item in type_ if item in ('featured', 'explore')])

    params = {'type': type_,
              'key': API_KEY}

    req = requests.get(base_url, params=params)
    req.raise_for_status()

    return req.json()

def get_trending(limit=20, pos=None):
    """
    Get trending, popular, and promoted GIFs and Videos.
    """

    base_url = 'https://api.tenor.co/v1/trending'
    limit = max(1, min(50, limit))
    params = {'key': API_KEY,
              'limit': limit,
              'pos': pos}

    req = requests.get(base_url, params=params)
    req.raise_for_status()

    return req.json()

def get_video(limit=20, pos=None):
    """
    Get popular video clips
    """
    base_url = 'https://api.tenor.co/v1/music'
    limit = max(1, min(50, limit))
    params = {'key': API_KEY,
              'limit': limit,
              'pos': pos}

    req = requests.get(base_url, params=params)
    req.raise_for_status()

    return req.json()

def get_gifs(ids):
    """
    Get GIFs by their IDs.

    params:
    ids: string:
    a comma separated list of GIF IDs (max: 50)
    eg: "5079878,4900007"
    """

    base_url = 'https://api.tenor.co/v1/gifs'
    params = {'key': API_KEY,
              'ids': ids}
    
    req = requests.get(base_url, params=params)
    req.raise_for_status()

    return req.json()

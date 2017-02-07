# Tenor GIF API

A Python Wrapper for the Tenor GIF API.


## Instructions

Create a copy of `example_settings.py` and edit it with your API key. Rename the copied file to `settings.py`

## Usage

```python
>>> import tenor_api
>>> from pprint import pprint
>>> pprint(tenor_api.get_trending(limit=1))

{'next': '1486467413.213124',
'results': [{'composite': None,
            'created': 1459886932.417291,
            'hasaudio': False,
            'id': '5296323',
            'itemurl': 'https://www.tenor.co/view/tired-yawn-boring-gif-5296323',
            'media': [{'gif': {'dims': [373, 498],
                                'preview': 'https://media.tenor.co/images/22030681235fd3230b13d7eec504f842/raw',
                .
                .
                .
                
            'shares': 209477,
            'tags': [],
            'title': '',
            'url': 'https://tenor.co/wnYJ.gif'}]}

>>> pprint(tenor_api.gif_search('hola :)', limit=1, safesearch='moderate'))
{'next': '1',
'results': [{'composite': None,
            'created': 1424133230.556408,
            'hasaudio': True,
            'hascaption': True,
            'id': '3790320',
            'itemurl': 'https://www.tenor.co/view/markiplier-gif-3790320',
            'media': [{'gif': {'dims': [498, 280],
            .
            .
            .

            'shares': 910,
            'tags': [],
            'title': '20/20/20/20',
            'url': 'https://tenor.co/p4cm.gif'}],
'weburl': 'https://www.tenor.co/search/hola%20:)-gifs'}
```
import urllib.parse
import pyproj

from services.downloader import Downloader
from services.mercator import Mercator
from services.writer import Writer

BASE_URL = 'https://services6.arcgis.com'
URL = '/NThLsKaeOKhGxBBE/arcgis/rest/services/Skyddsrum_220225/FeatureServer/0/query'

QUERY_PARAMETERS = {
    'f': 'json',
    'cacheHint': True,
    'maxRecordCountFactor': 4,
    'resultOffset': 16000,
    'resultRecordCount': 8000,
    'where': '1=1',
    'orderByFields': 'OBJECTID',
    'outFields': 'OBJECTID,Gatuadress,Kommunnamn,AntalPlatser,Skyddsrumsnr',
    'outSR': 102100,
    'spatialRel': 'esriSpatialRelIntersects'
}

query = '{}{}?{}'.format(BASE_URL, URL,
                         urllib.parse.urlencode(QUERY_PARAMETERS))

print('Downloading the data...')
data = Downloader.get_json(query)

skyddsrum = []
skyddsrum_geojson = {'type': 'FeatureCollection', 'features': []}

print('Converting the data...')
for feature in data['features']:
    long, lat = Mercator.convert(feature['geometry']['x'],
                                 feature['geometry']['y'])
    skyddsrum.append({
        'id': feature['attributes']['OBJECTID'],
        'skyddsrumsnr': feature['attributes']['Skyddsrumsnr'],
        'gatuadress': feature['attributes']['Gatuadress'],
        'kommunnamn': feature['attributes']['Kommunnamn'],
        'antalplatser': feature['attributes']['AntalPlatser'],
        'latitude': lat,
        'longitude': long
    })

    skyddsrum_geojson['features'].append({
        "type": "Feature",
        "properties": {
            'id': feature['attributes']['OBJECTID'],
            'skyddsrumsnr': feature['attributes']['Skyddsrumsnr'],
            'gatuadress': feature['attributes']['Gatuadress'],
            'kommunnamn': feature['attributes']['Kommunnamn'],
            'antalplatser': feature['attributes']['AntalPlatser']
        },
        "geometry": {
            "type": "Point",
            "coordinates": [lat, long]
        }
    })

print('Writing the data...')
#Writer.write_json(data, 'data.json')
Writer.write_json(skyddsrum, 'skyddsrum.json')
Writer.write_json(skyddsrum_geojson, 'skyddsrum.geojson')
Writer.write_csv(skyddsrum, 'skyddsrum.csv')

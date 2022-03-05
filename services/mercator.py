import pyproj

INPROJ = pyproj.Proj('epsg:3857')
OUTPROJ = pyproj.Proj('epsg:4326')


class Mercator(object):
    def convert(x, y):
        return pyproj.transform(INPROJ, OUTPROJ, x, y)

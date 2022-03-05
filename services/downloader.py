import json
import time
import urllib.request


class Downloader(object):
    @staticmethod
    def get(url):
        try:
            return urllib.request.urlopen(url).read()
        except urllib.error.HTTPError as err:
            print(f'ERROR {err.code}: Could not download {url}.')
            if (err.code == 403):
                print('Retrying in 10 seconds')
                time.sleep(10)
                return Downloader.get(url)
            else:
                print('Permanent error: skipping this center')
                return None

    def get_json(url):
        return json.loads(Downloader.get(url).decode('utf-8'))

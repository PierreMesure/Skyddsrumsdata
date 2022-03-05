import csv
import json


class Writer(object):
    @staticmethod
    def write_csv(list, filename):
        keys = list[0].keys()

        with open(filename, 'w', newline='') as file:
            dict_writer = csv.DictWriter(file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(list)

    def write_json(dict, filename):
        with open(filename, 'w') as file:
            json_string = json.dumps(dict, ensure_ascii=False,
                                     indent=4).encode('utf-8')
            file.write(json_string.decode())

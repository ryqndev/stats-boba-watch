import os.path
import os
import errno
import json
import datetime


class Cleanse(object):
    def __init__(self):
        return

    def cleanse_drinks(self, file_location):
        data = []
        date = {}
        name = {}
        location = {}
        price = {}
        with open(os.path.dirname(__file__) + file_location) as fp:
            for (i, line) in enumerate(fp):
                line = json.loads(line)
                line = line['drink']
                del line['__key__']
                del line['description']

                data.append(line)
                self.add_to_map(self.clean_name(line['name']), name)
                self.add_to_map(self.clean_date(line['date']), date)
                self.add_to_map(self.clean_location(line['location']), location)
                self.add_to_map(line['price'], price)
            # data = json.load(fp)
            # for drink in data:
            #     self.add_to_map(data.name)

        with open(os.path.dirname(__file__) + '/../raw_data/parsed2019-12-03T22_23_031', 'w') as fp:
                json.dump(data, fp, sort_keys=True, indent=4)
        with open(os.path.dirname(__file__) + '/../data/2/name.json', 'w') as fp:
                json.dump(name, fp, sort_keys=True, indent=4)
        with open(os.path.dirname(__file__) + '/../data/2/date.json', 'w') as fp:
                json.dump(date, fp, sort_keys=True, indent=4)
        with open(os.path.dirname(__file__) + '/../data/2/loc.json', 'w') as fp:
                json.dump(location, fp, sort_keys=True, indent=4)
        with open(os.path.dirname(__file__) + '/../data/2/price.json', 'w') as fp:
                json.dump(price, fp, sort_keys=True, indent=4)

    def clean_name(self, name):
        return name.strip().lower()

    def clean_date(self, date):
        return date[0:13]

    def clean_location(self, location):
        return location.strip().lower()

    def add_to_map(self, val, map_name):
        if val in map_name:
            map_name[val] += 1
        else:
            map_name[val] = 1

if __name__ == "__main__":
    cleanse = Cleanse()
    cleanse.cleanse_drinks('/../raw_data/parsed2019-12-03T22_23_031')

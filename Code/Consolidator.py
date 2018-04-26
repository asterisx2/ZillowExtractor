import json
from pprint import pprint


class Consoliator():

    def setUp(self):
        addresses = json.load(open('Addresses.json'))
        data = json.load(open('Data.json'))
        tax = json.load(open('Tax.json'))
        return [addresses, data, tax]

    #def consolidateTax(self, data, tax):

    #def consolidateAddress(self, data, addresses):

    #def consolidate(self, data, tax, addresses):

    #def write(self, data):
     #   import json
      #  with open('main.json', 'w') as outfile:
       #     json.dump(data, outfile)
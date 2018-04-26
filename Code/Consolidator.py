import json
from pprint import pprint


class Consoliator():

    def setUp(self):
        import os
        os.chdir(os.path.dirname(__file__))
        print(os.getcwd())
        a = open(os.getcwd()+'\Addresses.json', 'r')
        d = open(os.getcwd() + '\Data.json', 'r')
        t = open(os.getcwd()+'\Tax.json','r')
        addresses = json.load(a)
        data = json.load(d)
        tax = json.load(t)

        a.close()
        d.close()
        t.close()
        return [addresses, data, tax]

    def consolidateTax(self, data, tax):
        for d in data:
            if d['FIELD1'] == 'zpid':
                continue
            zpid = d['FIELD1']
            for t in tax:
                if t['FIELD1'] == zpid:
                    for i in range(2, 20):
                        d['Tax'+tax[0]['FIELD'+str(i)]] = t['FIELD'+str(i)]
                    break
        print(data[1])
        with open('consolidated.json', 'w') as fp:
            json.dump(data, fp)
        return data

    #def consolidateAddress(self, data, addresses):

    #def consolidate(self, data, tax, addresses):

    #def write(self, data):
     #   import json
      #  with open('main.json', 'w') as outfile:
       #     json.dump(data, outfile)
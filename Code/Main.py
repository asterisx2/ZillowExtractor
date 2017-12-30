from Utils import Utils
import ZillowApiWorker
import urllib.parse
import CSVHelper

utils = Utils()
apiWorker = ZillowApiWorker
zpids = []
results = []

def encode(val):
    return urllib.parse.quote_plus(val)

def getAddresses():
    global addresses
    addresses = utils.getVals("Addresses.txt",",")

def run(links, results, vals):
    get_zpids(links, vals)
    get_results(links, results)


def get_results(zpids, results):
    for zpid in zpids:
        r = apiWorker.getProperty(zpid)
        if (r != None):
            results += r


def get_zpids(zpids, addresses):
    for address in addresses:
        r = ZillowApiWorker.getZpids(encode(address[0]), encode(address[1] + "IL"))
        if (r != None):
            zpids += r

getAddresses()
get_zpids(zpids, addresses)
results += '<?xml version="1.0" encoding="utf-8"?><Properties>'
get_results(zpids, results)
results += '</Properties>'
f =  open("export.xml", "wb")
f.write(results)
f.close()
CSVHelper.saveToCsv("export.csv",results)


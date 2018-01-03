from Utils import Utils
import ZillowApiWorker
import urllib.parse
import CSVHelper

utils = Utils()
apiWorker = ZillowApiWorker
zpids = set()
results = []
noGood= []
comparableProperties = 5

def encode(val):
    return urllib.parse.quote_plus(val)

def getAddresses():
    global addresses
    addresses = utils.getVals("Addresses.txt",",")

def run(links, results, vals):
    get_zpids(links, vals)
    get_results(links, results)


def get_results(zpids, results):
    results.append('<?xml version="1.0" encoding="utf-8"?><Properties>')
    for zpid in zpids:
        r = apiWorker.getProperty(zpid)
        results .append(r)
    results.append('</Properties>')



def get_zpids(zpids, addresses):
    for address in addresses:
        retSet = ZillowApiWorker.getZpids(encode(address[0]), encode(address[1] + "IL"))
        if not retSet:
            print("No results for " + address[3])
            noGood.append(address[3])
        else:
            for ret in retSet:
                zpids.add(ret)
                retSetComp = ZillowApiWorker.getDeepComps(ret,comparableProperties)
                for retComp in retSetComp:
                    zpids.add(retComp)

def save_results():
    string = ""
    for result in results:
        string += result
    f = open("export.xml", "w")
    f.write(str(string))
    f.close()

def save_NoGood(noGood):
    f = open("NoGood.txt", "w")
    for ng in noGood:
        f.write(ng )
    f.close();


getAddresses()
get_zpids(zpids, addresses)
save_NoGood(noGood)
get_results(zpids, results)
save_results()
#CSVHelper.saveToCsv("export.csv",results)


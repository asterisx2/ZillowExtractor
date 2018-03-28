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
addresses = []

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
        r = apiWorker.getProperty(zpid[0],zpid[1])
        if r:
            results.append(r)

def get_zpids(zpids, addresses):
    for address in addresses:
        retSet = ZillowApiWorker.getZpids(encode(address[0]), encode(address[1] + ", IL, "+address[2]))
        if not retSet:
            #print("No results for " + address[1] + ", IL, "+address[2])
            noGood.append(address[1] + ", IL, "+address[2])
        else:
            for ret in retSet:
                zpids.add((ret, address[3]))
                #retSetComp = ZillowApiWorker.getDeepComps(ret,comparableProperties)
                #for retComp in retSetComp:
                 #   zpids.add(retComp)

def save_results():
    string = "<Properties>"
    for result in results:
        string += result
    string = string + "</Properties>";
    f = open("export.xml", "w")
    f.write(str(string))
    f.close()

def save_NoGood(noGood):
    f = open("NoGood.txt", "w")
    for ng in noGood:
        f.write(ng )
    f.close();


getAddresses()
#print(addresses)
get_zpids(zpids, addresses)
#print(zpids)
save_NoGood(noGood)
get_results(zpids, results)
save_results()
#CSVHelper.saveToCsv("export.csv",results)


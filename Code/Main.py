from Utils import Utils
from ZillowApiWorker import ZillowApiWorker
from PageExtractor import PageExtractor
import urllib.parse

utils = Utils()
apiWorker = ZillowApiWorker()
links = []
results = []
pageExtractor = PageExtractor()
def encode(val):
    return urllib.parse.quote_plus(val)

def getAddresses():
    global addresses
    addresses = utils.getVals("Addresses.txt",",")



def run(links, results, vals):
    get_links(links, vals)
    get_results(links, results)


def get_results(links, results):
    for link in links:
        r = pageExtractor.execute(link)
        if (r != None):
            results += r


def get_links(links, addresses):
    for address in addresses:
        r = apiWorker.makeRequest(encode(address[0]), encode(address[1] + "IL"))
        if (r != None):
            links += r


#Test for one url
turl = "http://www.zillow.com/webservice/GetSearchResults.htm?zws-id=X1-ZWz18wdrv6sq2z_3bebs&address=2033+N+HOWE+ST&citystatezip=Chicago%2C+IL"
r = apiWorker.makeRequest("2033+N+HOWE+ST","Chicago%2C+IL")
print(r)
#Stepping stone tests
#getAddresses()
#print(addresses)
#get_links(links, addresses)
#print(links)

#Main run
#run(links, results, vals)
#print(results)
import urllib.request as urllib
from lxml import etree


zillowId = "X1-ZWz18wdrv6sq2z_3bebs"
linksUrl = "http://www.zillow.com/webservice/GetSearchResults.htm?zws-id=" + zillowId + "&address="
propertyUrl = "http://www.zillow.com/webservice/GetUpdatedPropertyDetails.htm?zws-id="+zillowId+"&zpid="
deepCompsUrl = "http://www.zillow.com/webservice/GetDeepComps.htm?zws-id=" + zillowId

def printNode(node):
    print(etree.tostring(node, pretty_print=True))

def getProperty(zpid):
    url = propertyUrl + zpid;
    xml = urllib.urlopen(url).read()
    #print(xml)
    xml = xml.decode('utf-8')
    if(str(xml).find("<code>0</code>")!=-1):
        return str(xml).replace('<?xml version="1.0" encoding="utf-8"?>','')
    else:
        return None

def getZpids(address, citystatezip):
    url = linksUrl + address + "&citystatezip=" + citystatezip
    file = urllib.urlopen(url)
    data = file
    xmldoc = etree.parse(data)
    file.close()
    results = xmldoc.xpath("/SearchResults:searchresults/response/results/result", namespaces = {
        'SearchResults': 'http://www.zillow.com/static/xsd/SearchResults.xsd'
    })
    zpids = []
    for result in results:
        zpid = result.xpath("zpid", namespaces = {
        'zpid': 'http://www.zillow.com/static/xsd/SearchResults.xsd'
    })[0]
        print("[API]Found Property ZPID: "+zpid.text)
        zpids.append(zpid.text)
    return zpids

def getDeepComps(zpid, count):
    url = deepCompsUrl + "&zpid="+zpid+"&count="+str(count)
    file = urllib.urlopen(url)
    data = file
    xmldoc = etree.parse(data)
    file.close()

    comps = xmldoc.xpath("/Comps:comps/response/properties/comparables/comp", namespaces={
        'Comps': 'http://www.zillow.com/static/xsd/Comps.xsd'
    })
    zpids = []
    for comp in comps:
        zpid = comp.xpath("zpid", namespaces={
            'zpid': 'http://www.zillow.com/static/xsd/SearchResults.xsd'
        })[0]
        print("[API][COMPARABLE]Found Property ZPID: " + zpid.text)
        zpids.append(zpid.text)
    return zpids



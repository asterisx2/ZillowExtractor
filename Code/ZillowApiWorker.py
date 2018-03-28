import urllib.request as urllib
from lxml import etree


zillowId = ["X1-ZWz18wdrv6sq2z_3bebs","X1-ZWz1gat6yv2z2j_4ok8b","X1-ZWz1gasfcfi7ez_44w9p","X1-ZWz18pq1m04q2z_46au6"]
linksUrl = "https://www.zillow.com/webservice/GetSearchResults.htm?zws-id="
propertyUrl = "https://www.zillow.com/webservice/GetUpdatedPropertyDetails.htm?zws-id="
deepCompsUrl = "https://www.zillow.com/webservice/GetDeepComps.htm?zws-id="

c = 0;

def getUrl(baseUrl, param, value):
    global c
    c = c+1
    return baseUrl + zillowId[c%len(zillowId)] + "&" +  param +  "=" + value

def printNode(node):
    print(etree.tostring(node, pretty_print=True))

def getProperty(zpid, price):
    url = getUrl(propertyUrl, "zpid", zpid);
    xml = urllib.urlopen(url).read()
    #print('[PROPERTY] Fetching '+zpid)
    xml = xml.decode('utf-8')
    p = "<zestimate>" + str(price) + "</zestimate>"
    if(str(xml).find("<code>0</code>")!=-1):
        xml = str(xml).replace('<?xml version="1.0" encoding="utf-8"?>','').replace("</response></UpdatedPropertyDetails:updatedPropertyDetails>", p+"</response></UpdatedPropertyDetails:updatedPropertyDetails>")
        xml = xml.replace("UpdatedPropertyDetails:updatedPropertyDetails","Property")
        return xml
    else:
        return None

def getZpids(address, citystatezip):
    url = getUrl(linksUrl, "address", address) + "&citystatezip=" + citystatezip
    file = urllib.urlopen(url)
    data = file
    xmldoc = etree.parse(data)
    file.close()
    #print(url)
    results = xmldoc.xpath("/SearchResults:searchresults/response/results/result", namespaces = {
        'SearchResults': 'http://www.zillow.com/static/xsd/SearchResults.xsd'
    })
    zpids = []
    for result in results:
        zpid = result.xpath("zpid", namespaces = {
        'zpid': 'http://www.zillow.com/static/xsd/SearchResults.xsd'
    })[0]
        #print("[API]Found Property ZPID: "+zpid.text)
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



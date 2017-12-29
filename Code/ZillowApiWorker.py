import urllib.request as urllib
from lxml import html
class ZillowApiWorker:
    zillowId = "X1-ZWz18wdrv6sq2z_3bebs"
    baseUrl = "http://www.zillow.com/webservice/GetSearchResults.htm?zws-id=" + zillowId + "&address="

    def makeRequest(self, address, citystatezip):
        url = self.baseUrl + address + "&citystatezip=" + citystatezip
        print("Making Api Request: "+url)
        try:
            xml = html.fromstring(urllib.urlopen(url).read())
            results = xml.xpath("/SearchResults:searchresults/response/results/result")
            links = []

            for result in results:
                links.append(result.xpath("/links/homedetails").text)
                return links

        except:
            return
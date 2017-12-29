import urllib.request as urllib
from lxml import html

class PageExtractor:
    "This class contains methods which extract data from the property's listing page. You can create multiple instances of this class and multihread your extractions"

    def execute(self, url):
        print("Fetching Data From: "+url)
        dataDictionary = {}
        page = self.__getPage(url)
        self.__getValuesUnderHeader_FactsFeatures(page, dataDictionary)
        self.__getValuesUnderHeader_ForSale(page, dataDictionary)
        self.__get_pairedValues(page, dataDictionary)
        return dataDictionary

    def __getPage(url):
        return html.fromstring(urllib.urlopen(url).read())

    def __getValuesUnderHeader_ForSale(html, dictionary, identifiers):
        div = html.xpath('div[@id="home-value-wrapper"]')
        dictionary['FOR SALE'] = div.xpath('div[@class="estimates"]/div[2]').text;
        dictionary['Zestimate'] = div.xpath('div[@class="estimates"]/div[3]/span[2]').text
        dictionary['Est. Mortgage'] = div.xpath('div[@class="loan-calculator-container"]/div[2]/div[2]/div/div/section/span/span').text

    def __getValuesUnderHeader_FactsFeatures(html, dictionary, identifiers):
        divs = html.xpath('div[@class="zsg-lg-1-3 zsg-md-1-2"]')

        for aDiv in divs:
            dictionary[aDiv.xpath('div[@class="zsg-media-bd"]/p').text] = aDiv.xpath('div[@class="zsg-media-bd"]/div').text

    def __get_pairedValues(html, dictionary):
        div = html.xpath('div[@class="z-moreless-content hdp-fact-moreless-content"]')
        lis = div.xpath("li")

        for li in lis:
            pair = li.text.split(":")
            pair[0].strip()
            pair[1].strip()
            dictionary[pair[0]] = pair[1]





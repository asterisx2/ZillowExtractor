import Utils
import ZillowApiWorker
import PageExtractor

vals = Utils("Addresses.txt",";")
apiWorker = ZillowApiWorker
links = []
results = []
pageExtractor = PageExtractor

for val in vals:
    links += ZillowApiWorker.makeRequest(val[0],val[1])

for link in links:
    results += pageExtractor.execute(link)

print(results)
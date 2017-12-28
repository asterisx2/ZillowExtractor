class Utils:
    filePath = ""
    delimiter = ""
    def __init__(self, filepath, delimiter):
        self.filePath = filepath;
        self.delimiter = delimiter

    def getVals(self):
        list = []
        f = open(self.filePath,'r')

        line = f.readline()

        while line:
            vals = line.split(self.delimiter)
            list.append(vals)
            line = f.readline()

        f.close()
        return list

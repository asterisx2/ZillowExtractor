class Utils:

    def getVals(self, filePath, delimiter):
        list = []
        f = open(filePath,'r')

        line = f.readline()

        while line:
            vals = line.split(delimiter)
            vv = []
            for val in vals:
                va = val.strip()
                vv.append(va)
            vv.append(line)
            list.append(vv)
            line = f.readline()

        f.close()
        return list
    def getZpids(self, filePath):
        list = []
        f = open(filePath, 'r')

        line = f.readline()

        while line:
            list.append(line)
            line = f.readline()

        return list

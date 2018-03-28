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
        start = int(input('Enter the 0 based start index'))
        size = int(input('Enter no of items'))
        l = []
        for i in range(start, start + size):
            l.append(list[i])
        return l

    def getZpids(self, filePath):
        list = []
        f = open(filePath, 'r')

        line = f.readline()

        while line:
            list.append(line)
            line = f.readline()

        return list

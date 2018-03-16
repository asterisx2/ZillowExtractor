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
        start = int(input('Enter the 0 based start index'))
        end = int(input('Enter the 0 based last index'))
        f.close()
        l = []
        for i in [start, end]:
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

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
                if(va.find("CHICAGO") != -1):
                    va = "Chicago, "
                vv.append(va)
            list.append(vv)
            line = f.readline()

        f.close()
        return list

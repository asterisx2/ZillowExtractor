import json

import matplotlib.pyplot as pyplot
from matplotlib.widgets import CheckButtons

import Price



def plot():
    import os
    os.chdir(os.path.dirname(__file__))
    f = open(os.getcwd() + '\WithPrice.json', 'r')
    data = json.load(f)
    f.close()


    #Fields
    fields = ['Bathrooms','FinishedSqFt','LotSizeSqFt', 'YearBuilt','NumFloors']
    #fields = ['Price']
    weight = [20, 50, 50, 20, 20]
    #weight = [100.0]




    divisor = 0.0
    for w in weight:
        divisor = divisor + w;

    x = {}
    y = {}
    x['1999'] = []
    x['2000'] = []
    x['2001'] = []
    x['2002'] = []
    x['2003'] = []
    x['2004'] = []
    x['2005'] = []
    x['2006'] = []
    x['2007'] = []
    x['2008'] = []
    x['2009'] = []
    x['2010'] = []
    x['2011'] = []
    x['2012'] = []
    x['2013'] = []
    x['2014'] = []
    x['2015'] = []
    x['2016'] = []

    y['1999'] = []
    y['2000'] = []
    y['2001'] = []
    y['2002'] = []
    y['2003'] = []
    y['2004'] = []
    y['2005'] = []
    y['2006'] = []
    y['2007'] = []
    y['2008'] = []
    y['2009'] = []
    y['2010'] = []
    y['2011'] = []
    y['2012'] = []
    y['2013'] = []
    y['2014'] = []
    y['2015'] = []
    y['2016'] = []

    colors = ["#ffbe76", "#ff7979", "#badc58", '#f6e58d', '#f9ca24' ,'#f0932b' ,'#eb4d4b' ,'#6ab04c' ,'#7ed6df'
        ,'#e056fd' ,'#686de0' ,'#30336b' ,'#130f40' ,'#95afc0' ,'#535c68' ,'#be2edd' ,'#22a6b3', '#0000ff']

    taxRate = 0.019
    for d in data:
        c = 0
        p = 0.0
        notGood = False
        for f in fields:
            if not f in d:
                notGood = True
                break
            if not d[f]:
                notGood = True
                break
            else:
                p = p + (float(d[f]) * weight[c]/divisor)
            c = c+1
        p = p

        if not notGood and float(d['Price']) > 100000.00:
            taxShouldBe = ((p*1000) + float(d['Price']))  * taxRate
            for i in range(18):
                year = 1999 + i;
                if 'Tax'+str(year) in d:
                    if len(str(d['Tax'+str(year)])) > 2:
                        x[str(year)].append(p)



                        #y coordinate
                        #y[str(year)].append(int(str(d['Tax'+str(year)]).replace(',','').replace('$','')))
                        taxPercentage = ((float(str(d['Tax'+str(year)]).replace(',','').replace('$',''))-float(taxShouldBe))/taxShouldBe) * 100.0
                        y[str(year)].append(taxPercentage)




                        #Outliers to print
                        if taxPercentage > 200:
                            match =  Price.lcs(d['AddressTaken'], d['Street'])/len(d['Street']) * 100.0
                            print(str(match)+"%, "+str(taxPercentage)+"%[Abnormal Tax Percentage] AddressTaken: " +
                                  str(d['AddressTaken'])+", Zillow Address: " + d['Street'] + ", Price: " + d['Price'] +", Expected Tax: " +
                                  str(taxShouldBe)+", Actual Tax: " + str(str(d['Tax'+str(year)]).replace(',','').replace('$','')))





    #Plotting
    fig, ax = pyplot.subplots()

    l = {}

    for i in range(18):
        year = 1999+i
        c = colors[i]
        l[str(year)] = ax.scatter(x[str(year)], y[str(year)], label = str(year), color = c, visible=False, lw=2)

    rax = pyplot.axes([0.9, 0.1, 0.3, 0.5])
    years = ('1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011',
             '2012', '2013', '2014', '2015', '2016')
    bools = (True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
             True, True, True)
    check = CheckButtons(rax,years ,bools )
    [rec.set_facecolor(colors[i]) for i, rec in enumerate(check.rectangles)]

    def func(label):
        l[str(label)].set_visible(not l[str(label)].get_visible())
        pyplot.draw()

    check.on_clicked(func)

    pyplot.legend()
    pyplot.show()

plot()
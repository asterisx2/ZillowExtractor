from threading import Thread

from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from multiprocessing.dummy import Pool as ThreadPool
import multiprocessing

poolSize = 1
pool = ThreadPool(poolSize)
browsers = []
count = 0;


def getUrl(zpid):
    return "https://www.zillow.com/homedetails/" + zpid + "_zpid/?fullpage=true"


def getHtml(url):
    driver = browsers[multiprocessing.current_process().pid % poolSize]
    driver.get(url)
    timeout = 300  # seconds
    try:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        elems = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.TAG_NAME, 'tr')))
        print
        "Page is ready!"
        return driver.find_elements_by_tag_name("tr")
    except TimeoutException:
        print
        "Loading took too much time!"


def getData(rows):
    list = []
    if rows:
        for row in rows:
            try:
                c = row.find_elements_by_tag_name("td")
                if len(c) == 5:
                    if len(c[0].get_attribute('innerText')) == 4:
                        if str(c[0].get_attribute('innerText'))[:4].isdigit():
                            list.append([c[0].get_attribute('innerText'), c[3].get_attribute('innerText')])
            except:
                print('Nope' + row)
    global count
    count = count + 1
    if count % 50 == 0:
        print(count)
    return list


def getOne(zpid):
    r = [zpid, getData(getHtml(getUrl(zpid)))]
    return r


def getAll(zpids):
    list = []
    for zpid in zpids:
        list.append(getOne(zpid))
    return list


def save(list):
    string = "<Taxes>"
    for result in list:
        s = '<Tax><zpid>' + result[0] + '</zpid>'
        for r in result[1]:
            s = s + '<year value="' + r[0] + '">' + r[1] + '</year>'
        s = s + '</Tax>'
        string = string + s
    string = string + "</Taxes>"
    f = open("taxes.xml", "w")
    f.write(str(string))
    f.close()


def getZpids():
    list = []
    f = open("Zpids.txt", 'r')
    line = f.readline()
    while line:
        list.append(line)
        line = f.readline()
    f.close()
    return list


def buildBrowser(poolsize):
    global pool, browsers, poolSize
    poolSize = poolsize
    pool = ThreadPool(poolSize)
    for i in range(0, poolsize):
        browsers.append(webdriver.Firefox())


def executeMulti():
    buildBrowser(5)
    zpids = getZpids()
    save(pool.map(getOne, zpids))


def execute():
    buildBrowser(1)
    save(getAll(getZpids()))


execute()
for browser in browsers:
    browser.quit()

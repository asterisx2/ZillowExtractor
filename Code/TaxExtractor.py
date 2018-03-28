from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
driver = webdriver.Firefox()

def getUrl(zpid):
    return "https://www.zillow.com/homedetails/"+zpid+"_zpid/?fullpage=true"

def getHtml(url):
    driver.get(url)
    timeout = 30 # seconds
    try:
        elems = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.TAG_NAME, 'tr')))
        print
        "Page is ready!"
        return driver.find_elements_by_tag_name("tr")
    except TimeoutException:
        print
        "Loading took too much time!"


def getData(rows):
    list = []
    for row in rows:
        c = row.find_elements_by_tag_name("td")
        if len(c) == 5:
            if len(c[0].get_attribute('innerText')) == 4:
                if str(c[0].get_attribute('innerText'))[:4].isdigit():
                    list.append([c[0].get_attribute('innerText'),c[3].get_attribute('innerText')])
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
        s ='<zpid value="'+result[0]+'">'
        for r in result[1]:
            s = s + '<year value="'+r[0]+'">'+r[1]+'</year>'
        s = s + '</zpid>'
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

def execute():
    save(getAll(getZpids()))

execute()
driver.quit()



import requests
import selectorlib
import sqlite3

URL = "https://programmer100.pythonanywhere.com/tours/"

def scrape(url):
    response =requests.get(url)
    source = response.text
    return source

def extract(scraped):
    extractor = selectorlib.Extractor.from_yaml_file('extract.yaml')
    extract = extractor.extract(scraped)['tours']
    return extract

def sqlconnection():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    return cursor,connection

def checkExist(event):
    band,city,date= event
    cursor,connection = sqlconnection()
    querystmt = "SELECT band FROM events WHERE date=? AND city=?"
    cursor.execute(querystmt, (date, city))
    result = cursor.fetchall()
    if result:
        return True
    else:
        return False
def addEvent(event):
   cursor,connection = sqlconnection()
   band,city,date= event
   cursor.execute("INSERT INTO events VALUES(?,?,?)",(band,city,date))
   connection.commit()

if __name__ == "__main__":
    scraped = scrape(URL)
    extract = extract(scraped)
    print(extract)
    if extract != "No upcoming tours":
        band, city, date = extract.split(',')
        band =band.strip()
        city = city.strip()
        date = date.strip()
        event = (band,city,date)
        if checkExist(event) == False:
            addEvent(event)



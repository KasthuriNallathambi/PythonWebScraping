import requests
import selectorlib
from datetime import datetime
import streamlit as st
import plotly.express as px
import pandas as pd
from streamlit import plotly_chart
import sqlite3

URL = "https://programmer100.pythonanywhere.com/"
date_time = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

def scrape(URL):
    response = requests.get(URL)
   # date_time = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    scrape = response.text
    return scrape

def extract(scrape):
    extractor = selectorlib.Extractor.from_yaml_file('taskextract.yaml')
    extracted = extractor.extract(scrape)['temp']
    return extracted

def sqlconnection():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    return connection, cursor

if __name__ == "__main__":
    connection, cursor = sqlconnection()
    scrape = scrape(URL)
    extracted = extract(scrape)
    cursor.execute("INSERT INTO temperature VALUES(?,?)",(date_time,extracted))
    connection.commit()
    query_stmt = "SELECT * FROM temperature"
    df = pd.read_sql(query_stmt,connection)
    st.write("Date with temperature from DB")
    date = df['date'].to_list()
    temperature = df['temperature'].to_list()
    figure = px.line(x=date,y=temperature,labels={'x':'Date','y':'temperature'})
    plotly_chart(figure)





import requests
import selectorlib
from datetime import datetime
import streamlit as st
import plotly.express as px
import pandas as pd
from streamlit import plotly_chart

URL = "https://programmer100.pythonanywhere.com/"
response = requests.get(URL)
date_time = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
scrape = response.text

extractor = selectorlib.Extractor.from_yaml_file('taskextract.yaml')
extracted = extractor.extract(scrape)['temp']
with open('tasktemp.txt', 'a') as f:
    f.write(date_time)
    f.write(','.join(extracted))
    f.write('\n')
print(extracted)
print(datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))

df = pd.read_csv('tasktemp.csv')
st.write("Date with temperature")
date = df['data'].to_list()
temperature = df['temperature'].to_list()
figure = px.line(x=date,y=temperature,labels={'x':'Date','y':'temperature'})
plotly_chart(figure)
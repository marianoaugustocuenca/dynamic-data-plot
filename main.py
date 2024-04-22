import streamlit as st
import plotly.express as px
import pandas as pd


st.title('In search for Happiness')

data_x = st.selectbox('Select the data for the x-axis',
             ('GDP','Happiness','Generosity'))

data_y = st.selectbox('Select the data for the y-axis',
             ('GDP','Happiness','Generosity'))

file = pd.read_csv('happy.csv')

if data_x == 'GDP' :
    x_axis = file['gdp']
if data_x == 'Happiness' :
    x_axis = file['happiness']
if data_x == 'Generosity' :
    x_axis = file['generosity']

if data_y == 'GDP' :
    y_axis = file['gdp']
if data_y == 'Happiness' :
    y_axis = file['happiness']
if data_y == 'Generosity' :
    y_axis = file['generosity']

st.subheader(f'{data_x} and {data_y}')
figure = px.scatter(x=x_axis, y=y_axis,
                          labels={'x': data_x, 'y': data_y})
st.plotly_chart(figure)
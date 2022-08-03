import streamlit as st
import pandas as pd
import requests
from io import StringIO

mainc = st.container()
loaddata = st.container()

with mainc:
	font="sans serif"
	textColor="#26273"
	st.title('Electricity Theft Prediction')
	

def good_data():
	return pd.read_csv('https://raw.githubusercontent.com/kkumar47/Usage-Data/main/Final/Good_Residential.csv')[['Meter', 'Date_Raw','Usage']]

def bad_data():
	return pd.read_csv('https://raw.githubusercontent.com/kkumar47/Usage-Data/main/Final/Final_Bad_Customer.csv')

goodd = good_data()
badd = bad_data()

with loaddata:
	st.subheader("Electricity Usage History data for Customers", anchor ='The Data')
	col3,col4 = st.columns(2)
	with col3:
		st.text('Raw Data - Good Customer')
		#The raw data is displayed here
		st.dataframe(goodd.head(10))
	with col4:
		st.text('Raw Data - Bad Customer')
		st.dataframe(badd.head(10))
		
	

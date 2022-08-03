import streamlit as st
import pandas as pd
import requests
from io import StringIO
import numpy as np
import datetime as dt
import calendar
import random

mainc = st.container()
loaddata = st.container()
pprocess = st.container()

with mainc:
	font="sans serif"
	textColor="#26273"
	st.title('Electricity Theft Prediction')
	

def good_data():
	return pd.read_csv('https://raw.githubusercontent.com/kkumar47/Usage-Data/main/Final/Good_Residential.csv')[['Meter', 'Date_Raw','Usage']]

def bad_data():
	return pd.read_csv('https://raw.githubusercontent.com/kkumar47/Usage-Data/main/Final/Final_Bad_Customer.csv')

Good_Residential = good_data()
Bad_Residential = bad_data()

with loaddata:
	st.subheader("Electricity Usage History data for Customers", anchor ='The Data')
	col3,col4 = st.columns(2)
	with col3:
		st.text('Raw Data - Good Customer')
		#The raw data is displayed here
		st.dataframe(Good_Residential.head(10))
	with col4:
		st.text('Raw Data - Bad Customer')
		st.dataframe(Bad_Residential.head(10))
		
		
with pprocess:
	st.subheader("Pre-Process Data")
	#Process Good Customer Data
	Good_Residential['Hr'] = (((Good_Residential['Date_Raw']-1)%100)*30)//60
	Good_Residential['Day'] = abs(Good_Residential['Date_Raw']//100)
	Good_Residential = Good_Residential.drop(columns=['Date_Raw'])
	Good_Residential['Date'] = Good_Residential['Day'].apply(lambda x: pd.to_datetime((2009*1000 )+ x, format = "%Y%j") if x<=365 else pd.to_datetime((2010*1000 )+ (x-365), format = "%Y%j"))
	Good_Residential['Day_Num'] = Good_Residential['Date'].apply(lambda x: x.weekday())
	Good_Residential['Dayname'] = Good_Residential['Date'].apply(lambda x: calendar.day_name[x.weekday()])
	Good_Residential['Holiday_Ind'] = Good_Residential['Day_Num'].apply(lambda x: 0 if x<=4 else 1)
	Good_Residential['Month'] = Good_Residential['Date'].apply(lambda x: x.strftime("%B"))
	Good_Residential['Year'] = Good_Residential['Date'].apply(lambda x: x.year)
	def condition(x):
 		if (x=='August' or x=='September' or x=='October'):
    			return "Autumn"
  		elif (x=='November' or x=='December' or x=='January'):
    			return "Winter"
  		elif (x=='February' or x=='March' or x=='April'):
    			return "Spring"
  		elif (x=='May' or x=='June' or x=='July'):
    			return "Summer"
	Good_Residential['Season']=Good_Residential['Month'].apply(condition)
	col5, col6 = st.columns(2)
	col5.dataframe(Good_Residential)
	
	
	

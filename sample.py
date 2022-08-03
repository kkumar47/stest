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
	
def raw_data():
	repo ='Private_Data'
	path='Raw.txt'
	owner = 'kkumar47'
	token = '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'
	r = requests.get('https://api.github.com/repos/{owner}/{repo}/contents/{path}'.format(owner=owner, repo=repo, path=path),headers={'accept': 'application/vnd.github.v3.raw','authorization': 'token {}'.format(token)}, verify=False)
	string_io_obj = StringIO(r.text)
	return pd.read_csv(string_io_obj, usecols=["Meter","Date_Raw","Usage"])
rawdf = raw_data()

with loaddata:
	st.subheader("Electricity Usage History data for Customers", anchor ='The Data')
	col3,col4 = st.columns(2)
	with col3:
		st.text('Raw Data')
		#The raw data is displayed here
		st.dataframe(rawdf.head(10))
	

import requests
from bs4 import BeautifulSoup as bs
from bs4 import NavigableString, Tag
import pandas as pd
import numpy as np
import math
import datetime
from datetime import date
from datetime import timedelta

def parseTableData(tableId):
	table_report=soup.find_all('table',id=tableId)
	table_report=table_report[0]

	table_body=table_report.find_all('tbody')
	table_body=(table_body[0])

	df=pd.DataFrame()

	table_rows=table_body.find_all('tr')
	table_rows_list=list(table_rows)

	rows = []	
	for table_row in table_rows_list:			#UPTO for table_row in table_rows_list[0:7]: IT WORKS FINE, FOR ROW 7 BRAZIL - NEWCASES DOES NOT GIVE INT DATATYPE	
		rowContent = []
		for table_cell in list(table_row):
			if isinstance(table_cell,NavigableString):
				continue
			text=table_cell.get_text().replace('+', '')
			text=text.replace('\n', '')
			text=text.replace(',', '')
			if(text==''):
				text=0
			#print('text is ',text)
			try:
				text=int(text)
				rowContent.append(text)
				#print("{} converted to int".format(text))			
			except:
				rowContent.append(str(text))				
		rows.append(rowContent)		
	data_set=pd.DataFrame(rows)	
	

	colNames=[]
	for t in table_report.find('thead').find_all('th'):
		colNames.append(t.get_text())	
	#colNames.append('Population')
	#colNames.append('Continent')

	data_set.columns=colNames	
	#print(data_set.dtypes)
	return data_set

def getDataframe():
	data_set_today=parseTableData('main_table_countries_today')
	date_object = datetime.date.today()
	data_set_today['Date']=str(date_object)

	data_set_yesterday=parseTableData('main_table_countries_yesterday')
	date_object = datetime.date.today() - timedelta(days = 1)
	data_set_yesterday['Date']=str(date_object)

	data_set_yesterday2=parseTableData('main_table_countries_yesterday2')
	date_object = datetime.date.today() - timedelta(days = 2)
	data_set_yesterday2['Date']=str(date_object)

	data_set_today.rename(columns = {"Country,Other": "Country"},inplace = True)
	data_set_yesterday.rename(columns = {"Country,Other": "Country"},inplace = True)
	data_set_yesterday2.rename(columns = {"Country,Other": "Country"},inplace = True) 
		
	#return covid_data_set	
	return data_set_today,data_set_yesterday,data_set_yesterday2

# page=requests.get("https://www.worldometers.info/coronavirus/")
#soup = bs(page.content, 'html.parser')
covid_html_file='Coronavirus Update (Live) - Worldometer-Apr15.html'
with open(covid_html_file, "r") as f:
	page = f.read()
soup=bs(page,'html.parser')	

#covid_data_set=getDataframe()
data_set_today,data_set_yesterday,data_set_yesterday2=getDataframe()

covid_data_set=data_set_today
covid_data_set=covid_data_set.append(data_set_yesterday)
covid_data_set=covid_data_set.append(data_set_yesterday2)


# print(data_set_today.dtypes)
# print(data_set_yesterday.dtypes)
# print(data_set_yesterday2.dtypes)
# print(covid_data_set.dtypes)

covid_data_set.to_csv('covid_stats.csv')
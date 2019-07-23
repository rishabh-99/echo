import fitbit
import gather_keys_oauth2 as Oauth2
import pandas as pd 
import datetime
import pymysql
import csv
from pandas import DataFrame
# Open database connection
db = pymysql.connect("localhost","testuser","test123","echoes2" )
# prepare a cursor object using cursor() method
cursor = db.cursor()
CLIENT_ID = '22DP9C'
CLIENT_SECRET = '47b1c95d7df30de5c27df8f526069de3'
server = Oauth2.OAuth2Server(CLIENT_ID, CLIENT_SECRET)
server.browser_authorize()
ACCESS_TOKEN = str(server.fitbit.client.session.token['access_token'])
REFRESH_TOKEN = str(server.fitbit.client.session.token['refresh_token'])
auth2_client = fitbit.Fitbit(CLIENT_ID, CLIENT_SECRET, oauth2=True, access_token=ACCESS_TOKEN, refresh_token=REFRESH_TOKEN)
yesterday = str((datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y%m%d"))
yesterday2 = str((datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d"))
today = str(datetime.datetime.now().strftime("%Y-%m-%d"))
fit_statsHR = auth2_client.intraday_time_series('activities/heart', base_date=today, detail_level='1sec')
time_list = []
val_list = []
for i in fit_statsHR['activities-heart-intraday']['dataset']:
    val_list.append(i['value'])
    time_list.append(i['time'])
heartdf = pd.DataFrame({'Heart Rate':val_list,'Time':time_list})
#for m,n in heartdf.items():
#print(m)
# Drop table if it already exist using execute() method.
#cursor.execute("DROP TABLE IF EXISTS heart_rate")
#Create table as per requirement
''''sql = """CREATE TABLE heart_rate1 (
   DATE_ID  CHAR(20) NOT NULL,
   HEART_RATE  INT(20),
   TIME_SECS CHAR(15) )"""'''

sql="""INSERT INTO heart_rate1 VALUES('hello123','55','ransomd')"""
cursor.execute(sql)
# disconnect from server
db.close()
with open('trial1.csv','w') as f:
	l=heartdf.values.tolist()
	for lines in l:
		f.write("%s\n" %lines)
'''heartdf.to_csv()
with open('heartdf.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
    	print(row)'''
'''print(lines)
print("sdkbhfks")
print(heartdf)
with open('trial1.csv','w') as f:
f.write(lines)
print(lines)'''
#for m,n in heartdf.items():


	

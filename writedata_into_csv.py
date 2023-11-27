from datetime import date,datetime, timedelta
import datetime
from collections import defaultdict
import csv
import yfinance as yf


def date_format(string):
    date=''
    temp=''
    for i in string:
        if i=="-":
            date+=temp[::-1]+i
            temp=''
        else:
            temp+=i
    date+=temp[::-1]
    return date
#to read csv file

with open('C:\python\stocksproject.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    list_stocks=[]
    for line in csv_reader:
        list_stocks.append([line[0],line[1],line[2],line[3]])

#to add data in csv to dictionary 
        
    symbol={}
    for line in list_stocks[1:]:
        string=line[0]
        string=string[::-1]
        date=date_format(string)
        try:
            symbol[line[1]].append(date)
        except:
            symbol[line[1]]=[date]
    print(symbol)
    
# Open the CSV file for reading
with open('stockProjectdata2.csv', 'r') as file:
    reader = csv.reader(file)
    # Read the CSV data into a list
    data = list(reader)

data[0].append("triggered_date")
for i in range(1,len(data)):
    date=symbol[data[i][0]][-1]
    data[i].append(date)

# Write the updated data back to the CSV file
with open('stockProjectdata2.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
print("completed")




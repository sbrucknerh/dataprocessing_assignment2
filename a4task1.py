# YOUR CODE HERE
import requests
import pandas as pd

dataset1= {
    "creator" : "Fusion Media Limited" ,
    "catalogName" : "Investing.com" ,
    "catalogURL" : "https://www.investing.com" ,
    "datasetID" : "https://www.investing.com/indices/us-spx-500-historical-data" ,
    "resourceURL" : "https://raw.githubusercontent.com/sbrucknerh/dataprocessing_assignment2/refs/heads/main/S%26P_500_Historical_Data.csv"  ,
    "pubYear" : "2024"  ,
    "lastAccessed" : "2024-10-24T10:37:00"  ,
}

df = pd.read_csv(dataset1["resourceURL"], thousands = ",")

#print(df.info())
#drop NaN column
df = df.drop(columns=['Vol.'])
#convert date string to datetime
df["Date"] = pd.to_datetime(df["Date"])
#remove non numeric values from Change column
df["Change %"] = df["Change %"].str.replace("%","")
#convert strings to numeric values
df = df.astype({"Price": float, "Open": float, "High": float, "Low": float, "Change %": float})

#print(df)
#data is weekly, so group by year and get mean prices (open and closing prices). For High and Low prices get the highest and lowest of the year.
df = df.groupby(df["Date"].dt.year).agg({"Price": "mean", "Open": "mean", "High": "max", "Low": "min", "Change %": "mean"}).reset_index()
print(df)

#plotting the dataframe
df.plot(x="Date", y=["Price","High","Low"],
        kind="bar", figsize=(10, 10))

df.plot.scatter(x = 'Date', y = 'Change %', s = 10); 

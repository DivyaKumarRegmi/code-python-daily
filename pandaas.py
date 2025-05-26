import pandas as pd

df = pd.read_csv('data1.csv') #By default, the dropna() method returns a new DataFrame, and will not change the original.

new_df = df.dropna()
#It returns a new DataFrame with the rows containing NaN removed (it does not change the original DataFrame unless you use inplace=True).
#df.dropna(inplace = True) changes original data which is data1.csv

#This line prints the entire new_df DataFrame (after removing rows with NaN) in a tabular, readable format.
print(new_df.to_string())

#df.fillna(130, inplace = True) which replaces empty places to 130
#replace only for specific column
#df.fillna({"Calories": 130}, inplace=True)
#If you don’t use inplace=True in fillna, the method returns a new DataFrame with the missing values filled, but does not change the original DataFrame.


#Mean = the average value (the sum of all values divided by number of values).
x = df["Calories"].mean()

df.fillna({"Calories": x}, inplace=True)

df['Date'] = pd.to_datetime(df['Date'], format='mixed')
print(df.to_string())

df.dropna(subset=['Date'], inplace=True)
#subset=['Date'] tells pandas to look only at the 'Date' column for missing values.
#inplace=True means the change is made directly to the original DataFrame (df), not a copy.
print(df.to_string())

#wrong data 
#If you take a look at our data set, you can see that in row 7, the duration is 450, but for all the other rows the duration is between 30 and 60.
#It doesn't have to be wrong, but taking in consideration that this is the data set of someone's workout sessions, we conclude with the fact that this person did not work out in 450 minutes.

df.loc[7, 'Duration'] = 45
print(df.to_string())
#USING LOOP TO REPLACE WRONG DATA FOR LARGER SETS   
#To replace wrong data for larger data sets you can create some rules, e.g. set some boundaries for legal values, and replace any values that are outside of the boundaries.
for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.loc[x, "Duration"] = 120
print(df.to_string())

#REMOVING ROWS
#Another way of handling wrong data is to remove the rows that contains wrong data.
#Delete rows where "Duration" is higher than 120:
for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.drop(x, inplace = True)

print(df.to_string())

#REMOVING DUPLICATES
#To discover duplicates, we can use the duplicated() method.
#The duplicated() method returns a Boolean values for each row:
print(df.duplicated())
#now to remove those duplicates 
df.drop_duplicates(inplace = True)
print(df.to_string())


df.to_csv('data2.csv', index=False)
#df.to_excel('data2.xlsx', index=False)
#df.to_json('data2.json')






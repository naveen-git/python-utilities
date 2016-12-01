import pandas as pd
from pandas import ExcelWriter

# Reads the CSV dataset into Pandas
df = pd.read_csv('Traffic_Violations.csv', low_memory=False)
# Prints the number of lines in the CSV datasets
print("Total number of data lines in the CSV dataset:",len(df))
print("Number of Rows, Columns :",df.shape)  # size of the data
# List the column names on the Dataframe.
print("List of Columns in the dataset :",df.columns)  # column names
# Creates new Dataframe with the below 4 columns
df1=df[["Date Of Stop","State","VehicleType","Make"]]
# Displaying the basic statistical information on the Dataframe.
print(df1.describe())
# Filtering - Extracts the datasets which belongs to the state 'MD'
df1 = df1[df1.State.str.startswith('MD')]
# Changing the column names for simplicity
df1.columns = ['date','state','vtype','make']
# Typecasting - converting the object dtype to panda datetime
df1['date'] = df1['date'].apply(pd.to_datetime)
# Filtering by date - having dataset from only 01/01/15 to 12/13/16 from Jan to June
df1=df1[(df1['date'] > '01/01/15') & (df1['date'] < '12/31/16')]
# To avoid column copy and have the new column as Index view
df1.is_copy = False
# Adding a new column for month field extracting it from datetime column
df1.loc[:,'month'] = pd.Series(df1['date'].dt.month, index=df1.index)
# Adding a new column for year field extracting it from datetime column
df1.loc[:,'year'] = pd.Series(df1['date'].dt.year, index=df1.index)
# Naming index column for the Dataframe
df1.index.names = ['Index']
# Grouping the rows as per month - The output is count of year, month, vehicletype and make for each month between 1/1/15 to 12/13/16 for MaryLand
aggregate_df = df1.groupby([df1.year, df1.month, df1.vtype, df1.make])[['make']].count()
print(aggregate_df)
# save to new CSV file
aggregate_df.to_csv('Aggregation.csv', encoding='utf-8')
# save to xls
writer = ExcelWriter('Aggregation.xlsx')
aggregate_df.to_excel(writer,'Sheet1')
writer.save()

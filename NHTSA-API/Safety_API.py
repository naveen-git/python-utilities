import pandas as pd
from getVehicleId import formURL
from getSafetyFeatures import formSafetyURL

# Reads the CSV dataset into Pandas
df = pd.read_csv('2015_Crash_Data_MakeModel.csv', low_memory=False)

new_header = df.iloc[0] #grab the first row for the header
df = df[1:] #take the data less the header row
df.rename(columns = new_header) #set the header row as the df header
# Prints the number of lines in the CSV datasets
print("Total number of data lines in the CSV dataset:",len(df))

#Added new columns for Safety feature
df["Lane Departure Warning"] = None
df["Forward Collision Warning"] = None
df["Rearview Video Systems"] = None
df["Automatic Emergency Braking"] = None
df["Electronic Stability Control"] = None

for index, row in df.iterrows():
    vehicleId = formURL(row[3], row[5], row[6])
    print("got vehicle id")
    if(vehicleId > 0):
        safetyFeatures = formSafetyURL(vehicleId)
        df.loc[index,'Lane Departure Warning'] = safetyFeatures['Lane Departure Warning']
        if 'Rearview Video Systems' in safetyFeatures.keys():
            df.loc[index,'Rearview Video Systems'] = safetyFeatures['Rearview Video Systems']
            df.loc[index,'Electronic Stability Control'] = "Standard"
        if 'Electronic Stability Control' in safetyFeatures.keys():
            df.loc[index,'Electronic Stability Control'] = safetyFeatures['Electronic Stability Control']
        df.loc[index,'Forward Collision Warning'] = safetyFeatures['Forward Collision Warning']
        df.loc[index,'Automatic Emergency Braking'] = safetyFeatures['Automatic Emergency Braking']
        print(df.loc[index])
    else:
        print("Ignored")

df.to_csv("final_crash_safety_2015.csv",sep='\t',encoding='utf-8')

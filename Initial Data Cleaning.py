import pandas as pd 
import numpy as np
from tabulate import tabulate 

# Load CSV file
df = pd.read_csv('C:/Users/PC/OneDrive/Documents/Data Portfolio/Hospital Allocation Project/hospitals.csv')
# Display the first few rows
print(df.head())

def clean_data(df):
    # Rename column 'PARISH,C,25' to 'Parish'
    df = df.rename(columns={'PARISH,C,25': 'Parish'})
    # Rename column 'HEALTH_ARE,C,16' to 'Health_region'
    df = df.rename(columns={'HEALTH_ARE,C,16': 'Health_region'})
    # Rename column 'FACIL_TYPE,C,40' to 'Facility_type'
    df = df.rename(columns={'FACIL_TYPE,C,40': 'Facility_type'})
    # Rename column 'CEN_NAME,C,50' to 'Facility_name'
    df = df.rename(columns={'CEN_NAME,C,50': 'Facility_name'})
    # Rename column 'CEN_CODE,C,8' to 'Facility_code'
    df = df.rename(columns={'CEN_CODE,C,8': 'Facility_code'})
    # Rename column 'ADDRESS,C,80' to 'Address'
    df = df.rename(columns={'ADDRESS,C,80': 'Address'})
    # Rename column 'TELEPHONE,C,10' to 'Telephone'
    df = df.rename(columns={'TELEPHONE,C,10': 'Telephone'})
    # Rename column 'FACIL_STAT,C,16' to 'Facility_status'
    df = df.rename(columns={'FACIL_STAT,C,16': 'Facility_status'})
    # Rename column 'OWNERSHIP,C,16' to 'Ownership'
    df = df.rename(columns={'OWNERSHIP,C,16': 'Ownership'})
    # Rename column 'Z990__BEDS,N,10,0' to 'Z990_Beds'
    df = df.rename(columns={'Z990__BEDS,N,10,0': 'Z990_Beds'})
    # Rename column 'Z996__BEDS,N,10,0' to 'Z996_Beds'
    df = df.rename(columns={'Z996__BEDS,N,10,0': 'Z996_Beds'})
    # Rename column 'Z999__BEDS,N,10,0' to 'Z999_Beds'
    df = df.rename(columns={'Z999__BEDS,N,10,0': 'Z999_Beds'})
    return df

df_clean = clean_data(df.copy())
df_clean.head()

# While viewing the data, we notice that the Facility_code column is being read as a date type, which may lead to issues if there are leading zeros in the codes. To ensure that the Facility_code is treated as a string, we can specify the data type when reading the CSV file.
df_clean = df_clean.astype({"Facility_code": str})

# Provides a more accurate representation of the data, especially if there are leading zeros in the Facility_code. Now, when we print the DataFrame, we can see that the Facility_code is treated as a string, preserving the format.
print(tabulate(df_clean, headers = 'keys', tablefmt = 'github'))

# Assign PRIV codes to missing Facility_code
df_clean["Facility_code"] = df_clean.apply(
    lambda row: f"PRIV{str(row.name+1).zfill(2)}" if pd.isna(row["Facility_code"]) else row["Facility_code"],
    axis=1
)

# A rerun of the tabular view inorder to confirm that the missing Facility_code values have been filled with the new PRIV codes.
print(tabulate(df_clean, headers = 'keys', tablefmt = 'github'))







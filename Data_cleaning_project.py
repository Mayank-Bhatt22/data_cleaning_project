import pandas as pd
import numpy as np
import time
import openpyxl
import xlrd
import os
import random


def data_cleaning_master(data_path, data_name):

    print("Thank you for giving the detail")
    
    # Generating random number
    sec = random.randint(1, 4)
    
    # Print delay message
    print(f"Plese wait for {sec}seconds! checking file path")
    time.sleep(sec)
    
    # checking if the path exists
    if not os.path.exists(data_path):
        print("Incorrect path! Try again with correct path")
        return  # Stop further execution
        
    else:
        # checking the file type
        if data_path.endswith('.csv'):
            print("Dataset is csv file!")
            data = pd.read_csv(data_path, encoding_errors="ignore")
            
        elif data_path.endswith('.xlsx'):
            print('Dataset is excel file!')
            data = pd.read_excel(data_path)
                
        else:
            print('Unknown file type')
            return  # Stop further execution
     
    sec = random.randint(1, 4)   
    # Print delay message
    print(f"Plese wait for {sec}seconds! checking total columns and rows")
    time.sleep(sec)
    
    # showing number of records
    print(f"Dataset contains total rows: {data.shape[0]} \n Total Columns: {data.shape[1]}")

    # start cleaning
    
    sec = random.randint(1, 4)
    # Print delay message
    print(f"Plese wait for {sec}seconds! checking total duplicates")
    time.sleep(sec)
    
    # checking duplicates
    duplicates = data[data.duplicated()]
    total_duplicates = duplicates.shape[0]

    print(f"Dataset has total duplicate records: {total_duplicates}")

    sec = random.randint(1, 4)
    # Print delay message
    print(f"Plese wait for {sec}seconds! Saving total duplicates rows")
    time.sleep(sec)
    


    # saving the duplicates
    if total_duplicates > 0:
        duplicates.to_csv(f'{data_name}_duplicates.csv', index=None)

    # deleting duplicates
    df = data.drop_duplicates()

    sec = random.randint(1, 4)
    # Print delay message
    print(f"Plese wait for {sec}seconds! checking for missing values")
    time.sleep(sec)
    

    # find missing values
    total_missing_value = df.isnull().sum().sum()
    missing_value_colums = df.isnull().sum()

    print(f"Dataset has Total missing value: {total_missing_value}")
    print(f"Dataset contains missing values by columns: \n{missing_value_colums}")

    # Dealing with missing values 
    # fillna for numeric columns
    # dropna for non-numeric columns
    
    sec = random.randint(1, 4)
    # Print delay message
    print(f"Plese wait for {sec}seconds! cleaning datasets")
    time.sleep(sec)
    

    columns = df.columns

    for col in columns:
        # filling mean for numeric columns
        if np.issubdtype(df[col].dtype, np.number):
            df[col] = df[col].fillna(df[col].mean())
        else:
            # Dropping all rows with missing records for non-numeric columns
            df.dropna(subset=[col], inplace=True)
    
    sec = random.randint(1, 4)            
    # Print delay message
    print(f"Plese wait for {sec}seconds! exporting datasets")
    time.sleep(sec)
    

    # Data is cleaned
    print(f"Congrats! Dataset is cleaned! \n Number of Rows: {df.shape[0]} \n Number of Columns: {df.shape[1]}")

    # saving the clean dataset 
    df.to_csv(f'{data_name}_Clean_data.csv', index=None)
    print("Dataset is saved!")


if __name__ == "__main__":
    
    print("Welcom to Data clraning Master!")
    # asking  path and file name
    data_path = input("Please enter dataset path: ")
    data_name = input("Please enter dataset name: ")
    
    # calling the function
    data_cleaning_master(data_path, data_name)
    
    print("*********( Thank you! )**********")
    
    
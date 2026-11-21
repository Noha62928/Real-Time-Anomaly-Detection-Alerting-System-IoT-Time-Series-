import pandas as pd 
# Load dataset
df = pd.read_csv("data/predictive_maintenance_dataset.csv")
#display first 5 rows of the dataset 
print(df.head())
#dataset dimentions 
print("Shape:", df.shape)
#Column names 
print("Columns:", df.columns.tolist())
#display dataset information
df.info()  
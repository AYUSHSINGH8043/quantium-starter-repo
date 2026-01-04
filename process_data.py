import pandas as pd
from pathlib import Path

# Folder containing CSV files
data_folder = Path("data")

# Read all CSV files
csv_files = list(data_folder.glob("*.csv"))

df_list = []

for file in csv_files:
    df = pd.read_csv(file)
    df_list.append(df)

# Combine all CSVs into one DataFrame
data = pd.concat(df_list, ignore_index=True)

# Keep only Pink Morsel
data = data[data["product"] == "Pink Morsel"]

# Create Sales column
data["Sales"] = data["quantity"] * data["price"]

# Keep only required columns
final_data = data[["Sales", "date", "region"]]

# Rename columns to match requirement
final_data.columns = ["Sales", "Date", "Region"]

# Save output file
final_data.to_csv("processed_sales_data.csv", index=False)

print("Data processing complete. Output saved as processed_sales_data.csv")

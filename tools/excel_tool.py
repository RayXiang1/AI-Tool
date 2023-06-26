import pandas as pd

# Load the tables from different sheets of the same Excel file
summary_df = pd.read_excel('data/future-ems-wms-stock.xlsx', sheet_name='summary')
detail_df = pd.read_excel('data/future-ems-wms-stock.xlsx', sheet_name='detail')

# Ensure the SKU columns in both dataframes are of the same type
summary_df['品名'] = summary_df['品名'].astype(str)
detail_df['品名'] = detail_df['品名'].astype(str)
summary_df['编码'] = summary_df['编码'].astype(str)
detail_df['编码'] = detail_df['编码'].astype(str)
summary_df['单位'] = summary_df['单位'].astype(str)
detail_df['单位'] = detail_df['单位'].astype(str)
summary_df['原产国'] = summary_df['原产国'].astype(str)
detail_df['原产国'] = detail_df['原产国'].astype(str)

# Create an empty list for the result
result = []

# Loop over the rows in the summary dataframe
for idx, row in summary_df.iterrows():
    # Append the current summary row to the result list
    result.append(row.to_frame().T) # Convert the series to a dataframe

    # Get the corresponding details and append them to the result list
    details = detail_df[(detail_df['品名'] == row['品名']) 
                        & (detail_df['编码'] == row['编码'])
                        & (detail_df['单位'] == row['单位'])
                        & (detail_df['原产国'] == row['原产国'])
                        ]
    result.append(details)

# Concatenate all the dataframes in the result list
result_df = pd.concat(result)

# Reset the index of the result dataframe
result_df = result_df.reset_index(drop=True)

# Save the result dataframe to a new Excel file
result_df.to_excel('combined.xlsx', index=False)
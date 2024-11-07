import pandas as pd
import re

# Define file paths
da1_barcodes_file = '/Users/gc/Desktop/Ten-a-b-GH146/find_DA1/names_DA1_24hAPF.txt'
barcode_file = '/Users/gc/Desktop/Ten-a-b-GH146/find_DA1/Barcode.txt'
gsm_file = '/Users/gc/Desktop/Ten-a-b-GH146/find_DA1/GSM.txt'
metadata_file = '/Users/gc/Desktop/Ten-a-b-GH146/find_DA1/Metadata.txt'

with open(da1_barcodes_file, 'r') as file:
    da1_barcodes = [line.strip() for line in file]

with open(barcode_file, 'r') as file:
    all_barcodes_raw = file.read().split()

all_barcodes = []
for i in all_barcodes_raw:
    if '[' in i:
        a = i.split('[')[1]
        b = a.split(']')[0]
        all_barcodes.append(b)

with open(gsm_file, 'r') as file:
    all_gsm_ids = file.read().split()

# Step 1: Match DA1 barcodes to GSM IDs
barcode_to_gsm = {}
for barcode in da1_barcodes:
    if barcode in all_barcodes:
        index = all_barcodes.index(barcode)
        barcode_to_gsm[barcode] = all_gsm_ids[index]

# Step 2: Load Metadata and match GSM IDs to SRR IDs
metadata = pd.read_csv(metadata_file, header=None)
metadata.columns = ["SRR_ID", "Other", "Length", "Reads", "Project", "Sample", "BioSample", "Type", "Source",
                    "Visibility", "Files", "Storage", "Region", "Experiment", "Marker", "GSM_ID", "Platform",
                    "Layout", "Other_Type", "Transcription", "Num", "Species", "Instrument", "Date", "GSM",
                    "Type_2", "SRP", "Update_Date", "Count"]
# Filter metadata to only rows with matching GSM IDs
matching_gsm_ids = list(barcode_to_gsm.values())
filtered_metadata = metadata[metadata["GSM"].isin(matching_gsm_ids)]

# Map GSM IDs to SRR IDs
gsm_to_srr = filtered_metadata[["GSM", "SRR_ID"]].drop_duplicates()

# Save the result to a CSV
#output_file = '/Users/gc/Desktop/Ten-a-b-GH146/find_DA1/DA1_GSM_to_SRR.csv'
#gsm_to_srr.to_csv(output_file, index=False)

srr_list = gsm_to_srr['SRR_ID']
srr_list.to_csv('DA1_GH146_Acc_List.txt',index=False,header=False)





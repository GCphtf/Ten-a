import pandas as pd

# Map the transcript ID (FBtr) to the transcript name
FBtr_to_Name_df = pd.read_csv('/Users/gc/Desktop/Ten-a/Tena-isoform-tables/transcripts-Summary-Drosophila_melanogaster_Transcript_Exons_FBtr0300201.csv')
FBtr_list = list(FBtr_to_Name_df['Transcript ID'])
Name_list = list(FBtr_to_Name_df['Name'])

# Path for pandas to read junction table
Csv_path_list = []
for ID in FBtr_list:
    Csv_path_list.append(f'/Users/gc/Desktop/Ten-a/Tena-isoform-tables/ExonsSpreadsheet-Drosophila_melanogaster_Transcript_Exons_{ID}.csv')

# Make the junction list to store all junctions for A & B isoform
A_isoform_junction_list = []
B_isoform_junction_list = []

# Want to read the odd number lines in the csv
def create_odd_numbers(total_number):
    Number_list = range(total_number)
    return [i for i in Number_list if (i % 2 != 0 and i != total_number-1)]

for csv_path in Csv_path_list:
    # Determine the isoform type (A or B ?)
    ID_csv = csv_path.split('_')[4]
    ID = ID_csv.split('.')[0]
    if ID in ['FBtr0346129','FBtr0299859','FBtr0346335']:
        Isoform = 'B'
    else:
        Isoform = 'A'

    # Read the exon lines
    df = pd.read_csv(csv_path)
    row_list = create_odd_numbers(len(df))

    # Make a list to hold the exon start and end points
    Exon_start_end = []

    for i in row_list:
        exon_start = df.at[i, 'Start']
        exon_end = df.at[i, 'End']
        # Add those into the continuous list
        Exon_start_end.append(exon_start)
        Exon_start_end.append(exon_end)

    # The junctions are the [1,2] [3,4]... combinations in the list
    Number_of_junction_2 = len(Exon_start_end)
    Number_of_junction = int(Number_of_junction_2/2)
    for j in range(Number_of_junction-1):
        k = j+1
        junction = (Exon_start_end[2*k-1],Exon_start_end[2*k])
        if Isoform == 'A':
            A_isoform_junction_list.append(junction)
        else:
            B_isoform_junction_list.append(junction)

A_isoform_junction_list = set(A_isoform_junction_list)
B_isoform_junction_list = set(B_isoform_junction_list)

A_unique_junctions = A_isoform_junction_list - B_isoform_junction_list
B_unique_junctions = B_isoform_junction_list - A_isoform_junction_list

print('A')
print(A_unique_junctions)
print('B')
print(B_unique_junctions)




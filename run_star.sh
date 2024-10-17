#!/bin/bash 
# Set directories 
FASTQ_DIR="/Users/gc/Desktop/Ten-a/STAR_test/SRR_fastq" 
GENOME_DIR="/Users/gc/Desktop/to_be_dealt_with/NYUSH/Capstone/genome_directory" 
OUTPUT_DIR="/Users/gc/Desktop/Ten-a/STAR_test/STAR_output" 

# Loop through all _1.fastq files and match with _2.fastq 
for R1 in "$FASTQ_DIR"/*_1.fastq; do 
    # Get the base name without _1.fastq (e.g., SRR1234567) 
    BASE=$(basename "$R1" _1.fastq) 

    # Define the corresponding R2 file 
    R2="$FASTQ_DIR/${BASE}_2.fastq" 

    # Check if both R1 and R2 exist
    if [[ -f "$R1" && -f "$R2" ]]; then
        echo "Processing: $R1 and $R2"

        # Run STAR for the paired-end group
        STAR --runThreadN 8 \
             --genomeDir "$GENOME_DIR" \
             --readFilesIn "$R1" "$R2" \
             --outSJfilterReads Unique \
             --outFileNamePrefix "$OUTPUT_DIR/${BASE}_" \
             --outSAMtype None

        echo "Processed $BASE"
    else
        echo "Error: One or both FASTQ files missing for $BASE"
    fi
done

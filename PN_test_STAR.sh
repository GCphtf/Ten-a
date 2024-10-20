#!/bin/bash 

# Set directories 
FASTQ_DIR=~/ten_a_isoform_project/PN_fastq 
GENOME_DIR=~/ten_a_isoform_project/genome_directory 
OUTPUT_DIR=~/ten_a_isoform_project/STAR_output 

# Loop through all _1.fastq.gz files and match with _2.fastq.gz 
for R1_GZ in "$FASTQ_DIR"/*_1.fastq.gz; do 
    # Get the base name without _1.fastq.gz (e.g., SRR1234567) 
    BASE=$(basename "$R1_GZ" _1.fastq.gz) 

    # Define the corresponding R2 file 
    R2_GZ="$FASTQ_DIR/${BASE}_2.fastq.gz" 

    # Check if both R1 and R2 exist
    if [[ -f "$R1_GZ" && -f "$R2_GZ" ]]; then
        echo "Processing: $R1_GZ and $R2_GZ"

        # Gunzip the files
        gunzip -c "$R1_GZ" > "$FASTQ_DIR/${BASE}_1.fastq"
        gunzip -c "$R2_GZ" > "$FASTQ_DIR/${BASE}_2.fastq"

        # Define uncompressed files
        R1="$FASTQ_DIR/${BASE}_1.fastq"
        R2="$FASTQ_DIR/${BASE}_2.fastq"

        # Run STAR for the paired-end group
        STAR --runThreadN 16 \
             --genomeDir "$GENOME_DIR" \
             --readFilesIn "$R1" "$R2" \
             --outSJfilterReads Unique \
             --outFileNamePrefix "$OUTPUT_DIR/${BASE}_" \
             --outSAMtype SAM

        echo "Processed $BASE"

        rm "$R1" "$R2"
    else
        echo "Error: One or both FASTQ files missing for $BASE"
    fi
done

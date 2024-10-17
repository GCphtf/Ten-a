# Ten-a
Things to do:

1, download miniconda3, then use miniconda3 to download SRA Toolkit, STAR, kallisto (Done)
    
    Set the SRA configuration by vdb-config -i, set the Cache path.

2, From GSE162121 and GSE161228 find the [SRA Accession list](https://github.com/GCphtf/Ten-a/tree/main/Accession_List) and download. (Done)

3, Use the SRA Accession list to download the PN and ORN sample fastq files.

    cat /_(path to accession list)_/.txt | xargs -n 1 -P 4 prefetch
    for srr in $(cat /_(path to accession list)__/.txt); do
      fastq-dump --split-3 --outdir /_(path to fastq storage place)_/ $srr
    done

4， Generate STAR index. 

    STAR --runThreadN 8 --runMode genomeGenerate --genomeDir /Users/gc/Desktop/genome_directory --genomeFastaFiles /Users/gc/Desktop/to_be_dealt_with/NYUSH/Capstone/gene_annotation/Drosophila_melanogaster.BDGP6.46.dna.toplevel.fa --sjdbGTFfile /Users/gc/Desktop/to_be_dealt_with/NYUSH/Capstone/gene_annotation/Drosophila_melanogaster.BDGP6.46.111.gtf --sjdbOverhang 74

5, Run STAR to generate the output files. The command line code is written in [run_star.sh](https://github.com/GCphtf/Ten-a/tree/main/run_star.sh). Change the path before using!

    ulimit -n 4096
    chmod +x run_star.sh   #path to run_star should be added
    ./run_star.sh
    
6, Having SRR....._SJ.out.tab in the directory, now use a python script to determine which cell has which junction.





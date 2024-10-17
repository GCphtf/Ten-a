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
    
4, Run STAR to generate the output files. The command line code is written in [run_star.sh](https://github.com/GCphtf/Ten-a/tree/main/run_star.sh)

    ulimit -n 4096
    
    





# Ten-a
Things to do:

1, download miniconda3, then use miniconda3 to download SRA Toolkit, STAR, kallisto (Done)
    
    Set the SRA configuration by vdb-config -i, set the Cache path.

2, From GSE162121(?) and GSE161228 find the [SRA Accession list](https://github.com/GCphtf/Ten-a/tree/main/Accession_List) and download. (Done)
    JH provided ORN: GSE143038
    Liyuan used PN: GSE161228

    The accession lists are downloaded in the Acc_List folder.
    Ways to download the accession lists by wget will be updated later.

3, Use the SRA Accession list to download the PN and ORN sample fastq files.
    fastq files are stored in FastQ folder. The FastQ folder has PN, ORN, and test_DC3, test_DA1 subfolders.

    cat /public/home/tongchaogroup/yijielin/Acc_List/PN_Acc.txt | xargs -n 1 -P 4 prefetch
    cat /public/home/tongchaogroup/yijielin/Acc_List/ORN_Acc.txt | xargs -n 1 -P 4 prefetch
    
    for srr in $(cat /public/home/tongchaogroup/yijielin/Acc_List/PN_Acc.txt); do
      fasterq-dump --outdir /public/home/tongchaogroup/yijielin/FastQ/PN $srr
      gzip /public/home/tongchaogroup/yijielin/FastQ/PN/${srr}_1.fastq
      gzip /public/home/tongchaogroup/yijielin/FastQ/PN/${srr}_2.fastq
      find /public/home/tongchaogroup/yijielin/FastQ/PN -type f -name "*.fastq" ! -name "*_1.fastq" ! -name "*_2.fastq" -exec rm {} +
    done

    for srr in $(cat /public/home/tongchaogroup/yijielin/Acc_List/ORN_Acc.txt); do
      fasterq-dump --outdir /public/home/tongchaogroup/yijielin/FastQ/ORN $srr
      gzip /public/home/tongchaogroup/yijielin/FastQ/ORN/${srr}_1.fastq
      gzip /public/home/tongchaogroup/yijielin/FastQ/ORN/${srr}_2.fastq
      find /public/home/tongchaogroup/yijielin/FastQ/ORN -type f -name "*.fastq" ! -name "*_1.fastq" ! -name "*_2.fastq" -exec rm {} +
    done
    

4， Generate STAR index. 

    Download dna fasta and gtf:

    

    STAR --runThreadN 8 --runMode genomeGenerate --genomeDir /Users/gc/Desktop/genome_directory --genomeFastaFiles /Users/gc/Desktop/to_be_dealt_with/NYUSH/Capstone/gene_annotation/Drosophila_melanogaster.BDGP6.46.dna.toplevel.fa --sjdbGTFfile /Users/gc/Desktop/to_be_dealt_with/NYUSH/Capstone/gene_annotation/Drosophila_melanogaster.BDGP6.46.111.gtf --sjdbOverhang 74

5, Run STAR to generate the output files. The command line code is written in [run_star.sh](https://github.com/GCphtf/Ten-a/tree/main/run_star.sh). Change the path before using!

    ulimit -n 4096
    chmod +x run_star.sh   #path to run_star should be added
    ./run_star.sh
    
6, Having SRR....._SJ.out.tab in the directory, now use a python script to determine which cell has which junction.





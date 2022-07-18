# BackgroundErrorSuppreesionforQAseq
Recording of the background polishing for QAseq 

**createBED.sh**

Create a bed file based on the output of QAseq pipeline

```
./createBED.sh /dssg/home/acct-medkwf/medkwf4/results/MRD/standard_3_6_16_AAABAC/index/tube_1.fasta
```

After making the bed file, use the iDES software to convert bed files created by the standard QAseq pipeline to FREQ format files. These FREQ files are named as "read-level samples"

See the official document for iDES: https://aalab.stanford.edu/ides/download.php#fileConversion


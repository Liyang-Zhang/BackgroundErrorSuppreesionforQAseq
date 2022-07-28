# BackgroundErrorSuppreesionforQAseq
Recording of the background polishing for QAseq 

**createBED.sh**

Create a bed file based on the output of QAseq pipeline

```
./createBED.sh /dssg/home/acct-medkwf/medkwf4/results/MRD/standard_3_6_16_AAABAC/index/tube_1.fasta
```

After making the bed file, use the iDES software to convert bed files created by the standard QAseq pipeline to FREQ format files. These FREQ files are named as "read-level samples"

See the official document for iDES: https://aalab.stanford.edu/ides/download.php#fileConversion

**QAseq_MRD.py**

Extract mutation information of designed sites from official QAseq pipeline outcome. Two extra sheets, "MRD" and "MRD_error",  will be made. Some parameters like input paths need change, and the script is run locally. Download the mutation directory from the server before running this script.

**FREQfileCreate.py**

Use the QAseq pipeline outputs to create FREQ files on UMI level. This script can be used to make either input samples of iDES or FREQ files for UMI-level database.

**QASeq_FreqAnnotation.py**

Convert background polishing freq results to easy-reading excel format. Yellow cells stand for the variant type consistent with the design sites, and pink cells correspond to error sites left by the iDES polishing model.

**iDES-freqModification.py**

The original FREQ files created from bam files contain all sites informations, including undesigned sites. Use this script to modify the read level backgrounf database FREQ files, and only retain the design sites' information.

**errorRateDataFrameCreate.py**

Use this script to get a summary about error signals in either pre-polished or polished databases FREQ files.

**MRDErrorRateHeatmap.R**

Followed by *errorRateDataFrameCreate.py*, use this script to visualize the error rate dataframe with heatmap.

**iDES_polishing_example.R**

Sometimes, there are some werid sites in the iDES polishing result. This script is used to model the calculation procedure of iDES model.

**QAseq_iDES_linux.py**

The linux version pipeline that integrate the scripts for background polishing. It should be ran in the QAseq pipeline running directory.

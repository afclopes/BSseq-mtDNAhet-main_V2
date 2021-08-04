# BSseq-mtDNAhet - README SBatch-Script-For-pipeline.sh


MitoCall is a scalable and versatile pipeline for the analysis of mitochondrial DNA parameters generating reliable output with the identification and quantification of heteroplasmic variants, adaptable for the use of both mouse and human genomes.

This tool depends on paired end single cell data, and will not work for measuring heteroplasmy when using single end data or bulk cell data.

## System requirements

This pipeline uses a number of different standard bioinformatics tools, which must be installed before starting to use this tool.

- FastQC v0.11.9
- trim_galore version 0.6.4_dev
- bismark 0.23.0
- samtools 1.11
- bcftools 1.11
- python 3.8.6
- bowtie2 2.4.2

## MitoCall scripts

A number of different scripts are required to run this pipeline. They are described below:

- SBatch-Script-For-pipeline.sh: contains the details to run the pipeline on the cluster via slurm.
- SBatch-Script-For-pipeline-xargs.sh: contains the details to run the pipeline on the cluster via slurm, when you want to run multiple samples at the same time. It can be faster that running your multiple samples using a job_array.
- SBatch-full-align-pipeline.sh: needed to run all the steps of the pipeline up to the production of the final vcf file required by the python script.
- variables.sh: has a list of variables that can be changed to affect the entire tool. The values found here can be considered the default values and example file names or paths.
- variables-xargs.sh: has a list of variables that can be changed to affect the entire tool. The values found here can be considered the default values and example file names or paths. The filename has changed to allow for sample names from the list to be inputed one at a time.
- PythonScript_HetTable.py: is the python script which is required to compute the heteroplasmy approximations for each position of the mitochondrial DNA.
- ListSamples.dat: is a list of sample names that should be run through the pipeline one at a time.


## Other files required

To run this pipeline, you will require to have paired end bisulfite sequencing data. This pipeline was tested for data produced using the scBS-seq method. You will also require:
- 2 files of sequencing data, eg. SRR8239851_1.fastq.gz SRR8239851_2.fastq.gz. These were gathered from https://genomemedicine.biomedcentral.com/articles/10.1186/s13073-019-0694-y#Sec2
- reference genome of the species in question.

## Accepted inputs

Each file needed needs to be in specific format to be accepted as an input:

- .fa.gz: reference genome. Fasta files ending for example in .fasta can be manually changed to .fa
- filename_1.fastq.gz: paired data files name followed by _1 or _2 for the pair


## User defined options

### User defined options in variables file:

In the script called 'variables.sh', the user is allowed to change some settings according to what the require. This can be due to the how the experimental work was carried out, or whether enough data passed most of the quality controls and hence if they want to relax some of the quality controls.

Here are some of the options to change:

- input_dir: input directory, where all your raw data can be found in .fastq.gz format
- working_dir: working directory, where all data produced during the pipeline will be stored
- genome_dir: genome directory, where your reference genome will be kept in fa.gz format and later in fa format
- filename: can be your unique filename prefix or a list to several filenames
- clipping_value: refers to the number of bases that you want to remove from the ends of each sequence. This usually is used to remove bases belonging to the adaptor used during sequencing
- mapping_quality: default value is 20. Try plotting your "MAPQ value" to see whether the default number causes too much data loss, and consider reducing this if necessary.
- base_quality: default value is 30. This number is quite strict compared to other studies.

### User defined options in python script:

Another place that the user needs to define is when using the python script (PythonScript_HetTable.py). The user needs to make sure to replace '/path/to/directory/with/finalvcffiles' with the actual path for their files.

### User defined options in sbatch script:

-J: add name of job that will appear when running your job on slurm
-t: set time desired to run sample. Usually 48-72 h is enough for single cells
-output: add the name for the output file for the sbatch run. This file will describe the sets of your pipeline that have been completed
-D: set the name of the directory where the output files produced during the pipeline will go
-c: number of cpus used for running this job. By default, keep this at 1, unless running multiple samples together with xargs, then use 4.
-partition: name the server partition where your job should be run via slurm
-/path/to/sbatchScript/: define path to the pipeline script

## MitoCall outputs

Every step of the pipeline will produce a different file. These files will each have an expected suffix, allowing us to track which step the pipeline is at, and in case of an error, allowing us to discover which was the last file that was outputted as expected. The following are the expected file suffixes and which step produces them:

- gunzip produces .fa
- bisulfite_genome_preparation produces a folder called Bisulfite_Genome and a file ending in .fa.fai
- trim_galore produces _1_val_1.fq.gz and _2_val_2.fq.gz
- _1_val_1.fq.gz are replaced by _val.R1.fastq.gz
- bismark produces _val.R1_bismark_bt2_pe.bam (the paired files will now become just one)
- deduplication with bismark produces _val.R1_bismark_bt2_pe.bam
- samtools sorting produces _val.R1_bismark_bt2_pe.deduplicated_sorted.bam
- samtools mapping quality produces _val.R1_bismark_bt2_pe.deduplicated_sorted_MAPQ20.bam
- bcftools mpileup and base quality produces _val.R1_bismark_bt2_pe.deduplicated_sorted_MAPQ20_bcftools.vcf
- bcftools normalisation produces _val.R1_bismark_bt2_pe.deduplicated_sorted_MAPQ20_bcftools_Normalised.vcf
- grep selection of mtDNA produces _val.R1_bismark_bt2_pe.deduplicated_sorted_MAPQ20_bcftools_Normalised_MitoReads.vcf
- awk selection of necessary columns from vcf file produces multiple files: _val.R1_bismark_bt2_pe.deduplicated_sorted_MAPQ20_bcftools_Normalised_MitoReads_part1_1.vcf, _val.R1_bismark_bt2_pe.deduplicated_sorted_MAPQ20_bcftools_Normalised_MitoReads_part1_2.vcf, _val.R1_bismark_bt2_pe.deduplicated_sorted_MAPQ20_bcftools_Normalised_MitoReads_part2_3.vcf, and _val.R1_bismark_bt2_pe.deduplicated_sorted_MAPQ20_bcftools_Normalised_MitoReads_final.vcf

The sbatch script will also produce an output informing you of what has happened and what went wrong, this will be outputted in a .out file. The name of this file can be changed adapting the SBatch-Script-For-pipeline.sh script.

## How to run MitoCall

   1. Change variables.sh or variables-xargs.sh according to the values, filenames and paths required
   2. Optional: Change the ListSamples.dat according to the names of samples being used
   3. Change sbatch script (SBatch-Script-For-pipeline.sh or SBatch-Script-For-pipeline-xargs.sh) according to the file paths required
   4. Change PythonScript_HetTable.py to have the necessary path to file requried
   5. Make sure that all the symstem requirements (see section above) are met
   6. Run the sbatch script (SBatch-Script-For-pipeline.sh or SBatch-Script-For-pipeline-xargs.sh)
   7. Once step 6 is completed, run the python script (PythonScript_HetTable.py)

You should now have an output csv file.

## Extra notes

The pipeline script (SBatch-Script-For-pipeline.sh) includes headers that were added for convenience to spot which step of the pipeline has been successfully completed and if an error took place, allows the user to more easily spot where this has happened. By default, these headers can be seen as: "Next step starts here: trimming!". If the user does a search for terms like "Next step starts here", they should be able to find which was the last step that was completed and where the issue took place.

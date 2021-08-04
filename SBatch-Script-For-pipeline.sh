#!/bin/bash


#SBATCH -J jobname
#SBATCH -t 72:00:00
#SBATCH --output=sbatch_output_file.out
#SBATCH -D /working/directory/where/output/files/are/placed
#SBATCH -c number of cpus necessaryto run the job
#SBATCH -N 1
#SBATCH --partition=name_of_server_partition

/path/to/sbatchScript/SBatch-full-align-pipeline.sh {}

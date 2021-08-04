#!/bin/bash


#SBATCH -J jobname
#SBATCH -t 72:00:00
#SBATCH --output=sbatch_output_file.out
#SBATCH -D /working/directory/where/output/files/are/placed
#SBATCH -c 4
#SBATCH -N 1
#SBATCH --partition=name_of_server_partition

cat ListSamples.dat | xargs -i -t -n 1 -P 4  /path/to/sbatchScript/SBatch-full-align-pipeline.sh {}

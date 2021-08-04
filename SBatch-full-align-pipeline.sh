#!/bin/bash

source variables.sh


awk 'BEGIN {print "Next step starts here: unzip!"}'
gunzip /raw/RawGenomicsE/afcl2/Genome_Downloads/Genome_Human_full/GRCh38.p13.genome.fa.gz

awk 'BEGIN {print "Next step starts here: genome preparation!"}'
bismark_genome_preparation --verbose /raw/RawGenomicsE/afcl2/Genome_Downloads/Genome_Human_full/
#Only need to do this once. Perhaps these first two steps are best to do separate and just once.

awk 'BEGIN {print "Next step starts here: trimming!"}'
trim_galore --clip_R1 "${clipping_value}" --clip_R2 "${clipping_value}" --paired --fastqc "${input_dir}/${filename}"_1.fastq.gz  "${input_dir}/${filename}"_2.fastq.gz

awk 'BEGIN {print "Next step starts here: renaming files!"}'
mv "${working_dir}/${filename}"_1_val_1.fq.gz "${working_dir}/${filename}"_val.R1.fastq.gz

mv "${working_dir}/${filename}"_2_val_2.fq.gz "${working_dir}/${filename}"_val.R2.fastq.gz

awk 'BEGIN {print "Next step starts here: aligning sequences!"}'
bismark --non_directional --genome "${genome_dir}" -1 "${working_dir}/${filename}"_val.R1.fastq.gz -2 "${working_dir}/${filename}"_val.R2.fastq.gz

awk 'BEGIN {print "Next step starts here: deduplication!"}'
deduplicate_bismark --bam -p "${filename}"_val.R1_bismark_bt2_pe.bam 

awk 'BEGIN {print "Next step starts here: sorting!"}'
samtools sort -o "${filename}"_val.R1_bismark_bt2_pe.deduplicated_sorted.bam "${filename}"_val.R1_bismark_bt2_pe.deduplicated.bam

awk 'BEGIN {print "Next step starts here: mapping quality control!"}'
samtools view -b -q "${mapping_quality}" "${filename}"_val.R1_bismark_bt2_pe.deduplicated_sorted.bam > "${filename}"_val.R1_bismark_bt2_pe.deduplicated_sorted_MAPQ20.bam

awk 'BEGIN {print "Next step starts here: pileup, variant calling!"}'
bcftools mpileup -B -Ou --max-depth 1000 -Q "${base_quality}" -f "${genome_dir}"/GRCh38.p13.genome.fa "${filename}"_val.R1_bismark_bt2_pe.deduplicated_sorted_MAPQ20.bam | bcftools call -m -Ov -o "${filename}"_val.R1_bismark_bt2_pe.deduplicated_sorted_MAPQ20_bcftools.vcf

awk 'BEGIN {print "Next step starts here: normalisation of variant calling!"}'
bcftools norm -f "${genome_dir}"/GRCh38.p13.genome.fa "${filename}"_val.R1_bismark_bt2_pe.deduplicated_sorted_MAPQ20_bcftools.vcf > "${filename}"_val.R1_bismark_bt2_pe.deduplicated_sorted_MAPQ20_bcftools_Normalised.vcf

awk 'BEGIN {print "Next step starts here: selecting mito reads from vcf file!"}'
cat "${filename}"_val.R1_bismark_bt2_pe.deduplicated_sorted_MAPQ20_bcftools_Normalised.vcf | grep -w chrM > "${filename}"_val.R1_bismark_bt2_pe.deduplicated_sorted_MAPQ20_bcftools_Normalised_MitoReads.vcf

awk 'BEGIN {print "Next step starts here: producing table with only desirable columns!"}'
awk '/DP4=/ {dap=index($0,"DP4=");posdap=index(substr($0,dap+4,256),";");print $1,$2,$3,$4,$5,$6,$7,substr($0,dap+4,posdap-1)}' "${filename}"_val.R1_bismark_bt2_pe.deduplicated_sorted_MAPQ20_bcftools_Normalised_MitoReads.vcf > "${filename}"_val.R1_bismark_bt2_pe.deduplicated_sorted_MAPQ20_bcftools_Normalised_MitoReads_part1_1.vcf

awk '{print$1,$2,$3,$4,$5,$6,$7}' "${filename}"_val.R1_bismark_bt2_pe.deduplicated_sorted_MAPQ20_bcftools_Normalised_MitoReads_part1_1.vcf > "${filename}"_val.R1_bismark_bt2_pe.deduplicated_sorted_MAPQ20_bcftools_Normalised_MitoReads_part1_2.vcf

awk '{print $8}' "${filename}"_val.R1_bismark_bt2_pe.deduplicated_sorted_MAPQ20_bcftools_Normalised_MitoReads_part1_1.vcf | awk -F',' '{print $1,$2,$3,$4}' - > "${filename}"_val.R1_bismark_bt2_pe.deduplicated_sorted_MAPQ20_bcftools_Normalised_MitoReads_part2_3.vcf

paste "${filename}"_val.R1_bismark_bt2_pe.deduplicated_sorted_MAPQ20_bcftools_Normalised_MitoReads_part1_2.vcf "${filename}"_val.R1_bismark_bt2_pe.deduplicated_sorted_MAPQ20_bcftools_Normalised_MitoReads_part2_3.vcf | awk 'BEGIN{print "CHROM POS ID REF ALT QUAL FILTER DP4-Ref-Fwd DP4-Ref-Rev DP4-Alt-Fwd DP4-Alt-Rev"};{print $1,$2,$3,$4,$5,$6,$7,$8,$9,$10,$11}' -  > "${filename}"_val.R1_bismark_bt2_pe.deduplicated_sorted_MAPQ20_bcftools_Normalised_MitoReads_final.vcf


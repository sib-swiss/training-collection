# Bioinformatics training materials

A curated list of **bioinformatics training material**. All material is:

- In a GitHub repository
- Free to use
- Written in markdown or similar

**NOTE:** This list of courses is selected *only* based on the above criteria. There are *no* checks on quality. 
 
Is your (favourite) course not in there? Any contribution to this list is highly appreciated :+1:. Please have a look at [CONTRIBUTING.md](CONTRIBUTING.md) first.

## Contents

- [Scripting and languages](#scripting-and-languages)
  - [UNIX shell](#unix-shell)
  - [Python](#python)
  - [R](#R)
  - [git](#git)
- [Sequence data analysis](#sequence-data-analysis)
  - [General](#general)  
  - [RNA-seq](#rna-seq)
  - [ChIP-seq](#chip-seq)
  - [Single cell](#single-cell)
  - [Variant analysis](#variant-analysis)
  - [Genome Assembly](#genome-assembly)
- [Computational methods and pipelines](#computational-methods-and-pipelines)
  - [Containers](#containers)
  - [Nextflow](#nextflow)
  - [Snakemake](#snakemake) 
  - [High performance computing](#high-performance-computing)
- [Reproducibility and data management](#reproducibility-and-data-management)
  - [Reproducibility](#reproducibility)
  - [Data management](#data-management)

## Scripting and languages

### UNIX shell

- [**Carpentries** The Unix Shell](https://github.com/swcarpentry/shell-novice) | [website](https://swcarpentry.github.io/shell-novice/)
- [**bioinformaticsworkbook.org** Introduction to Unix](https://github.com/ISUgenomics/bioinformatics-workbook) | [website](https://bioinformaticsworkbook.org/Appendix/Unix/unix-basics-1.html#gsc.tab=0)
- [**Harvard Chan Bioinformatics Core** Introduction to the command-line interface (shell)](https://github.com/hbctraining/Intro-to-shell-flipped) | [website](https://hbctraining.github.io/Intro-to-shell-flipped/schedule/links-to-lessons.html)


### Python

- [**Carpentries** Programming with Python](https://github.com/swcarpentry/python-novice-inflammation) | [website](https://swcarpentry.github.io/python-novice-inflammation/)
- [**Harvard Chan Bioinformatics Core** Introduction to Python](https://github.com/hbctraining/Training-modules) | [website](https://hbctraining.github.io/Training-modules/Python/)

### R

- [**Carpentries** R for Reproducible Scientific Analysis](https://github.com/swcarpentry/r-novice-gapminder) | [website](https://swcarpentry.github.io/r-novice-gapminder/)
- [**Harvard Chan Bioinformatics Core** Introduction to R](https://github.com/hbctraining/Intro-to-R-flipped) | [website](https://hbctraining.github.io/Intro-to-R-flipped/schedules/links-to-lessons.html)
- [**Harvard Chan Bioinformatics Core** Introduction to R - Practical workshop](https://github.com/hbctraining/Training-modules) | [website](https://hbctraining.github.io/Training-modules/IntroR_practical_online_resource/)

### git

- [**Carpentries** Version Control with Git](https://github.com/swcarpentry/git-novice) | [website](https://swcarpentry.github.io/git-novice/)

## Sequence data analysis

### General

- [**SIB** NGS: Quality control, Alignment, Visualisation](https://github.com/sib-swiss/NGS-introduction-training) | [website](https://sib-swiss.github.io/NGS-introduction-training/)
- [**Harvard Chan Bioinformatics Core** Accessing genomic reference and experimental sequencing data](https://github.com/hbctraining/Accessing_public_genomic_data) | [website](https://hbctraining.github.io/Accessing_public_genomic_data/)

### RNA-seq

- [**SIB** Introduction to RNA-Seq: From quality control to pathway analysis](https://github.com/sib-swiss/RNAseq-introduction-training) | [website](https://sib-swiss.github.io/RNAseq-introduction-training/)
- [**Carpentries** RNA-seq analysis with Bioconductor](https://github.com/carpentries-incubator/bioc-rnaseq) | [website](https://carpentries-incubator.github.io/bioc-rnaseq/)
- [**bioinformaticsworkbook.org** RNA-Seq data Analysis](https://github.com/ISUgenomics/bioinformatics-workbook) | [website](https://bioinformaticsworkbook.org/dataAnalysis/RNA-Seq/RNA-SeqIntro/RNAseq-using-a-genome.html#gsc.tab=0)
- [**bioinformaticsworkbook.org** Differential Gene Expression analysis](https://github.com/ISUgenomics/bioinformatics-workbook) | [website](https://bioinformaticsworkbook.org/dataAnalysis/RNA-Seq/RNA-SeqIntro/Differential-Expression-Analysis.html#gsc.tab=0)
- [**Harvard Chan Bioinformatics Core** Introduction to bulk RNA-seq](https://github.com/hbctraining/Intro-to-rnaseq-hpc-salmon-flipped) | [website](https://hbctraining.github.io/Intro-to-rnaseq-hpc-salmon-flipped/schedule/links-to-lessons.html)
- [**Harvard Chan Bioinformatics Core** Differential Gene Expression Analysis](https://github.com/hbctraining/DGE_workshop_salmon_online) | [website](https://hbctraining.github.io/DGE_workshop_salmon_online/schedule/links-to-lessons.html)

### ChIP-seq

- [**Harvard Chan Bioinformatics Core** Introduction to ChIP-seq using high performance computing](https://github.com/hbctraining/Intro-to-ChIPseq) | [website](https://hbctraining.github.io/Intro-to-ChIPseq/)

### Single cell

- [**SIB** Single-cell Transcriptomics](https://github.com/sib-swiss/single-cell-training/) | [website](https://sib-swiss.github.io/single-cell-training/latest/)
- [**SIB** NBIS/SciLifeLab Advanced topics in Single Cell Omics](https://github.com/NBISweden/single-cell_sib_scilifelab_2021) | [website](https://nbisweden.github.io/single-cell_sib_scilifelab_2021/)
- [**SIB** Advanced topics in single-cell transcriptomics](https://github.com/fmicompbio/adv_scrnaseq_2020)
- [**University of Cambridge** Introduction to single-cell RNA-seq data analysis](https://github.com/bioinformatics-core-shared-training/UnivCambridge_ScRnaSeq_Nov2021/) | [website](https://bioinformatics-core-shared-training.github.io/UnivCambridge_ScRnaSeq_Nov2021/)
- [**NBIS** Single cell RNA-seq analysis workshop](https://github.com/nbisweden/workshop-scRNAseq) | [website](https://nbisweden.github.io/workshop-scRNAseq/)
- [**MGC/BioSB** Course - Single Cell Analysis](https://github.com/LeidenCBC/MGC-BioSB-SingleCellAnalysis2021)
- [**Harvard Chan Bioinformatics Core** Single-cell RNA-seq data analysis workshop](https://github.com/hbctraining/scRNA-seq_online) | [website](https://hbctraining.github.io/scRNA-seq_online/schedule/links-to-lessons.html)

### Variant analysis

- [**SIB** NGS - Genome variant analysis](https://github.com/sib-swiss/NGS-variants-training/) | [website](https://sib-swiss.github.io/NGS-variants-training/)
- [**bioinformaticsworkbook.org** Variant Discovery](https://github.com/ISUgenomics/bioinformatics-workbook) | [website](https://bioinformaticsworkbook.org/dataAnalysis/VariantCalling/variant-calling-index.html#gsc.tab=0)

### Genome assembly

- [**bioinformaticsworkbook.org** Introduction to Genome Assembly](https://github.com/ISUgenomics/bioinformatics-workbook) | [website](https://bioinformaticsworkbook.org/dataAnalysis/GenomeAssembly/Intro_GenomeAssembly.html#gsc.tab=0)

## Computational methods and pipelines

### Containers

- [**SIB** Docker and Singularity for reproducible research: getting started with containers](https://github.com/sib-swiss/containers-introduction-training) | [website](https://sib-swiss.github.io/containers-introduction-training/latest/)
- [**Carpentries** Reproducible Computational Environments Using Containers: Introduction to Docker](https://github.com/carpentries-incubator/docker-introduction) | [website](https://carpentries-incubator.github.io/docker-introduction/)
- [**Carpentries** Reproducible computational environments using containers: Introduction to Singularity](https://github.com/carpentries-incubator/singularity-introduction) | [website](https://carpentries-incubator.github.io/singularity-introduction/)
- [**rOpenSci Labs** R Docker tutorial](https://github.com/jsta/r-docker-tutorial) | [website](https://jsta.github.io/r-docker-tutorial/)

### Nextflow

- [**CRG SIB** Reproducible research and data analysis using Nextflow pipelines](https://github.com/biocorecrg/SIB_course_nextflow_Nov_2021) | [website](https://biocorecrg.github.io/SIB_course_nextflow_Nov_2021/docs/)

### Snakemake

### High performance computing

- [**Carpentries** Introduction to High-Performance Computing](https://github.com/carpentries-incubator/hpc-intro) | [website](https://carpentries-incubator.github.io/hpc-intro/)

## Reproducibility and data management

### Reproducibility

- [**Harvard Chan Bioinformatics Core** Tools for Reproducible Research](https://github.com/hbctraining/reproducibility-tools) | [website](https://hbctraining.github.io/reproducibility-tools/)

## Data management


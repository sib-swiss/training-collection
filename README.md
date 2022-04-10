[![DOI](https://zenodo.org/badge/437832906.svg)](https://zenodo.org/badge/latestdoi/437832906)
![lychee workflow](https://github.com/sib-swiss/training-collection/actions/workflows/lychee-action.yml/badge.svg)
![toc workflow](https://github.com/sib-swiss/training-collection/actions/workflows/toc-generator.yml/badge.svg)

# Bioinformatics training materials

A curated list of **bioinformatics training material**. All material is:

- In a GitHub or GitLab repository
- Free to use
- Written in markdown or similar

**NOTE:** This list of courses is selected *only* based on the above criteria. There are *no* checks on quality. 
 
Is your (favourite) course not in there? Is a link dead? Did you find a typo? Any contribution to this list is highly appreciated :+1:. Please have a look at [CONTRIBUTING.md](CONTRIBUTING.md) first.

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
## Contents

- [Scripting and languages](#scripting-and-languages)
  - [UNIX shell](#unix-shell)
  - [Python](#python)
  - [R](#r)
  - [git](#git)
- [Sequence data analysis](#sequence-data-analysis)
  - [General](#general)
  - [Miscellaneous](#miscellaneous)
  - [RNA-seq](#rna-seq)
  - [ChIP-seq](#chip-seq)
  - [Single cell](#single-cell)
  - [Variant analysis](#variant-analysis)
  - [Genome assembly](#genome-assembly)
  - [Metagenomics](#metagenomics)
- [Computational methods and pipelines](#computational-methods-and-pipelines)
  - [Containers](#containers)
  - [Nextflow](#nextflow)
  - [Snakemake](#snakemake)
  - [Galaxy](#galaxy)
  - [CWL](#cwl)
  - [High performance computing](#high-performance-computing)
- [Statistics and machine learning](#statistics-and-machine-learning)
  - [Statistics](#statistics)
  - [Machine learning](#machine-learning)
- [Reproducibility and data management](#reproducibility-and-data-management)
  - [Reproducibility](#reproducibility)
  - [Data management](#data-management)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Scripting and languages

### UNIX shell

- [**Carpentries** The Unix Shell](https://github.com/swcarpentry/shell-novice) | [website](https://swcarpentry.github.io/shell-novice/)
- [**Carpentries** Introduction to the Command Line for Genomics](https://github.com/datacarpentry/shell-genomics) | [website](https://datacarpentry.org/shell-genomics/)
- [**bioinformaticsworkbook.org** Introduction to Unix](https://github.com/ISUgenomics/bioinformatics-workbook) | [website](https://bioinformaticsworkbook.org/Appendix/Unix/unix-basics-1.html#gsc.tab=0)
- [**Harvard Chan Bioinformatics Core** Introduction to the command-line interface (shell)](https://github.com/hbctraining/Intro-to-shell-flipped) | [website](https://hbctraining.github.io/Intro-to-shell-flipped/schedule/links-to-lessons.html)

### Python

- [**SIB** First Steps with Python in Life Sciences](https://github.com/sib-swiss/first-steps-with-python-training/)
- [**Carpentries** Programming with Python](https://github.com/swcarpentry/python-novice-inflammation) | [website](https://swcarpentry.github.io/python-novice-inflammation/)
- [**Harvard Chan Bioinformatics Core** Introduction to Python](https://github.com/hbctraining/Training-modules) | [website](https://hbctraining.github.io/Training-modules/Python/)
- [**Carpentries** Interactive Data Visualizations in Python](https://github.com/carpentries-incubator/python-interactive-data-visualizations) | [website](https://carpentries-incubator.github.io/python-interactive-data-visualizations/)

### R

- [**SIB** First Steps with R in Life Sciences](https://github.com/sib-swiss/first-steps-with-R-training) 
- [**Carpentries** R for Reproducible Scientific Analysis](https://github.com/swcarpentry/r-novice-gapminder) | [website](https://swcarpentry.github.io/r-novice-gapminder/)
- [**Harvard Chan Bioinformatics Core** Introduction to R](https://github.com/hbctraining/Intro-to-R-flipped) | [website](https://hbctraining.github.io/Intro-to-R-flipped/schedules/links-to-lessons.html)
- [**Harvard Chan Bioinformatics Core** Introduction to R - Practical workshop](https://github.com/hbctraining/Training-modules) | [website](https://hbctraining.github.io/Training-modules/IntroR_practical_online_resource/)
- [**DKFZ** University of Heidelberg Basic R course](https://github.com/CompEpigen/BasicR/) | [website](https://compepigen.github.io/BasicR/)


### git

- [**Carpentries** Version Control with Git](https://github.com/swcarpentry/git-novice) | [website](https://swcarpentry.github.io/git-novice/)

## Sequence data analysis

### General

- [**SIB** NGS: Quality control, Alignment, Visualisation](https://github.com/sib-swiss/NGS-introduction-training) | [website](https://sib-swiss.github.io/NGS-introduction-training/)
- [**Harvard Chan Bioinformatics Core** Accessing genomic reference and experimental sequencing data](https://github.com/hbctraining/Accessing_public_genomic_data) | [website](https://hbctraining.github.io/Accessing_public_genomic_data/)
- [**CRUK** Workshop on Functional Genomics - summer school 2020](https://github.com/bioinformatics-core-shared-training/cruk-summer-school-2020) | [website](https://bioinformatics-core-shared-training.github.io/cruk-summer-school-2020/)

### Miscellaneous

- [**James W. MacDonald** Introduction to Bioconductor annotation resources](https://github.com/jmacdon/Bioc2020Anno) | [website](https://jmacdon.github.io/Bioc2020Anno/)
- [**Waldron lab CUNY** Public data resources and Bioconductor](https://github.com/jmacdon/Bioc2020Anno) | [website](https://waldronlab.io/PublicDataResources/)
- [**Waldron lab CUNY** Functional enrichment analysis of high-throughput omics data](https://github.com/waldronlab/enrichOmics) | [website](https://waldronlab.io/enrichOmics/)
- [**WEHI**  Gene-set enrichment analysis workshop](https://github.com/DavisLaboratory/GenesetAnalysisWorkflow/) | [website](https://davislaboratory.github.io/GenesetAnalysisWorkflow/)
- [**Waldron lab CUNY** Multi-omic Integration of cBioPortal and TCGA data with MultiAssayExperiment](https://github.com/waldronlab/MultiAssayWorkshop/) | [website](https://waldronlab.io/MultiAssayWorkshop/)


### RNA-seq

- [**SIB** Introduction to RNA-Seq: From quality control to pathway analysis](https://github.com/sib-swiss/RNAseq-introduction-training) | [website](https://sib-swiss.github.io/RNAseq-introduction-training/)
- [**Carpentries** RNA-seq analysis with Bioconductor](https://github.com/carpentries-incubator/bioc-rnaseq) | [website](https://carpentries-incubator.github.io/bioc-rnaseq/)
- [**bioinformaticsworkbook.org** RNA-Seq data Analysis](https://github.com/ISUgenomics/bioinformatics-workbook) | [website](https://bioinformaticsworkbook.org/dataAnalysis/RNA-Seq/RNA-SeqIntro/RNAseq-using-a-genome.html#gsc.tab=0)
- [**bioinformaticsworkbook.org** Differential Gene Expression analysis](https://github.com/ISUgenomics/bioinformatics-workbook) | [website](https://bioinformaticsworkbook.org/dataAnalysis/RNA-Seq/RNA-SeqIntro/Differential-Expression-Analysis.html#gsc.tab=0)
- [**Harvard Chan Bioinformatics Core** Introduction to bulk RNA-seq](https://github.com/hbctraining/Intro-to-rnaseq-hpc-salmon-flipped) | [website](https://hbctraining.github.io/Intro-to-rnaseq-hpc-salmon-flipped/schedule/links-to-lessons.html)
- [**Harvard Chan Bioinformatics Core** Differential Gene Expression Analysis](https://github.com/hbctraining/DGE_workshop_salmon_online) | [website](https://hbctraining.github.io/DGE_workshop_salmon_online/schedule/links-to-lessons.html)
- [**CRUK CI** Introduction to Bulk RNA-seq data analysis](https://github.com/bioinformatics-core-shared-training/Bulk_RNASeq_Course_Nov21) | [website](https://bioinformatics-core-shared-training.github.io/Bulk_RNASeq_Course_Nov21/)
- [**Stefano Mangiola** A Tidy Transcriptomics introduction to RNA sequencing analyses](https://github.com/stemangiola/bioc_2020_tidytranscriptomics/) | [website](https://stemangiola.github.io/bioc_2020_tidytranscriptomics/)
- [**WEHI** Workshop: RNA-seq analysis is easy as 1-2-3 with limma, Glimma and edgeR](https://github.com/XueyiDong/RNAseq123workshop/) | [website](https://xueyidong.github.io/RNAseq123workshop/index.html)
- [**EBI** Bulk RNA-seq tutorial](https://gitlab.com/mperalc/bulk_RNA-seq_workshop_2021/) | [website](https://mperalc.gitlab.io/bulk_RNA-seq_workshop_2021/)

### ChIP-seq

- [**Harvard Chan Bioinformatics Core** Introduction to ChIP-seq using high performance computing](https://github.com/hbctraining/Intro-to-ChIPseq) | [website](https://hbctraining.github.io/Intro-to-ChIPseq/)
- [**CRUK CI** Quantitiative analysis of ChiP-seq, ATAC-seq, and related DNA enrichment assays](https://github.com/bioinformatics-core-shared-training/Quantitative-ChIPseq-Workshop)
- [**UMass MCCB** Best practices for ATAC-seq QC and data analysis](https://github.com/haibol2016/ATACseqQCWorkshop/) | [website](https://haibol2016.github.io/ATACseqQCWorkshop/)
- [**UMass** Integrated ChIP-seq Data Analysis Workshop](https://github.com/hukai916/IntegratedChIPseqWorkshop/) | [website](https://hukai916.github.io/IntegratedChIPseqWorkshop/)

### Single cell

- [**SIB** Single-cell Transcriptomics](https://github.com/sib-swiss/single-cell-training/) | [website](https://sib-swiss.github.io/single-cell-training/latest/)
- [**SIB NBIS/SciLifeLab** Advanced topics in Single Cell Omics](https://github.com/NBISweden/single-cell_sib_scilifelab_2021) | [website](https://nbisweden.github.io/single-cell_sib_scilifelab_2021/)
- [**SIB** Advanced topics in single-cell transcriptomics](https://github.com/fmicompbio/adv_scrnaseq_2020)
- [**CRUK CI** Introduction to single-cell RNA-seq data analysis](https://github.com/bioinformatics-core-shared-training/UnivCambridge_ScRnaSeq_Nov2021/) | [website](https://bioinformatics-core-shared-training.github.io/UnivCambridge_ScRnaSeq_Nov2021/)
- [**NBIS** Single cell RNA-seq analysis workshop](https://github.com/nbisweden/workshop-scRNAseq) | [website](https://nbisweden.github.io/workshop-scRNAseq/)
- [**MGC/BioSB** Course - Single Cell Analysis](https://github.com/LeidenCBC/MGC-BioSB-SingleCellAnalysis2021)
- [**Harvard Chan Bioinformatics Core** Single-cell RNA-seq data analysis workshop](https://github.com/hbctraining/scRNA-seq_online) | [website](https://hbctraining.github.io/scRNA-seq_online/schedule/links-to-lessons.html)
- [**WEHI**  Single cell RNA-seq analysis workshop](https://github.com/yunshun/SingleCellWorkshop/) | [website](https://yunshun.github.io/SingleCellWorkshop/)
- [**Dana-Farber Cancer Institute** Trajectory inference across conditions: differential expression and differential progression](https://github.com/kstreet13/bioc2020trajectories) | [website](https://kstreet13.github.io/bioc2020trajectories/)
- [**ELIXIR EXCELERATE** Single RNA-seq data analysis with R](https://github.com/NBISweden/excelerate-scRNAseq) | [website](https://nbisweden.github.io/excelerate-scRNAseq/)
- [**EBI** Single cell RNA-seq tutorial](https://gitlab.com/mperalc/scRNA-seq_workshop_2021) | [website](https://mperalc.gitlab.io/scRNA-seq_workshop_2021/)

### Variant analysis

- [**SIB** NGS - Genome variant analysis](https://github.com/sib-swiss/NGS-variants-training/) | [website](https://sib-swiss.github.io/NGS-variants-training/)
- [**bioinformaticsworkbook.org** Variant Discovery](https://github.com/ISUgenomics/bioinformatics-workbook) | [website](https://bioinformaticsworkbook.org/dataAnalysis/VariantCalling/variant-calling-index.html#gsc.tab=0)
- [**WEHI** A introduction to SNV analyses in whole genome sequencing](https://github.com/PapenfussLab/IntroductionToGenomicsWorkshop/) | [website](https://papenfusslab.github.io/IntroductionToGenomicsWorkshop/)
- [**Waldron lab CUNY** Copy number variation analysis with Bioconductor](https://github.com/waldronlab/CNVWorkshop) | [website](https://waldronlab.io/CNVWorkshop/)
- [**Sateesh Peri** Nextflow Tutorial - Variant Calling Edition](https://github.com/sateeshperi/nextflow_varcal) | [website](https://sateeshperi.github.io/nextflow_varcal/nextflow/)

### Genome assembly

- [**bioinformaticsworkbook.org** Introduction to Genome Assembly](https://github.com/ISUgenomics/bioinformatics-workbook) | [website](https://bioinformaticsworkbook.org/dataAnalysis/GenomeAssembly/Intro_GenomeAssembly.html#gsc.tab=0)

### Metagenomics

- [**Waldron lab CUNY**  Curated Metagenomic Analyses](https://github.com/waldronlab/curatedMetagenomicDataAnalyses) | [website](https://waldronlab.io/curatedMetagenomicDataAnalyses/)

## Computational methods and pipelines

### Containers

- [**SIB** Docker and Singularity for reproducible research: getting started with containers](https://github.com/sib-swiss/containers-introduction-training) | [website](https://sib-swiss.github.io/containers-introduction-training/latest/)
- [**Carpentries** Reproducible Computational Environments Using Containers: Introduction to Docker](https://github.com/carpentries-incubator/docker-introduction) | [website](https://carpentries-incubator.github.io/docker-introduction/)
- [**Carpentries** Reproducible computational environments using containers: Introduction to Singularity](https://github.com/carpentries-incubator/singularity-introduction) | [website](https://carpentries-incubator.github.io/singularity-introduction/)
- [**rOpenSci Labs** R Docker tutorial](https://github.com/jsta/r-docker-tutorial) | [website](https://jsta.github.io/r-docker-tutorial/)

### Nextflow

- [**CRG SIB** Reproducible research and data analysis using Nextflow pipelines](https://github.com/biocorecrg/SIB_course_nextflow_Nov_2021) | [website](https://biocorecrg.github.io/SIB_course_nextflow_Nov_2021/docs/)
- [**Carpentries** Introduction to Bioinformatics workflows with Nextflow and nf-core](https://github.com/carpentries-incubator/workflows-nextflow) | [website](https://carpentries-incubator.github.io/workflows-nextflow/)
- [**CRG BovReg** Nextflow training](https://github.com/bovreg/nf-workshop20) | [website](https://bovreg.github.io/nf-workshop20/)
- [**CRG** Reproducible research and data analysis with Linux containers and Nextflow pipelines](https://github.com/biocorecrg/CoursesCRG_Containers_Nextflow_May_2021) | [website](https://biocorecrg.github.io/CoursesCRG_Containers_Nextflow_May_2021/)
- [**CRUK CI** nextflow_september_2021](https://github.com/bioinformatics-core-shared-training/nextflow_september_2021) 
- [**Sateesh Peri** Nextflow Tutorial - Variant Calling Edition](https://github.com/sateeshperi/nextflow_varcal) | [website](https://sateeshperi.github.io/nextflow_varcal/nextflow/)

### Snakemake

- [**Snakemake** Snakemake Tutorial](https://github.com/snakemake/snakemake) | [website](https://snakemake.readthedocs.io/en/stable/tutorial/tutorial.html)
- [**Carpentries** Snakemake for Bioinformatics](https://github.com/carpentries-incubator/snakemake-novice-bioinformatics) | [website](https://carpentries-incubator.github.io/snakemake-novice-bioinformatics/)
- [**Carpentries** Getting Started with Snakemake](https://github.com/carpentries-incubator/workflows-snakemake) | [website](https://carpentries-incubator.github.io/workflows-snakemake/)

### Galaxy

- [**Galaxy** Training](https://github.com/galaxyproject/training-material) | [website](https://training.galaxyproject.org/training-material/)

### CWL

- [**Roswell Park** Connecting Bioconductor to other bioinformatics tools using `Rcwl`](https://github.com/liubuntu/Bioc2020Rcwl) | [website](https://liubuntu.github.io/Bioc2020RCWL/) 
- [**INAB/CERTH** Introduction to CWL and Docker](https://github.com/BiodataAnalysisGroup/intro-to-cwl-docker) | [website](https://biodataanalysisgroup.github.io/intro-to-cwl-docker/)

### High performance computing

- [**Carpentries** Introduction to High-Performance Computing](https://github.com/carpentries-incubator/hpc-intro) | [website](https://carpentries-incubator.github.io/hpc-intro/)
- [**NIH CFDE** Introduction to Remote Computing](https://github.com/ngs-docs/2021-august-remote-computing) | [website](https://ngs-docs.github.io/2021-august-remote-computing)

## Statistics and machine learning

### Statistics

- [**Danielle Navarro** Learning Statistics with R ](https://github.com/djnavarro/rbook) | [website](https://learningstatisticswithr.com/book/)
- [**CRUK CI** Introduction to Statistical Analysis](https://github.com/bioinformatics-core-shared-training/IntroductionToStats) | [website](https://github.com/bioinformatics-core-shared-training/IntroductionToStats)
- [**CRUK CI** Experimental design](https://github.com/bioinformatics-core-shared-training/experimental-design) | [website](http://bioinformatics-core-shared-training.github.io/experimental-design/)
- [**CRUK CI** linear-models-r](https://github.com/bioinformatics-core-shared-training/linear-models-r) | [website](https://bioinformatics-core-shared-training.github.io/linear-models-r/)
- [**Aedin Culhane** Dimension Reduction for Beginners: Hitchhiker’s Guide to Matrix Factorization and PCA](https://github.com/aedin/PCAworkshop/) | [website](https://aedin.github.io/PCAworkshop/)
- [**SIB** Statistics and Machine Learning (Python)](https://github.com/sib-swiss/statistics-and-machine-learning-training)

### Machine learning

- [**SIB** Introduction to Machine Learning (Python)](https://github.com/sib-swiss/intro-machine-learning-training)
- [**Carpentries** Introduction to Machine Learning with Scikit Learn](https://github.com/carpentries-incubator/machine-learning-novice-sklearn) | [website](https://carpentries-incubator.github.io/machine-learning-novice-sklearn/)
- [**Carpentries** Introduction to Machine Learning in Python](https://github.com/carpentries-incubator/machine-learning-novice-python) | [website](https://carpentries-incubator.github.io/machine-learning-novice-python/)

## Reproducibility and data management

### Reproducibility

- [**Harvard Chan Bioinformatics Core** Tools for Reproducible Research](https://github.com/hbctraining/reproducibility-tools) | [website](https://hbctraining.github.io/reproducibility-tools/)
- [**Carpentries** FAIR in (biological) practice](https://github.com/carpentries-incubator/fair-bio-practice) | [website](https://carpentries-incubator.github.io/fair-bio-practice/)
- [**Carpentries** Introduction to Conda for (Data) Scientists](https://github.com/carpentries-incubator/introduction-to-conda-for-data-scientists) | [website](https://carpentries-incubator.github.io/introduction-to-conda-for-data-scientists/)
- [**FAIRplus** FAIR Cookbook](https://github.com/FAIRplus/the-fair-cookbook) | [website](https://fairplus.github.io/the-fair-cookbook/content/home.html)

### Data management

- [**Carpentries** From a Spreadsheet to a Database](https://github.com/carpentries-incubator/capstone-novice-spreadsheet-biblio) | [website](https://carpentries-incubator.github.io/capstone-novice-spreadsheet-biblio/)
- [**CRUK CI** Managing your Research Data: Best practices in Research Data Management for Biological Sciences](https://github.com/bioinformatics-core-shared-training/Managing-your-research-data) | [website](https://bioinformatics-core-shared-training.github.io/Managing-your-research-data/)

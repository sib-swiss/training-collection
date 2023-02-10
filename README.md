[![DOI](https://zenodo.org/badge/437832906.svg)](https://zenodo.org/badge/latestdoi/437832906)
![lychee workflow](https://github.com/sib-swiss/training-collection/actions/workflows/lychee-action.yml/badge.svg)
![toc workflow](https://github.com/sib-swiss/training-collection/actions/workflows/toc-generator.yml/badge.svg)
![badge](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/GeertvanGeest/5dd50ff10dbb3fe3222aa8ac658878bf/raw/ncourses.json)

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
  - [Spatial transcriptomics](#spatial-transcriptomics)
  - [Variant analysis](#variant-analysis)
  - [Genome assembly & annotation](#genome-assembly--annotation)
  - [Metagenomics/microbial](#metagenomicsmicrobial)
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
  - [FAIR & Reproducibility](#fair--reproducibility)
  - [Data management](#data-management)
- [Image analysis](#image-analysis)
- [Other lists](#other-lists)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Scripting and languages

### UNIX shell

- [**SIB** First Steps with UNIX](https://github.com/sib-swiss/unix-first-steps-training)
- [**Carpentries** The Unix Shell](https://github.com/swcarpentry/shell-novice) | [website](https://swcarpentry.github.io/shell-novice/)
- [**Carpentries** Introduction to the Command Line for Genomics](https://github.com/datacarpentry/shell-genomics) | [website](https://datacarpentry.org/shell-genomics/)
- [**bioinformaticsworkbook.org** Introduction to Unix](https://github.com/ISUgenomics/bioinformatics-workbook) | [website](https://bioinformaticsworkbook.org/Appendix/Unix/unix-basics-1.html#gsc.tab=0)
- [**Harvard Chan Bioinformatics Core** Introduction to the command-line interface (shell)](https://github.com/hbctraining/Intro-to-shell-flipped) | [website](https://hbctraining.github.io/Intro-to-shell-flipped/schedule/links-to-lessons.html)
- [**Ted Laderas** Bash for bioinformatics](https://github.com/laderast/bash_for_bioinformatics) | [website](https://laderast.github.io/bash_for_bioinformatics/)

### Python

- [**SIB** First Steps with Python in Life Sciences](https://github.com/sib-swiss/first-steps-with-python-training/)
- [**SIB** Intermediate Python : "data analysis and representation" &  "<s>harder</s> faster better stronger : optimizing python code"](https://github.com/sib-swiss/intermediate-python-training)
- [**Carpentries** Programming with Python](https://github.com/swcarpentry/python-novice-inflammation) | [website](https://swcarpentry.github.io/python-novice-inflammation/)
- [**Harvard Chan Bioinformatics Core** Introduction to Python](https://github.com/hbctraining/Training-modules) | [website](https://hbctraining.github.io/Training-modules/Python/)
- [**Carpentries** Interactive Data Visualizations in Python](https://github.com/carpentries-incubator/python-interactive-data-visualizations) | [website](https://carpentries-incubator.github.io/python-interactive-data-visualizations/)
- [**Jake van der Plas** Python Data Science Handbook](https://github.com/jakevdp/PythonDataScienceHandbook) | [website](https://jakevdp.github.io/PythonDataScienceHandbook/)
- [**Jake van der Plas** A Whirlwind Tour of Python](https://github.com/jakevdp/WhirlwindTourOfPython) | [website](https://jakevdp.github.io/WhirlwindTourOfPython)
- [**Michigan State University** Plants and Python](https://github.com/PlantsAndPython/PlantsAndPython) | [website](https://plantsandpython.github.io/PlantsAndPython)
- [**VIB** Gentle hands-on introduction to Python programming](https://github.com/vibbits/gentle-hands-on-python)

### R

- [**SIB** First Steps with R in Life Sciences](https://github.com/sib-swiss/first-steps-with-R-training)
- [**Carpentries** R for Reproducible Scientific Analysis](https://github.com/swcarpentry/r-novice-gapminder) | [website](https://swcarpentry.github.io/r-novice-gapminder/)
- [**Harvard Chan Bioinformatics Core** Introduction to R](https://github.com/hbctraining/Intro-to-R-flipped) | [website](https://hbctraining.github.io/Intro-to-R-flipped/schedules/links-to-lessons.html)
- [**Harvard Chan Bioinformatics Core** Introduction to R - Practical workshop](https://github.com/hbctraining/Training-modules) | [website](https://hbctraining.github.io/Training-modules/IntroR_practical_online_resource/)
- [**DKFZ** University of Heidelberg Basic R course](https://github.com/CompEpigen/BasicR/) | [website](https://compepigen.github.io/BasicR/)
- [**CRG** Introduction to R (2021)](https://github.com/biocorecrg/CRG_RIntroduction_2021/) | [website](https://biocorecrg.github.io/CRG_RIntroduction_2021/)
- [**CRG** Intermediate R: introduction to data wrangling with the Tidyverse (2021)](https://github.com/biocorecrg/CRG_R_tidyverse_2021/) | [website](https://biocorecrg.github.io/CRG_R_tidyverse_2021/)
- [**NHS** Rmarkdown: reproducible reporting](https://github.com/jthomasmock/rmd-nhs) | [website](https://jthomasmock.github.io/rmd-nhs)
- [**Moderndive** Statistical Inference via Data Science](https://github.com/moderndive/ModernDive_book) | [website](https://moderndive.com/)
- [**Rafael A. Irizarry** Introduction to Data Science](https://github.com/rafalab/dsbook) | [website](https://rafalab.github.io/dsbook/)
- [**Bradley Boehmke** Intro to R Bootcamp](https://github.com/bradleyboehmke/Intro-to-R-Bootcamp) | [website](http://uc-r.github.io/r_bootcamp)
- [**Julia Silge and David Robinson** Text mining with R](https://github.com/dgrtwo/tidy-text-mining) | [website](https://www.tidytextmining.com/)
- [**Rstudio** R Markdown: The Definitive Guide](https://github.com/rstudio/rmarkdown-book) | [website](https://bookdown.org/yihui/rmarkdown)
- [**Jennifer Bryan** purrr tutorial](https://github.com/jennybc/purrr-tutorial) | [website](https://jennybc.github.io/purrr-tutorial/)
- [**Australian Biocommons** Introduction to data analysis with R and Bioconductor](https://github.com/SaskiaFreytag/biocommons-r-intro) | [website](https://saskiafreytag.github.io/biocommons-r-intro/)
- [**rstudio::conf 2022** Graphic Design with ggplot2](https://github.com/rstudio-conf-2022/ggplot2-graphic-design) | [website](https://rstudio-conf-2022.github.io/ggplot2-graphic-design/)
- [**rstudio::conf 2022** Building Production-Quality Shiny Applications](https://github.com/rstudio-conf-2022/shiny-prod-apps) | [website](https://shinyprod.com/)
- [**rstudio::conf 2022** What They Forgot to Teach You About R](https://github.com/rstudio-conf-2022/wtf-rstats) | [website](https://rstudio-conf-2022.github.io/wtf-rstats/)
- [**rstudio::conf 2022** Getting Started with Quarto](https://github.com/rstudio-conf-2022/get-started-quarto) | [website](https://rstudio-conf-2022.github.io/get-started-quarto/)
- [**rstudio::conf 2022** Building tidy tools](https://github.com/rstudio-conf-2022/build-tidy-tools) | [website](https://rstudio-conf-2022.github.io/build-tidy-tools/)
- [**rstudio::conf 2022** Art from code](https://github.com/rstudio-conf-2022/art-from-code) | [website](https://art-from-code.netlify.app/)
- [**rstudio::conf 2022** Introduction to the tidyverse](https://github.com/rstudio-conf-2022/intro-to-tidyverse) | [website](https://conf22-intro-tidyverse.netlify.app/)
- [**rstudio::conf 2022** Getting Started with Shiny](https://github.com/rstudio-conf-2022/get-started-shiny) | [website](https://rstd.io/start-shiny)
- [**rstudio::conf 2022** Designing the Data Science Classroom](https://github.com/rstudio-conf-2022/teach-ds) | [website](https://rstudio-conf-2022.github.io/teach-ds/)
- [**Hadley Wickham** Advanced R](https://github.com/hadley/adv-r) | [website](https://adv-r.hadley.nz/index.html)
- [**Nathaniel D. Philips** YaRrr! The Pirate’s Guide to R](https://github.com/ndphillips/ThePiratesGuideToR) | [website](https://bookdown.org/ndphillips/YaRrr/)
- [**Unversity of Manchester** Data analysis using R](https://github.com/UoMResearchIT/r-tidyverse-intro) | [website](https://uomresearchit.github.io/r-tidyverse-intro/)
- [**Hadley Wickham and Garett Grolemund** R for data science](https://github.com/hadley/r4ds) | [website](https://r4ds.had.co.nz/)
- [**Oscar Baruffa** Big book of R](https://github.com/oscarbaruffa/BigBookofR) | [website](https://www.bigbookofr.com/)
- [**Norm Matloff** fasteR](https://github.com/matloff/fasteR)
- [**Sean Davis** Intro to R](https://github.com/seandavi/ITR) | [website](https://seandavi.github.io/ITR)
- [**Colin Gillespie and Robin Lovelace** Efficient R programming](https://github.com/csgillespie/efficientR) | [website](https://csgillespie.github.io/efficientR/)
- [**Chenxin Li** Online R learning](https://github.com/cxli233/Online_R_learning)
- [**bioinformatics.ca** Analysis using R 2021](https://github.com/bioinformatics-ca/AUR_2021) | [website](https://bioinformaticsdotca.github.io/AUR_2021)
- [**bioinformatics.ca** Introduction to R 2021](https://github.com/bioinformatics-ca/INR_2021) | [website](https://bioinformaticsdotca.github.io/INR_2021)
- [**Carpentries** The bioconductor project](https://github.com/carpentries-incubator/bioc-project) | [website](https://carpentries-incubator.github.io/bioc-project/)
- [**Rstudio eduction** Data science box](https://github.com/rstudio-education/datascience-box) | [website](https://datasciencebox.org/)
- [**University of California, Irvine** Introduction to Data Science](https://github.com/ics80-fa21/website) | [website](https://www.introdata.science/)
- [**University of Edinburgh** Introduction to Data Science](https://github.com/ids-s1-20/website) | [website](https://introds-2020.netlify.app/)
- [**Duke University** Introduction to Data Science](https://github.com/DukeStatSci/introds) | [website](https://introds-duke.netlify.app/)
- [**Joachim Goedhart** An introduction to data visualization protocols for wet lab scientists](https://github.com/JoachimGoedhart/DataViz-protocols) | [website](https://joachimgoedhart.github.io/DataViz-protocols/)
- [**Ted Laderas** R Bootcamp](https://github.com/laderast/RBootcamp) | [website](http://r-bootcamp.netlify.app/)
- [**Ted Laderas** A gRadual Introduction to Shiny](https://github.com/laderast/gradual_shiny) | [website](http://laderast.github.io/gradual_shiny)
- [**Carpentries** High dimensional statistics with R](https://github.com/carpentries-incubator/high-dimensional-stats-r) | [website](https://carpentries-incubator.github.io/high-dimensional-stats-r/)
- [**Melbourne Bioinformatics** An Introduction to R for Biologists](https://github.com/melbournebioinformatics/r-intro-biologists) | [website](https://melbournebioinformatics.github.io/r-intro-biologists/)
- [**Colautti Lab** R Crash Course](https://github.com/ColauttiLab/RCrashCourse_Book) | [website](https://colauttilab.github.io/RCrashCourse)
- [**Bruno Rodrigues** Reproducible Analytical Pipelines - Master's of Data Science](https://github.com/b-rodrigues/rap4mads) | [website](https://rap4mads.eu/)
- [**Openscapes** Making shareable documents with Quarto](https://github.com/Openscapes/quarto-website-tutorial) | [website](https://openscapes.github.io/quarto-website-tutorial/)
- [**UCSB-MEDS** Creating quarto websites](https://github.com/UCSB-MEDS/creating-quarto-websites) | [websites](https://ucsb-meds.github.io/creating-quarto-websites/)
- [**UCSB-MEDS** Customizing quarto websites](https://github.com/UCSB-MEDS/customizing-quarto-websites) | [websites](https://ucsb-meds.github.io/creating-quarto-websites/)

### git

- [**Carpentries** Version Control with Git](https://github.com/swcarpentry/git-novice) | [website](https://swcarpentry.github.io/git-novice/)
- [**Jennifer (Jenny) Bryan** Happy git with r](https://github.com/jennybc/happy-git-with-r) | [website](https://happygitwithr.com/)

## Sequence data analysis

### General

- [**SIB** NGS: Quality control, Alignment, Visualisation](https://github.com/sib-swiss/NGS-introduction-training) | [website](https://sib-swiss.github.io/NGS-introduction-training/)
- [**Harvard Chan Bioinformatics Core** Accessing genomic reference and experimental sequencing data](https://github.com/hbctraining/Accessing_public_genomic_data) | [website](https://hbctraining.github.io/Accessing_public_genomic_data/)
- [**CRUK** Workshop on Functional Genomics - summer school 2020](https://github.com/bioinformatics-core-shared-training/cruk-summer-school-2020) | [website](https://bioinformatics-core-shared-training.github.io/cruk-summer-school-2020/)
- [**Carpentries** Data Wrangling and Processing for Genomics](https://github.com/datacarpentry/wrangling-genomics) | [website](https://datacarpentry.org/wrangling-genomics/)
- [**Mike Love** Introduction to Computational Biology](https://github.com/biodatascience/compbio) | [website](https://biodatascience.github.io/compbio/)
- [**bioinformatics.ca** High Throughput Genomics Analysis](https://github.com/bioinformatics-ca/HTG_2021) | [website](https://bioinformaticsdotca.github.io/HTG_2021)
- [**St. Jude Children's Research Hospital** Learn Genomics](https://github.com/stjude/learngenomics.dev)| [website](https://learngenomics.dev/)
- [**Melbourne Bioinformatics** Bioinformatics Documentation](https://github.com/melbournebioinformatics/MelBioInf_docs) | [website](http://melbournebioinformatics.github.io/MelBioInf_docs/)
- [**Griffiths lab** pmbio.org](https://github.com/griffithlab/pmbio.org) | [website](https://pmbio.org/)
- [**Mike Lee** Happy Belly Bioinformatics](https://github.com/AstrobioMike/AstrobioMike.github.io) | [website](https://astrobiomike.github.io/)

### Miscellaneous

- [**James W. MacDonald** Introduction to Bioconductor annotation resources](https://github.com/jmacdon/Bioc2020Anno) | [website](https://jmacdon.github.io/Bioc2020Anno/)
- [**Waldron lab CUNY** Public data resources and Bioconductor](https://github.com/jmacdon/Bioc2020Anno) | [website](https://waldronlab.io/PublicDataResources/)
- [**Waldron lab CUNY** Functional enrichment analysis of high-throughput omics data](https://github.com/waldronlab/enrichOmics) | [website](https://waldronlab.io/enrichOmics/)
- [**WEHI**  Gene-set enrichment analysis workshop](https://github.com/DavisLaboratory/GenesetAnalysisWorkflow/) | [website](https://davislaboratory.github.io/GenesetAnalysisWorkflow/)
- [**Waldron lab CUNY** Multi-omic Integration of cBioPortal and TCGA data with MultiAssayExperiment](https://github.com/waldronlab/MultiAssayWorkshop/) | [website](https://waldronlab.io/MultiAssayWorkshop/)
- [**SIB** Enrichment Analysis](https://github.com/sib-swiss/enrichment-analysis-training/) | [website](https://sib-swiss.github.io/enrichment-analysis-training/)
- [**bioinformatics.ca** Cancer Analysis 2021](https://github.com/bioinformatics-ca/CAN_2021) | [website](https://bioinformaticsdotca.github.io/CAN_2021)
- [**bioinformatics.ca** Infectious Disease Epidemiology Analysis 2021](https://github.com/bioinformatics-ca/IDE_2021) | [website](https://bioinformaticsdotca.github.io/IDE_2021)
- [**bioinformatics.ca** Pathway Network Analysis 2021](https://github.com/bioinformatics-ca/PNA_2021) | [website](https://bioinformaticsdotca.github.io/PNA_2021)
- [**The Haibe-Kains Laboratory @ Princess Margaret Cancer Centre** Biomarker discovery from high throughput screening datasets](https://github.com/bhklab/bioc2020workshop) | [website](https://bhklab.ca/bioc2020workshop/)
- [**James W. MacDonald** Introduction to Bioconductor annotation resources](https://github.com/jmacdon/Bioc2022Anno) | [website](https://jmacdon.github.io/Bioc2022Anno)
- [**Chloe Mirzayi** Epidemiology for Bioinformaticians](https://github.com/cmirzayi/EpiForBioWorkshop2020/) | [website](https://chloemirzayi.com/EpiForBioWorkshop2020/)


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
- [**CRG** RNAseq course 2019](https://github.com/biocorecrg/RNAseq_course_2019) | [website](https://biocorecrg.github.io/RNAseq_course_2019/)
- [**Dan Beiting** DIYtranscriptomics](https://github.com/DIYtranscriptomics/DIYtranscriptomics.github.io) | [website](https://diytranscriptomics.com/)
- [**bioinformatics.ca** RNA-seq Analysis 2021](https://github.com/bioinformatics-ca/RNA_2021) | [website](https://bioinformaticsdotca.github.io/RNA_2021)

### ChIP-seq

- [**Harvard Chan Bioinformatics Core** Introduction to ChIP-seq using high performance computing](https://github.com/hbctraining/Intro-to-ChIPseq) | [website](https://hbctraining.github.io/Intro-to-ChIPseq/)
- [**CRUK CI** Quantitiative analysis of ChiP-seq, ATAC-seq, and related DNA enrichment assays](https://github.com/bioinformatics-core-shared-training/Quantitative-ChIPseq-Workshop)
- [**UMass MCCB** Best practices for ATAC-seq QC and data analysis](https://github.com/haibol2016/ATACseqQCWorkshop/) | [website](https://haibol2016.github.io/ATACseqQCWorkshop/)
- [**UMass** Integrated ChIP-seq Data Analysis Workshop](https://github.com/hukai916/IntegratedChIPseqWorkshop/) | [website](https://hukai916.github.io/IntegratedChIPseqWorkshop/)
- [**bioinformatics.ca** Epigenomic Analysis 2021](https://github.com/bioinformatics-ca/EPI_2021) | [website](https://bioinformaticsdotca.github.io/EPI_2021)

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
- [**Wellcome Sanger Institute** Analysis of single cell RNA-seq data](https://github.com/hemberg-lab/scRNA.seq.course) | [website](https://www.singlecellcourse.org/)
- [**Aedin Culhane** basic scRNAseq workflow](https://github.com/aedin/scRNAseqBasicWorkflow) | [website](https://aedin.github.io/scRNAseqBasicWorkflow/)
- [**Martin Morgan** introduction to Human Cell Atlas data retrieval and analysis in R / Bioconductor](https://github.com/mtmorgan/HCABiocTraining) | [webiste](https://mtmorgan.github.io/HCABiocTraining/)
- [**Tidy-transcriptomics workshops** Tidy Transcriptomics For Single-Cell RNA Sequencing Analyses](https://github.com/tidytranscriptomics-workshops/bioc2022_tidytranscriptomics) | [website](https://tidytranscriptomics-workshops.github.io/bioc2022_tidytranscriptomics)

### Spatial transcriptomics
- [**Davis Laboratory** Analysing GeoMx DSP dataset with standR](https://github.com/DavisLaboratory/GeoMXAnalysisWorkflow) | [website](https://davislaboratory.github.io/GeoMXAnalysisWorkflow)

### Variant analysis

- [**SIB** NGS - Genome variant analysis](https://github.com/sib-swiss/NGS-variants-training/) | [website](https://sib-swiss.github.io/NGS-variants-training/)
- [**bioinformaticsworkbook.org** Variant Discovery](https://github.com/ISUgenomics/bioinformatics-workbook) | [website](https://bioinformaticsworkbook.org/dataAnalysis/VariantCalling/variant-calling-index.html#gsc.tab=0)
- [**WEHI** A introduction to SNV analyses in whole genome sequencing](https://github.com/PapenfussLab/IntroductionToGenomicsWorkshop/) | [website](https://papenfusslab.github.io/IntroductionToGenomicsWorkshop/)
- [**Waldron lab CUNY** Copy number variation analysis with Bioconductor](https://github.com/waldronlab/CNVWorkshop) | [website](https://waldronlab.io/CNVWorkshop/)
- [**Sateesh Peri** Nextflow Tutorial - Variant Calling Edition](https://github.com/sateeshperi/nextflow_varcal) | [website](https://sateeshperi.github.io/nextflow_varcal/nextflow/)

### Genome assembly & annotation

- [**bioinformaticsworkbook.org** Introduction to Genome Assembly](https://github.com/ISUgenomics/bioinformatics-workbook) | [website](https://bioinformaticsworkbook.org/dataAnalysis/GenomeAssembly/Intro_GenomeAssembly.html#gsc.tab=0)
- [**Katharina Hoff** BRAKER-TSEBRA-Workshop](https://github.com/KatharinaHoff/BRAKER-TSEBRA-Workshop)

### Metagenomics/microbial

- [**Waldron lab CUNY**  Curated Metagenomic Analyses](https://github.com/waldronlab/curatedMetagenomicDataAnalyses) | [website](https://waldronlab.io/curatedMetagenomicDataAnalyses/)
- [**bioinformatics.ca** Microbiome Analysis 2021](https://github.com/bioinformatics-ca/MIC_2021) | [website](https://bioinformaticsdotca.github.io/MIC_2021)
- [**Matteo Calgaro** An introduction to benchdamic](https://github.com/mcalgaro93/benchdamicWorkshop) | [website](https://mcalgaro93.github.io/benchdamicWorkshop/)

## Computational methods and pipelines

### Containers

- [**SIB** Docker and Singularity for reproducible research: getting started with containers](https://github.com/sib-swiss/containers-introduction-training) | [website](https://sib-swiss.github.io/containers-introduction-training/latest/)
- [**Carpentries** Reproducible Computational Environments Using Containers: Introduction to Docker](https://github.com/carpentries-incubator/docker-introduction) | [website](https://carpentries-incubator.github.io/docker-introduction/)
- [**Carpentries** Reproducible computational environments using containers: Introduction to Singularity](https://github.com/carpentries-incubator/singularity-introduction) | [website](https://carpentries-incubator.github.io/singularity-introduction/)
- [**rOpenSci Labs** R Docker tutorial](https://github.com/jsta/r-docker-tutorial) | [website](https://jsta.github.io/r-docker-tutorial/)
- [**Bioconductor** Docker containers for Bioconductor](https://github.com/Bioconductor/bioconductor_docker) | [website](https://bioconductor.org/help/docker/)
- [**Awesome workshop** Docker/Singularity HATS@LPC](https://github.com/awesome-workshop/docker-singularity-hats) | [website](https://awesome-workshop.github.io/docker-singularity-hats/index.html)

### Nextflow

- [**CRG SIB** Reproducible research and data analysis using Nextflow pipelines](https://github.com/biocorecrg/SIB_course_nextflow_Nov_2021) | [website](https://biocorecrg.github.io/SIB_course_nextflow_Nov_2021/docs/)
- [**Carpentries** Introduction to Bioinformatics workflows with Nextflow and nf-core](https://github.com/carpentries-incubator/workflows-nextflow) | [website](https://carpentries-incubator.github.io/workflows-nextflow/)
- [**CRG BovReg** Nextflow training](https://github.com/bovreg/nf-workshop20) | [website](https://bovreg.github.io/nf-workshop20/)
- [**CRG** Reproducible research and data analysis with Linux containers and Nextflow pipelines](https://github.com/biocorecrg/CoursesCRG_Containers_Nextflow_May_2022) | [website](https://biocorecrg.github.io/CoursesCRG_Containers_Nextflow_May_2022/)
- [**CRUK CI** nextflow_september_2021](https://github.com/bioinformatics-core-shared-training/nextflow_september_2021)
- [**Sateesh Peri** Nextflow Tutorial - Variant Calling Edition](https://github.com/sateeshperi/nextflow_varcal) | [website](https://sateeshperi.github.io/nextflow_varcal/nextflow/)
- [**CRG ELIXIR** Containers and Workflow Pipelines for reproducible and automated data analysis](https://github.com/biocorecrg/ELIXIR_containers_nextflow) | [website](https://biocorecrg.github.io/ELIXIR_containers_nextflow/)
- [**Seqera labs** Nextflow training](https://github.com/seqeralabs/nf-training-public) | [website](https://training.seqera.io/)
- [**VIB ELIXIR** Nextflow Pipelines for reproducible and automated data analysis](https://github.com/vibbits/nextflow-workshop) | [website](https://vibbits-nextflow-workshop.readthedocs.io/en/latest/)

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
- [**Richard McElreath** Statistical Rethinking (2022 Edition)](https://github.com/rmcelreath/stat_rethinking_2022)
- [**SIB** Advanced statistics: Statistical modelling](https://github.com/sib-swiss/advanced-statistics) | [website](https://sib-swiss.github.io/advanced-statistics/)
- [**SIB** Learning statistics with R](https://github.com/sib-swiss/Introduction-to-statistics-with-R) | [website](https://sib-swiss.github.io/Introduction-to-statistics-with-R/)
- [**SIB** Introduction to Bayesian statistics with R](https://github.com/sib-swiss/intro-bayesian-statistics-training)
- [**SIB** Introduction to Statistics for Life Science - with python](https://github.com/sib-swiss/introduction-to-statistics-with-python-training)
- [**Carpentries** Statistical thinking for public health](https://github.com/carpentries-incubator/statistical-thinking-public-health) | [website](https://carpentries-incubator.github.io/statistical-thinking-public-health/)

### Machine learning

- [**SIB** Introduction to Machine Learning (Python)](https://github.com/sib-swiss/intro-machine-learning-training)
- [**Carpentries** Introduction to Machine Learning with Scikit Learn](https://github.com/carpentries-incubator/machine-learning-novice-sklearn) | [website](https://carpentries-incubator.github.io/machine-learning-novice-sklearn/)
- [**Carpentries** Introduction to Machine Learning in Python](https://github.com/carpentries-incubator/machine-learning-novice-python) | [website](https://carpentries-incubator.github.io/machine-learning-novice-python/)
- [**fastai** Practical Deep Learning for Coders](https://github.com/fastai/course20) | [website](https://course.fast.ai/)
- [**bioinformatics.ca** Machine Learning 2021](https://github.com/bioinformatics-ca/MLE_2021) | [website](https://bioinformaticsdotca.github.io/MLE_2021)
- [**Phillip Lippe** UvA Deep Learning Tutorials](https://github.com/phlippe/uvadlc_notebooks) | [website](https://uvadlc-notebooks.readthedocs.io/en/latest/)
- [**INRIA** Machine learning in Python with scikit-learn MOOC](https://github.com/INRIA/scikit-learn-mooc) | [website](https://inria.github.io/scikit-learn-mooc/)

## Reproducibility and data management

### FAIR & Reproducibility

- [**Harvard Chan Bioinformatics Core** Tools for Reproducible Research](https://github.com/hbctraining/reproducibility-tools) | [website](https://hbctraining.github.io/reproducibility-tools/)
- [**Carpentries** FAIR in (biological) practice](https://github.com/carpentries-incubator/fair-bio-practice) | [website](https://carpentries-incubator.github.io/fair-bio-practice/)
- [**Carpentries** Introduction to Conda for (Data) Scientists](https://github.com/carpentries-incubator/introduction-to-conda-for-data-scientists) | [website](https://carpentries-incubator.github.io/introduction-to-conda-for-data-scientists/)
- [**FAIRplus** FAIR Cookbook](https://github.com/FAIRplus/the-fair-cookbook) | [website](https://fairplus.github.io/the-fair-cookbook/content/home.html)
- [**Carpentries** Fair for leaders](https://github.com/carpentries-incubator/fair-for-leaders) | [website](https://carpentries-incubator.github.io/fair-for-leaders/)
- [**SIB** Personalized Health informatics Group FAIR principles in practice for health data](https://git.dcc.sib.swiss/sphn-semantic-framework/fair-principles-in-practice-for-health-data/-/tree/main#fair-principles-in-practice-for-health-data) | [website](https://sphn.ch/training/fair-principles-in-practice-for-health-data/)

### Data management

- [**Carpentries** From a Spreadsheet to a Database](https://github.com/carpentries-incubator/capstone-novice-spreadsheet-biblio) | [website](https://carpentries-incubator.github.io/capstone-novice-spreadsheet-biblio/)
- [**CRUK CI** Managing your Research Data: Best practices in Research Data Management for Biological Sciences](https://github.com/bioinformatics-core-shared-training/Managing-your-research-data) | [website](https://bioinformatics-core-shared-training.github.io/Managing-your-research-data/)
- [**ELIXIR Europe** RDMkit](https://github.com/elixir-europe/rdmkit) | [website](https://rdmkit.elixir-europe.org)
- [**ELIXIR Belgium** RDM guide](https://github.com/ELIXIR-Belgium/rdm-guide) | [website](https://rdm.elixir-belgium.org/)
- [**ELIXIR Norway** 2022-09-26 DMP-writing-workshop](https://github.com/korbinib/DMP-writing-workshop) | [website](https://elixir.no/)
- [**ELIXIR Norway** FAIR Data Management in Life Sciences - June 2022 Course](https://github.com/elixir-oslo/fair-dm-lifesci-june-2022)
- [**SIB** Query SIB resources with SPARQL](https://github.com/sib-swiss/sparql-training)
- [**SIB Personalized Health Informatics Group** SPHN Training material](https://git.dcc.sib.swiss/sphn-semantic-framework/sphn-training-material/) | [website](https://sphn.ch/training/)

## Image analysis

- [**University of Michigan** Andy's brain book](https://github.com/andrewjahn/AndysBrainBook) | [website](https://andysbrainbook.readthedocs.io/en/latest/)

## Other lists

- [**Amanda Miotto** HackyHourBookmarks](https://github.com/amandamiotto/HackyHourBookmarks) | [website](https://amandamiotto.github.io/HackyHourBookmarks/)
- [**CRG**](https://github.com/biocorecrg/) | [website](https://biocorecrg.github.io/courses)
- [**Bradley Boehmke** Data science learning resources](https://github.com/bradleyboehmke/data-science-learning-resources)
- [**Ming Tang** Getting started with genomics tools and recources](https://github.com/crazyhottommy/getting-started-with-genomics-tools-and-resources)

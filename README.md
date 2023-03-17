[![DOI](https://zenodo.org/badge/437832906.svg)](https://zenodo.org/badge/latestdoi/437832906)

# Bioinformatics training materials

Do you like this collection? You're going to love [glittr.org](https://glittr.org)! The collection below is still maintained but updated by glittr.org. So, if you have anything to add or to ask, see you there!

[![](assets/logo-vertical.svg)](https://glittr.org)

I you haven't stopped reading, you're one of the few that still prefer the old school `README` :neckbeard:. Nice !

Below you'll find a curated list of **bioinformatics training material**. All material is:

- In a GitHub or GitLab repository
- Free to use
- Written in markdown or similar

**NOTE:** This list of courses is selected *only* based on the above criteria. There are *no* checks on quality.

## Contents

- [Scripting and languages](#scripting-and-languages)
  - [Data visualization](#data-visualization)
  - [Python](#python)
  - [Quarto](#quarto)
  - [R](#r)
  - [Unix/Linux](#unix/linux)
  - [Version control](#version-control)
  - [Julia](#julia)
- [Computational methods and pipelines](#computational-methods-and-pipelines)
  - [Containerization](#containerization)
  - [High performance computing](#high-performance-computing)
  - [Workflows](#workflows)
  - [Image analysis](#image-analysis)
- [Omics analysis](#omics-analysis)
  - [Epidemiology](#epidemiology)
  - [ChIP-seq](#chip-seq)
  - [Epigenetics](#epigenetics)
  - [Genome annotation](#genome-annotation)
  - [Genomics](#genomics)
  - [Metagenomics](#metagenomics)
  - [Multiomics](#multiomics)
  - [Next generation sequencing](#next-generation-sequencing)
  - [Single-cell sequencing](#single-cell-sequencing)
  - [Spatial transcriptomics](#spatial-transcriptomics)
  - [Transcriptomics](#transcriptomics)
- [Reproducibility and data management](#reproducibility-and-data-management)
  - [Data management](#data-management)
  - [FAIR data](#fair-data)
  - [Reproducibility](#reproducibility)
- [Statistics and machine learning](#statistics-and-machine-learning)
  - [Data science](#data-science)
  - [Machine learning](#machine-learning)
  - [Statistics](#statistics)
- [Others](#others)
  - [General](#general)

## Scripting and languages


### Data visualization

- [**Bioinformatics, Rockefeller University** RockefellerUniversity/IGV_course](https://github.com/RockefellerUniversity/IGV_course) | [website](https://rockefelleruniversity.github.io/IGV_course/)
- [**Hadley Wickham** hadley/ggplot2-book](https://github.com/hadley/ggplot2-book) | [website](https://ggplot2-book.org)

### Python

- [**carpentries-incubator** carpentries-incubator/introduction-to-conda-for-data-scientists](https://github.com/carpentries-incubator/introduction-to-conda-for-data-scientists) | [website](https://carpentries-incubator.github.io/introduction-to-conda-for-data-scientists/)
- [**carpentries-incubator** carpentries-incubator/python-interactive-data-visualizations](https://github.com/carpentries-incubator/python-interactive-data-visualizations) | [website](https://carpentries-incubator.github.io/python-interactive-data-visualizations/)
- [**Jake Vanderplas** jakevdp/PythonDataScienceHandbook](https://github.com/jakevdp/PythonDataScienceHandbook) | [website](http://jakevdp.github.io/PythonDataScienceHandbook)
- [**Jake Vanderplas** jakevdp/WhirlwindTourOfPython](https://github.com/jakevdp/WhirlwindTourOfPython)
- [**Plants&Python** PlantsAndPython/PlantsAndPython](https://github.com/PlantsAndPython/PlantsAndPython)
- [**SIB Swiss Institute of Bioinformatics** sib-swiss/first-steps-with-python-training](https://github.com/sib-swiss/first-steps-with-python-training)
- [**SIB Swiss Institute of Bioinformatics** sib-swiss/intermediate-python-training](https://github.com/sib-swiss/intermediate-python-training)
- [**Software Carpentry** swcarpentry/python-novice-inflammation](https://github.com/swcarpentry/python-novice-inflammation) | [website](http://swcarpentry.github.io/python-novice-inflammation/)
- [**VIB Technologies: Bioinformatics and software projects** vibbits/gentle-hands-on-python](https://github.com/vibbits/gentle-hands-on-python)

### Quarto

- [**UCSB-MEDS** UCSB-MEDS/customizing-quarto-websites](https://github.com/UCSB-MEDS/customizing-quarto-websites) | [website](https://ucsb-meds.github.io/customizing-quarto-websites/)

### R

- [**Bruno Rodrigues** b-rodrigues/rap4mads](https://github.com/b-rodrigues/rap4mads) | [website](https://b-rodrigues.github.io/rap4mads/)
- [**BHKLAB** bhklab/bioc2020workshop](https://github.com/bhklab/bioc2020workshop) | [website](http://bhklab.ca/bioc2020workshop/articles/GxWorkshop.html)
- [**Bioconductor** Bioconductor/bioconductor_docker](https://github.com/Bioconductor/bioconductor_docker) | [website](https://bioconductor.org/help/docker/)
- [**Biocore@CRG** biocorecrg/CRG_R_tidyverse_2021](https://github.com/biocorecrg/CRG_R_tidyverse_2021)
- [**Biocore@CRG** biocorecrg/CRG_RIntroduction_2021](https://github.com/biocorecrg/CRG_RIntroduction_2021)
- [**Canadian Bioinformatics Workshops** bioinformatics-ca/AUR_2021](https://github.com/bioinformatics-ca/AUR_2021)
- [**Canadian Bioinformatics Workshops** bioinformatics-ca/INR_2021](https://github.com/bioinformatics-ca/INR_2021)
- [**CRUK CI Bioinformatics Core** bioinformatics-core-shared-training/linear-models-r](https://github.com/bioinformatics-core-shared-training/linear-models-r) | [website](https://bioinformatics-core-shared-training.github.io/linear-models-r/)
- [**Bradley Boehmke** bradleyboehmke/Intro-to-R-Bootcamp](https://github.com/bradleyboehmke/Intro-to-R-Bootcamp)
- [**carpentries-incubator** carpentries-incubator/bioc-project](https://github.com/carpentries-incubator/bioc-project) | [website](https://carpentries-incubator.github.io/bioc-project)
- [**carpentries-incubator** carpentries-incubator/high-dimensional-stats-r](https://github.com/carpentries-incubator/high-dimensional-stats-r) | [website](https://carpentries-incubator.github.io/high-dimensional-stats-r)
- [**Colautti Lab** ColauttiLab/RCrashCourse_Book](https://github.com/ColauttiLab/RCrashCourse_Book)
- [**Computational Cancer Epigenomics @ DKFZ** CompEpigen/BasicR](https://github.com/CompEpigen/BasicR) | [website](https://compepigen.github.io/BasicR/)
- [**Colin Gillespie** csgillespie/efficientR](https://github.com/csgillespie/efficientR) | [website](https://csgillespie.github.io/efficientR/)
- [**C. Li** cxli233/Online_R_learning](https://github.com/cxli233/Online_R_learning)
- [**Davis Laboratory** DavisLaboratory/GenesetAnalysisWorkflow](https://github.com/DavisLaboratory/GenesetAnalysisWorkflow) | [website](https://davislaboratory.github.io/GenesetAnalysisWorkflow/)
- [**David Robinson** dgrtwo/tidy-text-mining](https://github.com/dgrtwo/tidy-text-mining) | [website](http://tidytextmining.com)
- [**Danielle Navarro** djnavarro/rbook](https://github.com/djnavarro/rbook) | [website](https://learningstatisticswithr.com)
- [**DukeStatSci** DukeStatSci/introds](https://github.com/DukeStatSci/introds) | [website](https://introds-duke.netlify.app)
- [**Hadley Wickham** hadley/adv-r](https://github.com/hadley/adv-r) | [website](http://adv-r.hadley.nz)
- [**Hadley Wickham** hadley/r4ds](https://github.com/hadley/r4ds) | [website](http://r4ds.hadley.nz)
- [**Teaching materials at the Harvard Chan Bioinformatics Core** hbctraining/Intro-to-R-flipped](https://github.com/hbctraining/Intro-to-R-flipped) | [website](https://hbctraining.github.io/Intro-to-R-flipped/)
- [**ICS 80 - Introduction to Data Science** ics80-fa21/website](https://github.com/ics80-fa21/website) | [website](https://introdata.science)
- [**Introduction to Data Science - 2020 - Semester 1** ids-s1-20/website](https://github.com/ids-s1-20/website) | [website](https://introds.org)
- [**Jennifer (Jenny) Bryan** jennybc/purrr-tutorial](https://github.com/jennybc/purrr-tutorial) | [website](https://jennybc.github.io/purrr-tutorial/)
- [**James W. MacDonald** jmacdon/Bioc2020Anno](https://github.com/jmacdon/Bioc2020Anno)
- [**James W. MacDonald** jmacdon/Bioc2022Anno](https://github.com/jmacdon/Bioc2022Anno)
- [**Joachim Goedhart** JoachimGoedhart/DataViz-protocols](https://github.com/JoachimGoedhart/DataViz-protocols) | [website](https://joachimgoedhart.github.io/DataViz-protocols/)
- [**Jemma Stachelek** jsta/r-docker-tutorial](https://github.com/jsta/r-docker-tutorial) | [website](http://jsta.github.io/r-docker-tutorial)
- [**Tom Mock** jthomasmock/rmd-nhs](https://github.com/jthomasmock/rmd-nhs) | [website](https://jthomasmock.github.io/rmd-nhs/)
- [**Ted Laderas** laderast/gradual_shiny](https://github.com/laderast/gradual_shiny) | [website](http://laderast.github.io/gradual_shiny)
- [**Ted Laderas** laderast/RBootcamp](https://github.com/laderast/RBootcamp) | [website](http://r-bootcamp.netlify.app)
- [**Qian Liu** Liubuntu/Bioc2020RCWL](https://github.com/liubuntu/Bioc2020Rcwl)
- [**Norm Matloff** matloff/fasteR](https://github.com/matloff/fasteR)
- [**Melbourne Bioinformatics** melbournebioinformatics/r-intro-biologists](https://github.com/melbournebioinformatics/r-intro-biologists)
- [**ModernDive** moderndive/ModernDive_book](https://github.com/moderndive/ModernDive_book) | [website](https://www.moderndive.com)
- [**Nathaniel Phillips** ndphillips/ThePiratesGuideToR](https://github.com/ndphillips/ThePiratesGuideToR) | [website](https://bookdown.org/ndphillips/YaRrr/)
- [**Openscapes** Openscapes/quarto-website-tutorial](https://github.com/Openscapes/quarto-website-tutorial) | [website](https://openscapes.github.io/quarto-website-tutorial)
- [**Oscar Baruffa** oscarbaruffa/BigBookofR](https://github.com/oscarbaruffa/BigBookofR) | [website](https://www.bigbookofr.com)
- [**Rafael A Irizarry** rafalab/dsbook](https://github.com/rafalab/dsbook)
- [**rstudio::conf(2022)** rstudio-conf-2022/art-from-code](https://github.com/rstudio-conf-2022/art-from-code) | [website](https://art-from-code.netlify.app)
- [**rstudio::conf(2022)** rstudio-conf-2022/build-tidy-tools](https://github.com/rstudio-conf-2022/build-tidy-tools) | [website](https://rstd.io/btt)
- [**rstudio::conf(2022)** rstudio-conf-2022/get-started-quarto](https://github.com/rstudio-conf-2022/get-started-quarto) | [website](https://rstudio-conf-2022.github.io/get-started-quarto/)
- [**rstudio::conf(2022)** rstudio-conf-2022/get-started-shiny](https://github.com/rstudio-conf-2022/get-started-shiny) | [website](https://rstd.io/start-shiny)
- [**rstudio::conf(2022)** rstudio-conf-2022/ggplot2-graphic-design](https://github.com/rstudio-conf-2022/ggplot2-graphic-design) | [website](https://rstudio-conf-2022.github.io/ggplot2-graphic-design/)
- [**rstudio::conf(2022)** rstudio-conf-2022/intro-to-tidyverse](https://github.com/rstudio-conf-2022/intro-to-tidyverse) | [website](https://conf22-intro-tidyverse.netlify.app)
- [**rstudio::conf(2022)** rstudio-conf-2022/shiny-prod-apps](https://github.com/rstudio-conf-2022/shiny-prod-apps) | [website](https://shinyprod.com)
- [**rstudio::conf(2022)** rstudio-conf-2022/teach-ds](https://github.com/rstudio-conf-2022/teach-ds) | [website](https://rstd.io/teach-ds-conf22)
- [**rstudio::conf(2022)** rstudio-conf-2022/wtf-rstats](https://github.com/rstudio-conf-2022/wtf-rstats)
- [**RStudio Education** rstudio-education/datascience-box](https://github.com/rstudio-education/datascience-box) | [website](https://datasciencebox.org)
- [**RStudio** rstudio/rmarkdown-book](https://github.com/rstudio/rmarkdown-book) | [website](https://bookdown.org/yihui/rmarkdown)
- [**Saskia** SaskiaFreytag/biocommons-r-intro](https://github.com/SaskiaFreytag/biocommons-r-intro) | [website](https://saskiafreytag.github.io/biocommons-r-intro/)
- [**Sean Davis** seandavi/ITR](https://github.com/seandavi/ITR) | [website](https://seandavi.github.io/ITR)
- [**SIB Swiss Institute of Bioinformatics** sib-swiss/enrichment-analysis-training](https://github.com/sib-swiss/enrichment-analysis-training)
- [**SIB Swiss Institute of Bioinformatics** sib-swiss/first-steps-with-R-training](https://github.com/sib-swiss/first-steps-with-R-training)
- [**Software Carpentry** swcarpentry/r-novice-gapminder](https://github.com/swcarpentry/r-novice-gapminder) | [website](http://swcarpentry.github.io/r-novice-gapminder/)
- [**Research IT, University of Manchester, UK** UoMResearchIT/r-tidyverse-intro](https://github.com/UoMResearchIT/r-tidyverse-intro) | [website](https://UoMResearchIT.github.io/r-tidyverse-intro)
- [**Waldron Lab at the CUNY SPH** waldronlab/enrichOmics](https://github.com/waldronlab/enrichOmics)
- [**Jennifer (Jenny) Bryan** jennybc/happy-git-with-r](https://github.com/jennybc/happy-git-with-r) | [website](https://happygitwithr.com)
- [**Bioinformatics, Rockefeller University** RockefellerUniversity/Bioconductor_Introduction](https://github.com/RockefellerUniversity/Bioconductor_Introduction) | [website](https://rockefelleruniversity.github.io/Bioconductor_Introduction/)
- [**Bioinformatics, Rockefeller University** RockefellerUniversity/Intro_To_R_1Day](https://github.com/RockefellerUniversity/Intro_To_R_1Day) | [website](https://rockefelleruniversity.github.io/Intro_To_R_1Day/)
- [**Bioinformatics, Rockefeller University** RockefellerUniversity/RU_reproducibleR](https://github.com/RockefellerUniversity/RU_reproducibleR) | [website](https://rockefelleruniversity.github.io/RU_reproducibleR/)
- [**Bioinformatics, Rockefeller University** RockefellerUniversity/RU_tidyverse_core](https://github.com/RockefellerUniversity/RU_tidyverse_core) | [website](https://rockefelleruniversity.github.io/RU_tidyverse_core/)
- [**Bioinformatics, Rockefeller University** RockefellerUniversity/RU_GenomicVariants](https://github.com/RockefellerUniversity/RU_GenomicVariants)
- [**Hadley Wickham** hadley/r-pkgs](https://github.com/hadley/r-pkgs) | [website](https://r-pkgs.org)
- [**Hadley Wickham** hadley/mastering-shiny](https://github.com/hadley/mastering-shiny) | [website](https://mastering-shiny.org)
- [**Dirk Eddelbuettel** eddelbuettel/gsir-te](https://github.com/eddelbuettel/gsir-te)

### Unix/Linux

- [**Data Carpentry** datacarpentry/shell-genomics](https://github.com/datacarpentry/shell-genomics) | [website](https://datacarpentry.org/shell-genomics)
- [**Teaching materials at the Harvard Chan Bioinformatics Core** hbctraining/Intro-to-shell-flipped](https://github.com/hbctraining/Intro-to-shell-flipped) | [website](https://hbctraining.github.io/Intro-to-shell-flipped/)
- [**Ted Laderas** laderast/bash_for_bioinformatics](https://github.com/laderast/bash_for_bioinformatics) | [website](https://laderast.github.io/bash_for_bioinformatics/)
- [**SIB Swiss Institute of Bioinformatics** sib-swiss/unix-first-steps-training](https://github.com/sib-swiss/unix-first-steps-training)
- [**Software Carpentry** swcarpentry/shell-novice](https://github.com/swcarpentry/shell-novice) | [website](http://swcarpentry.github.io/shell-novice/)

### Version control

- [**Software Carpentry** swcarpentry/git-novice](https://github.com/swcarpentry/git-novice) | [website](http://swcarpentry.github.io/git-novice/)

### Julia

- [**Antonello Lobianco** sylvaticus/juliatutorial](https://github.com/sylvaticus/juliatutorial)

## Computational methods and pipelines


### Containerization

- [**awesome-workshop** awesome-workshop/docker-singularity-hats](https://github.com/awesome-workshop/docker-singularity-hats) | [website](https://awesome-workshop.github.io/docker-singularity-hats/index.html)
- [**carpentries-incubator** carpentries-incubator/docker-introduction](https://github.com/carpentries-incubator/docker-introduction) | [website](https://carpentries-incubator.github.io/docker-introduction/)
- [**carpentries-incubator** carpentries-incubator/singularity-introduction](https://github.com/carpentries-incubator/singularity-introduction) | [website](https://carpentries-incubator.github.io/singularity-introduction)
- [**SIB Swiss Institute of Bioinformatics** sib-swiss/containers-introduction-training](https://github.com/sib-swiss/containers-introduction-training) | [website](https://sib-swiss.github.io/containers-introduction-training/)

### High performance computing

- [**carpentries-incubator** carpentries-incubator/hpc-intro](https://github.com/carpentries-incubator/hpc-intro) | [website](https://carpentries-incubator.github.io/hpc-intro/)
- [**ngs-docs** ngs-docs/2021-august-remote-computing](https://github.com/ngs-docs/2021-august-remote-computing) | [website](https://ngs-docs.github.io/2021-august-remote-computing)

### Workflows

- [**Biocore@CRG** biocorecrg/CoursesCRG_Containers_Nextflow_May_2022](https://github.com/biocorecrg/CoursesCRG_Containers_Nextflow_May_2022) | [website](https://biocorecrg.github.io/CoursesCRG_Containers_Nextflow_May_2022/)
- [**Biocore@CRG** biocorecrg/ELIXIR_containers_nextflow](https://github.com/biocorecrg/ELIXIR_containers_nextflow) | [website](https://biocorecrg.github.io/ELIXIR_containers_nextflow/)
- [**Biocore@CRG** biocorecrg/SIB_course_nextflow_Nov_2021](https://github.com/biocorecrg/SIB_course_nextflow_Nov_2021) | [website](https://biocorecrg.github.io/SIB_course_nextflow_Nov_2021/docs/)
- [**Biodata Analysis Group** BiodataAnalysisGroup/intro-to-cwl-docker](https://github.com/BiodataAnalysisGroup/intro-to-cwl-docker) | [website](https://biodataanalysisgroup.github.io/intro-to-cwl-docker/)
- [**CRUK CI Bioinformatics Core** bioinformatics-core-shared-training/nextflow_september_2021](https://github.com/bioinformatics-core-shared-training/nextflow_september_2021)
- [**BovReg** BovReg/nf-workshop20](https://github.com/bovreg/nf-workshop20)
- [**carpentries-incubator** carpentries-incubator/snakemake-novice-bioinformatics](https://github.com/carpentries-incubator/snakemake-novice-bioinformatics) | [website](https://carpentries-incubator.github.io/snakemake-novice-bioinformatics)
- [**carpentries-incubator** carpentries-incubator/workflows-nextflow](https://github.com/carpentries-incubator/workflows-nextflow) | [website](https://carpentries-incubator.github.io/workflows-nextflow/)
- [**carpentries-incubator** carpentries-incubator/workflows-snakemake](https://github.com/carpentries-incubator/workflows-snakemake) | [website](https://carpentries-incubator.github.io/workflows-snakemake/)
- [**Sateesh_Peri** sateeshperi/nextflow_varcal](https://github.com/sateeshperi/nextflow_varcal)
- [**Seqera Labs** nextflow-io/training](https://github.com/seqeralabs/nf-training-public) | [website](https://training.nextflow.io)
- [**Snakemake** snakemake/snakemake](https://github.com/snakemake/snakemake) | [website](https://snakemake.readthedocs.io)
- [**VIB Technologies: Bioinformatics and software projects** vibbits/nextflow-workshop](https://github.com/vibbits/nextflow-workshop)

### Image analysis

- [**Andrew Jahn** andrewjahn/AndysBrainBook](https://github.com/andrewjahn/AndysBrainBook)

## Omics analysis


### Epidemiology

- [**Canadian Bioinformatics Workshops** bioinformatics-ca/EPI_2021](https://github.com/bioinformatics-ca/EPI_2021)
- [**Canadian Bioinformatics Workshops** bioinformatics-ca/IDE_2021](https://github.com/bioinformatics-ca/IDE_2021)
- [**Chloe Mirzayi** cmirzayi/EpiForBioWorkshop2020](https://github.com/cmirzayi/EpiForBioWorkshop2020) | [website](https://cmirzayi.github.io/EpiForBioWorkshop2020/)

### ChIP-seq

- [**CRUK CI Bioinformatics Core** bioinformatics-core-shared-training/Quantitative-ChIPseq-Workshop](https://github.com/bioinformatics-core-shared-training/Quantitative-ChIPseq-Workshop)
- [**Teaching materials at the Harvard Chan Bioinformatics Core** hbctraining/Intro-to-ChIPseq](https://github.com/hbctraining/Intro-to-ChIPseq) | [website](https://hbctraining.github.io/Intro-to-ChIPseq/)
- [**hukai916** hukai916/IntegratedChIPseqWorkshop](https://github.com/hukai916/IntegratedChIPseqWorkshop)

### Epigenetics

- [**Haibo Liu** haibol2016/ATACseqQCWorkshop](https://github.com/haibol2016/ATACseqQCWorkshop)

### Genome annotation

- [**Katharina Hoff** KatharinaHoff/BRAKER-TSEBRA-Workshop](https://github.com/KatharinaHoff/BRAKER-TSEBRA-Workshop)

### Genomics

- [**Canadian Bioinformatics Workshops** bioinformatics-ca/CAN_2021](https://github.com/bioinformatics-ca/CAN_2021)
- [**Canadian Bioinformatics Workshops** bioinformatics-ca/HTG_2021](https://github.com/bioinformatics-ca/HTG_2021)
- [**Papenfuss Lab** PapenfussLab/IntroductionToGenomicsWorkshop](https://github.com/PapenfussLab/IntroductionToGenomicsWorkshop)
- [**Computational Metagenomics** metagenomics/denbi-nanopore-training](https://github.com/metagenomics/denbi-nanopore-training)

### Metagenomics

- [**Canadian Bioinformatics Workshops** bioinformatics-ca/MIC_2021](https://github.com/bioinformatics-ca/MIC_2021)
- [**Matteo Calgaro** mcalgaro93/benchdamicWorkshop](https://github.com/mcalgaro93/benchdamicWorkshop)
- [**Waldron Lab at the CUNY SPH** waldronlab/curatedMetagenomicDataAnalyses](https://github.com/waldronlab/curatedMetagenomicDataAnalyses) | [website](https://waldronlab.io/curatedMetagenomicDataAnalyses/)

### Multiomics

- [**Waldron Lab at the CUNY SPH** waldronlab/MultiAssayWorkshop](https://github.com/waldronlab/MultiAssayWorkshop) | [website](https://waldronlab.github.io/MultiAssayWorkshop)

### Next generation sequencing

- [**CRUK CI Bioinformatics Core** bioinformatics-core-shared-training/cruk-summer-school-2020](https://github.com/bioinformatics-core-shared-training/cruk-summer-school-2020) | [website](https://bioinformatics-core-shared-training.github.io/cruk-summer-school-2020/ )
- [**Data Carpentry** datacarpentry/wrangling-genomics](https://github.com/datacarpentry/wrangling-genomics) | [website](https://datacarpentry.org/wrangling-genomics/)
- [**Teaching materials at the Harvard Chan Bioinformatics Core** hbctraining/Accessing_public_genomic_data](https://github.com/hbctraining/Accessing_public_genomic_data) | [website](https://hbctraining.github.io/Accessing_public_genomic_data)
- [**SIB Swiss Institute of Bioinformatics** sib-swiss/NGS-introduction-training](https://github.com/sib-swiss/NGS-introduction-training) | [website](https://sib-swiss.github.io/NGS-introduction-training/)
- [**SIB Swiss Institute of Bioinformatics** sib-swiss/NGS-variants-training](https://github.com/sib-swiss/NGS-variants-training) | [website](https://sib-swiss.github.io/NGS-variants-training/)
- [**Waldron Lab at the CUNY SPH** waldronlab/CNVWorkshop](https://github.com/waldronlab/CNVWorkshop) | [website](https://waldronlab.io/CNVWorkshop)
- [**The Griffith Lab** griffithlab/pmbio.org](https://github.com/griffithlab/pmbio.org) | [website](http://pmbio.org)

### Single-cell sequencing

- [**Aedin Culhane** aedin/scRNAseqBasicWorkflow](https://github.com/aedin/scRNAseqBasicWorkflow)
- [**CRUK CI Bioinformatics Core** bioinformatics-core-shared-training/UnivCambridge_ScRnaSeq_Nov2021](https://github.com/bioinformatics-core-shared-training/UnivCambridge_ScRnaSeq_Nov2021) | [website](http://bioinformatics-core-shared-training.github.io/UnivCambridge_ScRnaSeq_Nov2021)
- [**fmicompbio** fmicompbio/adv_scrnaseq_2020](https://github.com/fmicompbio/adv_scrnaseq_2020)
- [**Teaching materials at the Harvard Chan Bioinformatics Core** hbctraining/scRNA-seq_online](https://github.com/hbctraining/scRNA-seq_online) | [website](https://hbctraining.github.io/scRNA-seq_online/.)
- [**Kelly Street** kstreet13/bioc2020trajectories](https://github.com/kstreet13/bioc2020trajectories) | [website](https://kstreet13.github.io/bioc2020trajectories/)
- [**Leiden Computational Biology Center** LeidenCBC/MGC-BioSB-SingleCellAnalysis2021](https://github.com/LeidenCBC/MGC-BioSB-SingleCellAnalysis2021)
- [**Martin Morgan** mtmorgan/HCABiocTraining](https://github.com/mtmorgan/HCABiocTraining) | [website](https://mtmorgan.github.io/HCABiocTraining/)
- [**NBIS - National Bioinformatics Infrastructure Sweden** NBISweden/excelerate-scRNAseq](https://github.com/NBISweden/excelerate-scRNAseq) | [website](https://nbisweden.github.io/excelerate-scRNAseq/)
- [**NBIS - National Bioinformatics Infrastructure Sweden** NBISweden/single-cell_sib_scilifelab_2021](https://github.com/NBISweden/single-cell_sib_scilifelab_2021)
- [**NBIS - National Bioinformatics Infrastructure Sweden** NBISweden/workshop-scRNAseq](https://github.com/nbisweden/workshop-scRNAseq) | [website](https://nbisweden.github.io/workshop-scRNAseq/)
- [**SIB Swiss Institute of Bioinformatics** sib-swiss/single-cell-training](https://github.com/sib-swiss/single-cell-training) | [website](https://sib-swiss.github.io/single-cell-training/)
- [**Yunshun Chen** yunshun/SingleCellWorkshop](https://github.com/yunshun/SingleCellWorkshop)

### Spatial transcriptomics

- [**Davis Laboratory** DavisLaboratory/GeoMXAnalysisWorkflow](https://github.com/DavisLaboratory/GeoMXAnalysisWorkflow) | [website](https://davislaboratory.github.io/GeoMXAnalysisWorkflow/)

### Transcriptomics

- [**Biocore@CRG** biocorecrg/RNAseq_course_2019](https://github.com/biocorecrg/RNAseq_course_2019) | [website](https://biocorecrg.github.io/RNAseq_course_2019/)
- [**Canadian Bioinformatics Workshops** bioinformatics-ca/PNA_2021](https://github.com/bioinformatics-ca/PNA_2021)
- [**Canadian Bioinformatics Workshops** bioinformatics-ca/RNA_2021](https://github.com/bioinformatics-ca/RNA_2021)
- [**CRUK CI Bioinformatics Core** bioinformatics-core-shared-training/Bulk_RNASeq_Course_Nov21](https://github.com/bioinformatics-core-shared-training/Bulk_RNASeq_Course_Nov21) | [website](https://bioinformatics-core-shared-training.github.io/Bulk_RNASeq_Course_Nov21/)
- [**carpentries-incubator** carpentries-incubator/bioc-rnaseq](https://github.com/carpentries-incubator/bioc-rnaseq) | [website](https://carpentries-incubator.github.io/bioc-rnaseq)
- [**Teaching materials at the Harvard Chan Bioinformatics Core** hbctraining/DGE_workshop_salmon_online](https://github.com/hbctraining/DGE_workshop_salmon_online) | [website](https://hbctraining.github.io/DGE_workshop_salmon_online/)
- [**Teaching materials at the Harvard Chan Bioinformatics Core** hbctraining/Intro-to-rnaseq-hpc-salmon-flipped](https://github.com/hbctraining/Intro-to-rnaseq-hpc-salmon-flipped) | [website](https://hbctraining.github.io/Intro-to-rnaseq-hpc-salmon-flipped/)
- [**SIB Swiss Institute of Bioinformatics** sib-swiss/RNAseq-introduction-training](https://github.com/sib-swiss/RNAseq-introduction-training)
- [**Stefano Mangiola** stemangiola/bioc_2020_tidytranscriptomics](https://github.com/stemangiola/bioc_2020_tidytranscriptomics) | [website](https://stemangiola.github.io/bioc_2020_tidytranscriptomics/)
- [**Tidy-transcriptomics workshops** tidytranscriptomics-workshops/bioc2022_tidytranscriptomics](https://github.com/tidytranscriptomics-workshops/bioc2022_tidytranscriptomics) | [website](https://tidytranscriptomics-workshops.github.io/bioc2022_tidytranscriptomics/index.html)
- [**Xueyi Dong** XueyiDong/RNAseq123workshop](https://github.com/XueyiDong/RNAseq123workshop)

## Reproducibility and data management


### Data management

- [**CRUK CI Bioinformatics Core** bioinformatics-core-shared-training/Managing-your-research-data](https://github.com/bioinformatics-core-shared-training/Managing-your-research-data) | [website](https://bioinformatics-core-shared-training.github.io/Managing-your-research-data/)
- [**carpentries-incubator** carpentries-incubator/capstone-novice-spreadsheet-biblio](https://github.com/carpentries-incubator/capstone-novice-spreadsheet-biblio) | [website](http://carpentries-incubator.github.io/capstone-novice-spreadsheet-biblio/)
- [**ELIXIR Belgium** ELIXIR-Belgium/rdm-guide](https://github.com/ELIXIR-Belgium/rdm-guide) | [website](https://rdm.elixir-belgium.org)
- [**ELIXIR Europe** elixir-europe/rdmkit](https://github.com/elixir-europe/rdmkit) | [website](https://rdmkit.elixir-europe.org)
- [**Korbinian Bösl** korbinib/DMP-writing-workshop](https://github.com/korbinib/DMP-writing-workshop) | [website](https://elixir.no)
- [**SIB Swiss Institute of Bioinformatics** sib-swiss/sparql-training](https://github.com/sib-swiss/sparql-training)
- [**OpenSciency** opensciency/sprint-content](https://github.com/opensciency/sprint-content)

### FAIR data

- [**carpentries-incubator** carpentries-incubator/fair-bio-practice](https://github.com/carpentries-incubator/fair-bio-practice) | [website](https://carpentries-incubator.github.io/fair-bio-practice/)
- [**carpentries-incubator** carpentries-incubator/fair-for-leaders](https://github.com/carpentries-incubator/fair-for-leaders) | [website](https://carpentries-incubator.github.io/fair-for-leaders/)
- [**elixir-oslo** ELIXIR-Norway-Training/fair-dm-lifesci-june-2022](https://github.com/elixir-oslo/fair-dm-lifesci-june-2022)
- [**FAIRplus** FAIRplus/the-fair-cookbook](https://github.com/FAIRplus/the-fair-cookbook) | [website](https://fairplus.github.io/the-fair-cookbook)

### Reproducibility

- [**Teaching materials at the Harvard Chan Bioinformatics Core** hbctraining/reproducibility-tools](https://github.com/hbctraining/reproducibility-tools) | [website](https://hbctraining.github.io/reproducibility-tools/)

## Statistics and machine learning


### Data science

- [**Stephanie Hicks** stephaniehicks/superwomen](https://github.com/stephaniehicks/superwomen) | [website](https://www.stephaniehicks.com/superwomen/)

### Machine learning

- [**Canadian Bioinformatics Workshops** bioinformatics-ca/MLE_2021](https://github.com/bioinformatics-ca/MLE_2021)
- [**carpentries-incubator** carpentries-incubator/machine-learning-novice-python](https://github.com/carpentries-incubator/machine-learning-novice-python) | [website](https://carpentries-incubator.github.io/machine-learning-novice-python/)
- [**carpentries-incubator** carpentries-incubator/machine-learning-novice-sklearn](https://github.com/carpentries-incubator/machine-learning-novice-sklearn) | [website](https://carpentries-incubator.github.io/machine-learning-novice-sklearn/)
- [**fast.ai** fastai/course20](https://github.com/fastai/course20) | [website](https://book.fast.ai)
- [**SIB Swiss Institute of Bioinformatics** sib-swiss/intro-machine-learning-training](https://github.com/sib-swiss/intro-machine-learning-training)
- [**Phillip Lippe** phlippe/uvadlc_notebooks](https://github.com/phlippe/uvadlc_notebooks/) | [website](https://uvadlc-notebooks.readthedocs.io/en/latest/)

### Statistics

- [**Aedin Culhane** aedin/PCAworkshop](https://github.com/aedin/PCAworkshop) | [website](https://aedin.github.io/PCAworkshop/)
- [**CRUK CI Bioinformatics Core** bioinformatics-core-shared-training/experimental-design](https://github.com/bioinformatics-core-shared-training/experimental-design) | [website](http://bioinformatics-core-shared-training.github.io/experimental-design)
- [**CRUK CI Bioinformatics Core** bioinformatics-core-shared-training/IntroductionToStats](https://github.com/bioinformatics-core-shared-training/IntroductionToStats) | [website](http://bioinformatics-core-shared-training.github.io/IntroductionToStats/)
- [**carpentries-incubator** carpentries-incubator/statistical-thinking-public-health](https://github.com/carpentries-incubator/statistical-thinking-public-health) | [website](https://carpentries-incubator.github.io/statistical-thinking-public-health)
- [**Richard McElreath** rmcelreath/stat_rethinking_2022](https://github.com/rmcelreath/stat_rethinking_2022)
- [**SIB Swiss Institute of Bioinformatics** sib-swiss/advanced-statistics](https://github.com/sib-swiss/advanced-statistics)
- [**SIB Swiss Institute of Bioinformatics** sib-swiss/intro-bayesian-statistics-training](https://github.com/sib-swiss/intro-bayesian-statistics-training)
- [**SIB Swiss Institute of Bioinformatics** sib-swiss/introduction-to-statistics-with-python-training](https://github.com/sib-swiss/introduction-to-statistics-with-python-training)
- [**SIB Swiss Institute of Bioinformatics** sib-swiss/Introduction-to-statistics-with-R](https://github.com/sib-swiss/Introduction-to-statistics-with-R)
- [**SIB Swiss Institute of Bioinformatics** sib-swiss/statistics-and-machine-learning-training](https://github.com/sib-swiss/statistics-and-machine-learning-training)
- [**Richard McElreath** rmcelreath/stat_rethinking_2023](https://github.com/rmcelreath/stat_rethinking_2023)

## Others


### General

- [**Amanda Miotto** amandamiotto/HackyHourBookmarks](https://github.com/amandamiotto/HackyHourBookmarks)
- [**biodatascience** biodatascience/compbio](https://github.com/biodatascience/compbio) | [website](https://biodatascience.github.io/compbio/)
- [**Bradley Boehmke** bradleyboehmke/data-science-learning-resources](https://github.com/bradleyboehmke/data-science-learning-resources)
- [**Ming Tang** crazyhottommy/getting-started-with-genomics-tools-and-resources](https://github.com/crazyhottommy/getting-started-with-genomics-tools-and-resources)
- [**Galaxy Project** galaxyproject/training-material](https://github.com/galaxyproject/training-material) | [website](https://training.galaxyproject.org)
- [**Teaching materials at the Harvard Chan Bioinformatics Core** hbctraining/Training-modules](https://github.com/hbctraining/Training-modules) | [website](https://hbctraining.github.io/Training-modules/)
- [**Genome Informatics Facility** ISUgenomics/bioinformatics-workbook](https://github.com/ISUgenomics/bioinformatics-workbook) | [website](https://bioinformaticsworkbook.org)
- [**Melbourne Bioinformatics** melbournebioinformatics/MelBioInf_docs](https://github.com/melbournebioinformatics/MelBioInf_docs)
- [**Mike Lee** AstrobioMike/AstrobioMike.github.io](https://github.com/AstrobioMike/AstrobioMike.github.io) | [website](https://astrobiomike.github.io)
- [**liulab-dfci** liulab-dfci/bioinfo-combio](https://github.com/liulab-dfci/bioinfo-combio)

[![DOI](https://zenodo.org/badge/437832906.svg)](https://zenodo.org/badge/latestdoi/437832906)

# Bioinformatics training materials

Do you like this collection? You're going to love [glittr.org](https://glittr.org)! The collection below is still maintained but updated by glittr.org. So, if you have anything to add or to ask, see you there!

[![](assets/logo-with-domain-tagline.svg)](https://glittr.org)

If you haven't stopped reading, you're one of the few that still prefer the old school `README` :neckbeard:. Nice!

Below you'll find a curated list of **bioinformatics training material**. All material is:

- In a GitHub or GitLab repository (repositories in self-managed instances of GitLab are not supported anymore..)
- Free to use
- Written in markdown or similar

**NOTE:** This list of courses is selected *only* based on the above criteria. There are *no* checks on quality.

## Contents

- [Scripting and languages](#scripting-and-languages)
  - [Version control](#version-control)
  - [Unix/Linux](#unix/linux)
  - [Python](#python)
  - [R](#r)
  - [Quarto](#quarto)
  - [Shiny](#shiny)
  - [Julia](#julia)
  - [Data visualization](#data-visualization)
  - [Java](#java)
  - [GNU Make](#gnu-make)
  - [MATLAB/Octave](#matlab/octave)
  - [C/C++](#c/c++)
  - [Rust](#rust)
  - [SPARQL](#sparql)
  - [LaTeX](#latex)
- [Computational methods and pipelines](#computational-methods-and-pipelines)
  - [Containerization](#containerization)
  - [Galaxy](#galaxy)
  - [High performance computing](#high-performance-computing)
  - [Nextflow](#nextflow)
  - [Workflows](#workflows)
  - [Image analysis](#image-analysis)
  - [Cloud computing](#cloud-computing)
  - [Data mining](#data-mining)
- [Omics analysis](#omics-analysis)
  - [Genomics](#genomics)
  - [Next generation sequencing](#next-generation-sequencing)
  - [Transcriptomics](#transcriptomics)
  - [RNA-seq](#rna-seq)
  - [Single-cell sequencing](#single-cell-sequencing)
  - [Variant analysis](#variant-analysis)
  - [ChIP-seq](#chip-seq)
  - [Comparative genomics](#comparative-genomics)
  - [Epigenetics](#epigenetics)
  - [Genome annotation](#genome-annotation)
  - [Genome assembly](#genome-assembly)
  - [Metagenomics](#metagenomics)
  - [Epidemiology](#epidemiology)
  - [Microbiology](#microbiology)
  - [Multiomics](#multiomics)
  - [Spatial transcriptomics](#spatial-transcriptomics)
  - [Long read sequencing](#long-read-sequencing)
  - [Metabolomics](#metabolomics)
  - [Proteomics](#proteomics)
  - [Pathways and Networks](#pathways-and-networks)
  - [Protein structure](#protein-structure)
- [Reproducibility and data management](#reproducibility-and-data-management)
  - [Data management](#data-management)
  - [FAIR data](#fair-data)
  - [Reproducibility](#reproducibility)
- [Statistics and machine learning](#statistics-and-machine-learning)
  - [Data science](#data-science)
  - [Statistics](#statistics)
  - [Machine learning](#machine-learning)
  - [Artificial intelligence](#artificial-intelligence)
- [Others](#others)
  - [General](#general)

## Scripting and languages


### Version control

- [**Software Carpentry** swcarpentry/git-novice](https://github.com/swcarpentry/git-novice) | [website](http://swcarpentry.github.io/git-novice/)
- [**BioinfGuru** BioinfGuru/gitTutorial](https://github.com/BioinfGuru/gitTutorial)
- [**Kottans** kottans/git-course](https://github.com/kottans/git-course) | [website](https://kottans.org/git-course/)
- [**Gerard Capes** gcapes/git-course](https://github.com/gcapes/git-course) | [website](http://gcapes.github.io/git-course/)
- [**The Carpentries Incubator** carpentries-incubator/gitlab-novice](https://github.com/carpentries-incubator/gitlab-novice) | [website](https://carpentries-incubator.github.io/gitlab-novice/)
- [**Data Carpentry** datacarpentry/rr-version-control](https://github.com/datacarpentry/rr-version-control) | [website](http://www.datacarpentry.org/rr-version-control/)
- [**VIB Technologies: Training material and software projects** vibbits/introduction-github](https://github.com/vibbits/introduction-github) | [website](https://liascript.github.io/course/#1)
- [**NBIS - National Bioinformatics Infrastructure Sweden** NBISweden/module-versioning-dm-practices](https://github.com/NBISweden/module-versioning-dm-practices/) | [website](https://nbisweden.github.io/module-versioning-dm-practices/)
- [**Sergio Martínez Cuesta** semacu/20190927_IntroductionGithub_HDRUK](https://github.com/semacu/20190927_IntroductionGithub_HDRUK)
- [**Sergio Martínez Cuesta** semacu/20181003_Intro_git_GitHub](https://github.com/semacu/20181003_Intro_git_GitHub)
- [**Sergio Martínez Cuesta** semacu/20171024_GitHub_Chemistry_Cambridge](https://github.com/semacu/20171024_GitHub_Chemistry_Cambridge)
- [**posit::conf(2024)** posit-conf-2024/dev-ops](https://github.com/posit-conf-2024/dev-ops)

### Unix/Linux

- [**Data Carpentry** datacarpentry/shell-genomics](https://github.com/datacarpentry/shell-genomics) | [website](https://datacarpentry.org/shell-genomics)
- [**Teaching materials at the Harvard Chan Bioinformatics Core** hbctraining/Shell-for-bioinformatics](https://github.com/hbctraining/Intro-to-shell-flipped) | [website](https://hbctraining.github.io/Shell-for-bioinformatics/)
- [**Ted Laderas** laderast/bash_for_bioinformatics](https://github.com/laderast/bash_for_bioinformatics) | [website](https://laderast.github.io/bash_for_bioinformatics/)
- [**SIB Swiss Institute of Bioinformatics** sib-swiss/unix-first-steps-training](https://github.com/sib-swiss/unix-first-steps-training)
- [**Software Carpentry** swcarpentry/shell-novice](https://github.com/swcarpentry/shell-novice) | [website](http://swcarpentry.github.io/shell-novice/)
- [**Sundeep Agarwal** learnbyexample/cli_text_processing_coreutils](https://github.com/learnbyexample/cli_text_processing_coreutils) | [website](https://learnbyexample.github.io/cli_text_processing_coreutils/)
- [**Sundeep Agarwal** learnbyexample/cli-computing](https://github.com/learnbyexample/cli-computing) | [website](https://learnbyexample.github.io/cli-computing/)
- [**Sundeep Agarwal** learnbyexample/learn_gnuawk](https://github.com/learnbyexample/learn_gnuawk) | [website](https://learnbyexample.github.io/learn_gnuawk/)
- [**Sundeep Agarwal** learnbyexample/learn_gnused](https://github.com/learnbyexample/learn_gnused) | [website](https://learnbyexample.github.io/learn_gnused/)
- [**Sundeep Agarwal** learnbyexample/learn_gnugrep_ripgrep](https://github.com/learnbyexample/learn_gnugrep_ripgrep) | [website](https://learnbyexample.github.io/learn_gnugrep_ripgrep/)
- [**slackermedia** slackermedia/bashcrawl](https://gitlab.com/slackermedia/bashcrawl)
- [**The Carpentries Incubator** carpentries-incubator/shell-extras](https://github.com/carpentries-incubator/shell-extras) | [website](http://carpentries-incubator.github.io/shell-extras/)
- [**The Carpentries Lab** carpentries-lab/metagenomics-shell](https://github.com/carpentries-lab/metagenomics-shell) | [website](https://carpentries-lab.github.io/metagenomics-shell/)
- [**UC Davis Bioinformatics Core Training Page** ucdavis-bioinformatics-training/2023-September-Introduction-to-the-Command-Line-for-Bioinformatics](https://github.com/ucdavis-bioinformatics-training/2023-September-Introduction-to-the-Command-Line-for-Bioinformatics)
- [**Cloud-SPAN** Cloud-SPAN/prenomics00-intro](https://github.com/cloud-span/prenomics00-intro) | [website](https://cloud-span.github.io/prenomics00-intro/)
- [**Sergio Martínez Cuesta** semacu/20180726_TrainMalta_Unix_R](https://github.com/semacu/20180726_TrainMalta_Unix_R)
- [**Bobby Iliev** bobbyiliev/introduction-to-bash-scripting](https://github.com/bobbyiliev/introduction-to-bash-scripting) | [website](https://leanpub.com/b/linux-devops-ebook-bundle)
- [**Firas Zemzem** Zemzemfiras1/Mastering_Linux_Tutorials](https://github.com/Zemzemfiras1/Mastering_Linux_Tutorials)
- [**Jeroen Janssens** jeroenjanssens/data-science-at-the-command-line](https://github.com/jeroenjanssens/data-science-at-the-command-line) | [website](https://datascienceatthecommandline.com)

### Python

- [**The Carpentries Incubator** carpentries-incubator/introduction-to-conda-for-data-scientists](https://github.com/carpentries-incubator/introduction-to-conda-for-data-scientists) | [website](https://carpentries-incubator.github.io/introduction-to-conda-for-data-scientists/)
- [**The Carpentries Incubator** carpentries-incubator/python-interactive-data-visualizations](https://github.com/carpentries-incubator/python-interactive-data-visualizations) | [website](https://carpentries-incubator.github.io/python-interactive-data-visualizations/)
- [**Jake Vanderplas** jakevdp/PythonDataScienceHandbook](https://github.com/jakevdp/PythonDataScienceHandbook) | [website](http://jakevdp.github.io/PythonDataScienceHandbook)
- [**Jake Vanderplas** jakevdp/WhirlwindTourOfPython](https://github.com/jakevdp/WhirlwindTourOfPython)
- [**Plants&Python** PlantsAndPython/PlantsAndPython](https://github.com/PlantsAndPython/PlantsAndPython)
- [**SIB Swiss Institute of Bioinformatics** sib-swiss/first-steps-with-python-training](https://github.com/sib-swiss/first-steps-with-python-training)
- [**SIB Swiss Institute of Bioinformatics** sib-swiss/intermediate-python-training](https://github.com/sib-swiss/intermediate-python-training)
- [**Software Carpentry** swcarpentry/python-novice-inflammation](https://github.com/swcarpentry/python-novice-inflammation) | [website](http://swcarpentry.github.io/python-novice-inflammation/)
- [**VIB Technologies: Training material and software projects** vibbits/gentle-hands-on-python](https://github.com/vibbits/gentle-hands-on-python)
- [**Talk Python** talkpython/python-for-absolute-beginners-course](https://github.com/talkpython/python-for-absolute-beginners-course) | [website](https://training.talkpython.fm/courses/explore_beginners/python-for-absolute-beginners)
- [**Sundeep Agarwal** learnbyexample/py_regular_expressions](https://github.com/learnbyexample/py_regular_expressions) | [website](https://learnbyexample.github.io/py_regular_expressions/)
- [**Sundeep Agarwal** learnbyexample/100_page_python_intro](https://github.com/learnbyexample/100_page_python_intro) | [website](https://learnbyexample.github.io/100_page_python_intro/)
- [**Alex Hall** alexmojaki/futurecoder](https://github.com/alexmojaki/futurecoder) | [website](https://futurecoder.io)
- [**Guillaume Gautier** guilgautier/sdia-python](https://github.com/guilgautier/sdia-python)
- [**cambiotraining** cambiotraining/python-data-science](https://github.com/cambiotraining/python-data-science)
- [**The Carpentries Incubator** carpentries-incubator/python-text-analysis](https://github.com/carpentries-incubator/python-text-analysis) | [website](https://carpentries-incubator.github.io/python-text-analysis/)
- [**The Carpentries Incubator** carpentries-incubator/python_packaging](https://github.com/carpentries-incubator/python_packaging) | [website](https://carpentries-incubator.github.io/python_packaging)
- [**The Carpentries Incubator** carpentries-incubator/python-testing](https://github.com/carpentries-incubator/python-testing) | [website](http://carpentries-incubator.github.io/python-testing/)
- [**The Carpentries Incubator** carpentries-incubator/python-intermediate-development](https://github.com/carpentries-incubator/python-intermediate-development) | [website](https://carpentries-incubator.github.io/python-intermediate-development/)
- [**The Carpentries Incubator** carpentries-incubator/python-packaging-publishing](https://github.com/carpentries-incubator/python-packaging-publishing) | [website](https://carpentries-incubator.github.io/python-packaging-publishing/)
- [**The Carpentries Incubator** carpentries-incubator/lesson-parallel-python](https://github.com/carpentries-incubator/lesson-parallel-python) | [website](https://carpentries-incubator.github.io/lesson-parallel-python/)
- [**The Algorithms** TheAlgorithms/Python](https://github.com/TheAlgorithms/Python) | [website](https://thealgorithms.github.io/Python/)
- [**Oleksii Trekhleb** trekhleb/learn-python](https://github.com/trekhleb/learn-python)
- [**João Ventura** joaoventura/full-speed-python](https://github.com/joaoventura/full-speed-python)
- [**Sebastian Raschka** rasbt/python_reference](https://github.com/rasbt/python_reference)
- [**Jeffrey Hu** zhiwehu/Python-programming-exercises](https://github.com/zhiwehu/Python-programming-exercises)
- [**LiaBooks ... by LiaScript** LiaBooks/How-To-Code-in-Python-3](https://github.com/LiaBooks/How-To-Code-in-Python-3) | [website](https://liascript.github.io/course/)
- [**LiaPlayground** LiaPlayground/PythonProgramming](https://github.com/LiaPlayground/PythonProgramming)
- [**Valentin Danchev** valdanchev/reproducible-data-science-python](https://github.com/valdanchev/reproducible-data-science-python)
- [**Girls Who Code at U-M DCMB** GWC-DCMB/GWC-DCMB](https://github.com/GWC-DCMB/GWC-DCMB) | [website](http://umich.edu/~girlswc/)
- [**UC Davis Bioinformatics Core Training Page** ucdavis-bioinformatics-training/2023-July-Introduction-To-Python-For-Bioinformatics](https://github.com/ucdavis-bioinformatics-training/2023-July-Introduction-To-Python-For-Bioinformatics)
- [**The Gulbenkian Training Programme in Bioinformatics** GTPB/PPB18](https://github.com/gtpb/PPB18) | [website](https://gtpb.github.io/PPB18/)
- [**Swaroop CH** swaroopch/byte-of-python](https://github.com/swaroopch/byte-of-python) | [website](https://python.swaroopch.com)
- [**S.Lott** slott56/building-skills-oo-design-book](https://github.com/slott56/building-skills-oo-design-book) | [website](https://slott56.github.io/building-skills-oo-design-book/build/html/index.html)
- [**Real Python** realpython/python-guide](https://github.com/realpython/python-guide) | [website](https://docs.python-guide.org)
- [**OpenTechSchool** OpenTechSchool/python-beginners](https://github.com/OpenTechSchool/python-beginners) | [website](http://opentechschool.github.io/python-beginners/)
- [**Ankit Mahato** animator/learn-python](https://github.com/animator/learn-python) | [website](https://animator.github.io/learn-python/)
- [**Sundeep Agarwal** learnbyexample/practice_python_projects](https://github.com/learnbyexample/practice_python_projects) | [website](https://learnbyexample.github.io/practice_python_projects/)
- [**SoftUni** SoftUni/Programming-Basics-Book-Python-EN](https://github.com/SoftUni/Programming-Basics-Book-Python-EN) | [website](https://python-book.softuni.org)
- [**Akuli** Akuli/python-tutorial](https://github.com/Akuli/python-tutorial)
- [**Charles Severance** csev/py4e](https://github.com/csev/py4e) | [website](http://www.py4e.com)
- [**Kushal Das** kushaldas/pym](https://github.com/kushaldas/pym)
- [**Greg Malcolm** gregmalcolm/python_koans](https://github.com/gregmalcolm/python_koans)
- [**BioINForm** bioinform-org/bioinforming-hs](https://github.com/bioinform-org/bioinforming-hs)
- [**Daniel Chen** chendaniely/positconf2023-academy_python](https://github.com/chendaniely/positconf2023-academy_python)
- [**Rami Krispin** RamiKrispin/vscode-python](https://github.com/RamiKrispin/vscode-python)
- [**Wes McKinney** wesm/pydata-book](https://github.com/wesm/pydata-book)
- [**Kevin Heavey** kevinheavey/modern-polars](https://github.com/kevinheavey/modern-polars/) | [website](https://kevinheavey.github.io/modern-polars/)
- [**Python Packages** py-pkgs/py-pkgs](https://github.com/py-pkgs/py-pkgs) | [website](https://py-pkgs.org)
- [**bioinfo-prog** bioinfo-prog/cours-python](https://github.com/bioinfo-prog/cours-python) | [website](https://python.sdv.u-paris.fr)
- [**R. Burke Squires** burkesquires/python_biologist](https://github.com/burkesquires/python_biologist)
- [**Sergio Martínez Cuesta** semacu/data-science-python](https://github.com/semacu/data-science-python)
- [**MolSSI Education** MolSSI-Education/python_scripting_cms](https://github.com/MolSSI-Education/python_scripting_cms) | [website](https://molssi-education.github.io/python_scripting_cms)
- [**Jean de Dieu Nyandwi** Nyandwi/PythonBasics](https://github.com/Nyandwi/PythonBasics)
- [**Scott Reed** scottmreed/molecular_informatics](https://github.com/scottmreed/molecular_informatics/tree/main)
- [**Scott Reed** scottmreed/Code_withGPT_tutorial](https://github.com/scottmreed/Code_withGPT_tutorial)
- [**Dan Chitwood** DanChitwood/plants_and_python](https://github.com/DanChitwood/plants_and_python) | [website](https://danchitwood.github.io/plants_and_python)

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
- [**The Carpentries Incubator** carpentries-incubator/bioc-project](https://github.com/carpentries-incubator/bioc-project) | [website](https://carpentries-incubator.github.io/bioc-project)
- [**The Carpentries Incubator** carpentries-incubator/high-dimensional-stats-r](https://github.com/carpentries-incubator/high-dimensional-stats-r) | [website](https://carpentries-incubator.github.io/high-dimensional-stats-r)
- [**Colautti Lab** ColauttiLab/RCrashCourse_Book](https://github.com/ColauttiLab/RCrashCourse_Book)
- [**Computational Cancer Biology and Epigenomics** CompEpigen/BasicR](https://github.com/CompEpigen/BasicR) | [website](https://compepigen.github.io/BasicR/)
- [**Colin Gillespie** csgillespie/efficientR](https://github.com/csgillespie/efficientR) | [website](https://csgillespie.github.io/efficientR/)
- [**C. Li** cxli233/Online_R_learning](https://github.com/cxli233/Online_R_learning)
- [**Davis Laboratory** DavisLaboratory/GenesetAnalysisWorkflow](https://github.com/DavisLaboratory/GenesetAnalysisWorkflow) | [website](https://davislaboratory.github.io/GenesetAnalysisWorkflow/)
- [**David Robinson** juliasilge/tidy-text-mining](https://github.com/dgrtwo/tidy-text-mining) | [website](http://tidytextmining.com)
- [**Danielle Navarro** djnavarro/rbook](https://github.com/djnavarro/rbook) | [website](https://learningstatisticswithr.com)
- [**Duke Department of Statistical Science** DukeStatSci/introds](https://github.com/DukeStatSci/introds) | [website](https://introds-duke.netlify.app)
- [**Hadley Wickham** hadley/adv-r](https://github.com/hadley/adv-r) | [website](http://adv-r.hadley.nz)
- [**Hadley Wickham** hadley/r4ds](https://github.com/hadley/r4ds) | [website](https://r4ds.hadley.nz)
- [**Teaching materials at the Harvard Chan Bioinformatics Core** hbctraining/Intro-to-R-flipped](https://github.com/hbctraining/Intro-to-R-flipped) | [website](https://hbctraining.github.io/Intro-to-R-flipped/)
- [**ICS 80 - Introduction to Data Science** ics80-fa21/website](https://github.com/ics80-fa21/website) | [website](https://ics80-fa21.github.io/website/)
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
- [**rstudio::conf(2022)** rstudio-conf-2022/art-from-code](https://github.com/rstudio-conf-2022/art-from-code) | [website](https://art-from-code.netlify.app)
- [**rstudio::conf(2022)** rstudio-conf-2022/build-tidy-tools](https://github.com/rstudio-conf-2022/build-tidy-tools) | [website](https://rstd.io/btt)
- [**rstudio::conf(2022)** rstudio-conf-2022/get-started-quarto](https://github.com/rstudio-conf-2022/get-started-quarto) | [website](https://rstudio-conf-2022.github.io/get-started-quarto/)
- [**rstudio::conf(2022)** rstudio-conf-2022/get-started-shiny](https://github.com/rstudio-conf-2022/get-started-shiny) | [website](https://rstd.io/start-shiny)
- [**rstudio::conf(2022)** rstudio-conf-2022/ggplot2-graphic-design](https://github.com/rstudio-conf-2022/ggplot2-graphic-design) | [website](https://rstudio-conf-2022.github.io/ggplot2-graphic-design/)
- [**rstudio::conf(2022)** rstudio-conf-2022/intro-to-tidyverse](https://github.com/rstudio-conf-2022/intro-to-tidyverse) | [website](https://conf22-intro-tidyverse.netlify.app)
- [**rstudio::conf(2022)** rstudio-conf-2022/shiny-prod-apps](https://github.com/rstudio-conf-2022/shiny-prod-apps) | [website](https://shinyprod.com)
- [**rstudio::conf(2022)** rstudio-conf-2022/teach-ds](https://github.com/rstudio-conf-2022/teach-ds) | [website](https://rstd.io/teach-ds-conf22)
- [**rstudio::conf(2022)** rstudio-conf-2022/wtf-rstats](https://github.com/rstudio-conf-2022/wtf-rstats)
- [**RStudio** rstudio/rmarkdown-book](https://github.com/rstudio/rmarkdown-book) | [website](https://bookdown.org/yihui/rmarkdown)
- [**Saskia** SaskiaFreytag/biocommons-r-intro](https://github.com/SaskiaFreytag/biocommons-r-intro) | [website](https://saskiafreytag.github.io/biocommons-r-intro/)
- [**Sean Davis** seandavi/ITR](https://github.com/seandavi/ITR) | [website](https://seandavi.github.io/ITR)
- [**SIB Swiss Institute of Bioinformatics** sib-swiss/enrichment-analysis-training](https://github.com/sib-swiss/enrichment-analysis-training) | [website](https://sib-swiss.github.io/enrichment-analysis-training/)
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
- [**The Carpentries Incubator** carpentries-incubator/bioc-intro](https://github.com/carpentries-incubator/bioc-intro) | [website](https://carpentries-incubator.github.io/bioc-intro)
- [**R Programming @ University of Cincinnati** uc-r/Advanced-R](https://github.com/uc-r/Advanced-R)
- [**R Programming @ University of Cincinnati** uc-r/Intro-R](https://github.com/uc-r/Intro-R)
- [**R Programming @ University of Cincinnati** uc-r/Intermediate-R](https://github.com/uc-r/Intermediate-R)
- [**RStudio Education** rstudio-education/advanced-shiny-az](https://github.com/rstudio-education/advanced-shiny-az) | [website](https://rstd.io/adv-shiny-az)
- [**RStudio** rstudio/learnr](https://github.com/rstudio/learnr) | [website](https://pkgs.rstudio.com/learnr)
- [**dcruvolo** davidruvolo51/shinyAppTutorials](https://github.com/davidruvolo51/shinyAppTutorials) | [website](https://davidruvolo51.github.io/shinytutorials/)
- [**Max Planck Institute of Immunobiology and Epigenetics** maxplanck-ie/Rintro](https://github.com/maxplanck-ie/Rintro/)
- [**CRUK CI Bioinformatics Core** bioinformatics-core-shared-training/r-basics](https://github.com/bioinformatics-core-shared-training/r-basics)
- [**NBIS - National Bioinformatics Infrastructure Sweden** NBISweden/workshop-data-visualization-r](https://github.com/NBISweden/workshop-data-visualization-r) | [website](https://nbisweden.github.io/workshop-data-visualization-r/)
- [**The Carpentries Incubator** carpentries-incubator/lc-litsearchr](https://github.com/carpentries-incubator/lc-litsearchr) | [website](https://carpentries-incubator.github.io/lc-litsearchr/)
- [**The Carpentries Incubator** carpentries-incubator/R-ecology-lesson](https://github.com/carpentries-incubator/R-ecology-lesson) | [website](https://carpentries-incubator.github.io/R-ecology-lesson/)
- [**The Carpentries Incubator** carpentries-incubator/R-ecology-lesson-intermediate](https://github.com/carpentries-incubator/R-ecology-lesson-intermediate) | [website](https://carpentries-incubator.github.io/R-ecology-lesson-intermediate/)
- [**The Carpentries Incubator** carpentries-incubator/open-science-with-r](https://github.com/carpentries-incubator/open-science-with-r) | [website](https://carpentries-incubator.github.io/open-science-with-r/)
- [**The Carpentries Incubator** carpentries-incubator/reproducible-publications-quarto](https://github.com/carpentries-incubator/Reproducible-Publications-with-RStudio) | [website](https://carpentries-incubator.github.io/reproducible-publications-quarto/)
- [**Data Carpentry** datacarpentry/R-ecology-lesson](https://github.com/datacarpentry/R-ecology-lesson) | [website](https://datacarpentry.org/R-ecology-lesson/)
- [**Data Carpentry** datacarpentry/genomics-r-intro](https://github.com/datacarpentry/genomics-r-intro) | [website](https://datacarpentry.org/genomics-r-intro/)
- [**Data Carpentry** datacarpentry/rr-automation](https://github.com/datacarpentry/rr-automation) | [website](http://www.datacarpentry.org/rr-automation/)
- [**Data Carpentry** datacarpentry/rr-literate-programming](https://github.com/datacarpentry/rr-literate-programming)
- [**RStudio Education** rstudio-education/stat545](https://github.com/rstudio-education/stat545) | [website](https://stat545.com)
- [**nullranges** tidyomics/tidy-ranges-tutorial](https://github.com/nullranges/tidy-ranges-tutorial) | [website](https://tidyomics.github.io/tidy-ranges-tutorial/)
- [**NBIS - National Bioinformatics Infrastructure Sweden** NBISweden/workshop-epigenomics-RTDs](https://github.com/NBISweden/workshop-epigenomics-RTDs/) | [website](https://nbis-workshop-epigenomics.readthedocs.io/en/latest/)
- [**Library Data Services** UNC-Libraries-data/R-Open-Labs](https://github.com/UNC-Libraries-data/R-Open-Labs) | [website](https://tarheels.live/beginr/)
- [**Greg Wilson** gvwilson/tidynomicon](https://github.com/gvwilson/tidynomicon) | [website](http://tidynomicon.github.io/tidynomicon)
- [**Vince Carey** vjcitn/BiocPyInterop](https://github.com/vjcitn/BiocPyInterop) | [website](https://vjcitn.github.io/BiocPyInterop/)
- [**Bioinformatics, Rockefeller University** RockefellerUniversity/RU_VisualizingGenomicsData](https://github.com/RockefellerUniversity/RU_VisualizingGenomicsData)
- [**genomicsclass** genomicsclass/book](https://github.com/genomicsclass/book) | [website](http://genomicsclass.github.io/book/)
- [**Kristyna Kupkova** kkupkova/GenomicDistributionsBioC2022](https://github.com/kkupkova/GenomicDistributions_BioC2022)
- [**Workflow Languages in R** rworkflow/RcwlWorkshop](https://github.com/rworkflow/RcwlWorkshop) | [website](http://rcwl.org/RcwlWorkshop/)
- [**tidyomics** tidyomics/tidyomicsWorkshopBioc2023](https://github.com/tidyomics/tidyomicsWorkshopBioc2023) | [website](https://tidyomics.github.io/tidyomicsWorkshopBioc2023)
- [**Surgical Informatics** SurgicalInformatics/healthyr_book](https://github.com/SurgicalInformatics/healthyr_book/tree/master) | [website](https://argoshare.is.ed.ac.uk/healthyr_book/)
- [**Trevor French** TrevorFrench/R-for-Data-Analysis](https://github.com/TrevorFrench/R-for-Data-Analysis) | [website](https://trevorfrench.github.io/R-for-Data-Analysis/)
- [**UM Carpentries** UMCarpentries/intro-curriculum-r](https://github.com/UMCarpentries/intro-curriculum-r/) | [website](https://umcarpentries.org/intro-curriculum-r/)
- [**rostools** rostools/r-cubed-intro](https://github.com/rostools/r-cubed-intro) | [website](https://r-cubed-intro.rostools.org)
- [**NBIS - National Bioinformatics Infrastructure Sweden** NBISweden/module-rstudio-intro-dm-practices](https://github.com/NBISweden/module-rstudio-intro-dm-practices/) | [website](https://nbisweden.github.io/module-rstudio-intro-dm-practices/)
- [**NBIS - National Bioinformatics Infrastructure Sweden** NBISweden/module-r-intro-dm-practices](https://github.com/NBISweden/module-r-intro-dm-practices/) | [website](https://nbisweden.github.io/module-r-intro-dm-practices/)
- [**bioinformatics.ca** bioinformaticsdotca/AUR_2023](https://github.com/bioinformaticsdotca/AUR_2023)
- [**Computational Biology and Bioinformatics at UCLouvain** UCLouvain-CBIO/WSBIM1207](https://github.com/UCLouvain-CBIO/WSBIM1207) | [website](https://UCLouvain-CBIO.github.io/WSBIM1207/)
- [**UC Davis Bioinformatics Core Training Page** ucdavis-bioinformatics-training/2023-June-Introduction-to-R-for-Bioinformatics](https://github.com/ucdavis-bioinformatics-training/2023-June-Introduction-to-R-for-Bioinformatics)
- [**Institut Français de Bioinformatique (IFB)** IFB-ElixirFr/IFB_Shiny_training](https://github.com/IFB-ElixirFr/IFB_Shiny_training) | [website](https://ifb-elixirfr.github.io/IFB_Shiny_training/)
- [**bioinformatics.ca** bioinformaticsdotca/INR_2023](https://github.com/bioinformaticsdotca/INR_2023)
- [**ELIXIR Estonia** ELIXIREstonia/2023-10-24-R-basic](https://github.com/ELIXIREstonia/2023-10-24-R-basic) | [website](https://elixir.ut.ee/node/552)
- [**The Gulbenkian Training Programme in Bioinformatics** GTPB/ABSTAT18](https://github.com/gtpb/ABSTAT18) | [website](https://gtpb.github.io/ABSTAT18/)
- [**Hugo Tavares** tavareshugo/2018-06-28-cambridge](https://github.com/tavareshugo/2018-06-28-cambridge) | [website](https://tavareshugo.github.io/2018-06-28-cambridge/)
- [**Sergio Martínez Cuesta** semacu/20180531_DataVisualisationRggplot2_Wolfson_Cambridge](https://github.com/semacu/20180531_DataVisualisationRggplot2_Wolfson_Cambridge)
- [**Data Carpentry** datacarpentry/ecology-workshop](https://github.com/datacarpentry/ecology-workshop) | [website](http://www.datacarpentry.org/ecology-workshop/)
- [**Jacques van Helden** jvanheld/stats_avec_RStudio_EBA](https://github.com/jvanheld/stats_avec_RStudio_EBA) | [website](http://jvanheld.github.io/stats_avec_RStudio_EBA/)
- [**Data Challenge Lab Open Content** dcl-docs/prog](https://github.com/dcl-docs/prog) | [website](https://dcl-prog.stanford.edu)
- [**G. Jay Kerns** gjkerns/IPSUR](https://github.com/gjkerns/IPSUR) | [website](http://ipsur.org)
- [**Roger D. Peng** rdpeng/rprogdatascience](https://github.com/rdpeng/rprogdatascience)
- [**Marek Gagolewski** gagolews/deepr](https://github.com/gagolews/deepr) | [website](https://deepr.gagolewski.com)
- [**bougioukas** bougioukas/practical_stats_med-r](https://github.com/bougioukas/practical_stats_med-r)
- [**TaniaW** taniawyss/flow-cytometry-analysis-with-R](https://github.com/taniawyss/flow-cytometry-analysis-with-R/) | [website](https://taniawyss.github.io/flow-cytometry-analysis-with-R/)
- [**Roger D. Peng** rdpeng/exdata](https://github.com/rdpeng/exdata)
- [**posit-conf-2023** posit-conf-2023/r-intro](https://github.com/posit-conf-2023/r-intro/) | [website](https://intro-tidyverse-2023.netlify.app)
- [**posit-conf-2023** posit-conf-2023/forecasting](https://github.com/posit-conf-2023/forecasting) | [website](https://posit-conf-2023.github.io/forecasting/)
- [**posit-conf-2023** posit-conf-2023/pkg-dev-masterclass](https://github.com/posit-conf-2023/pkg-dev-masterclass)
- [**posit-conf-2023** posit-conf-2023/pkg-dev](https://github.com/posit-conf-2023/pkg-dev) | [website](https://posit-conf-2023.github.io/pkg-dev/)
- [**What They Forgot to Teach You About R** rstats-wtf/what-they-forgot](https://github.com/rstats-wtf/what-they-forgot) | [website](https://rstats.wtf)
- [**posit-conf-2023** posit-conf-2023/arrow](https://github.com/posit-conf-2023/arrow) | [website](https://posit-conf-2023.github.io/arrow/)
- [**posit-conf-2023** posit-conf-2023/dataviz-storytelling](https://github.com/posit-conf-2023/dataviz-storytelling) | [website](https://posit-conf-2023.github.io/dataviz-storytelling/)
- [**posit-conf-2023** posit-conf-2023/ds-workflows-r](https://github.com/posit-conf-2023/ds-workflows-r) | [website](https://katie.quarto.pub/ds-workflows-r/)
- [**posit-conf-2023** posit-conf-2023/vetiver](https://github.com/posit-conf-2023/vetiver) | [website](https://posit-conf-2023.github.io/vetiver/)
- [**posit-conf-2023** posit-conf-2023/programming-r](https://github.com/posit-conf-2023/programming-r) | [website](https://posit-conf-2023.github.io/programming-r/)
- [**posit-conf-2023** posit-conf-2023/teach-ds-masterclass](https://github.com/posit-conf-2023/teach-ds-masterclass) | [website](https://pos.it/teach-ds-conf23)
- [**posit-conf-2023** posit-conf-2023/dataviz-ggplot2](https://github.com/posit-conf-2023/dataviz-ggplot2) | [website](https://posit-conf-2023.github.io/dataviz-ggplot2/)
- [**posit-conf-2023** posit-conf-2023/creative-coding](https://github.com/posit-conf-2023/creative-coding)
- [**Rami Krispin** RamiKrispin/vscode-r](https://github.com/RamiKrispin/vscode-r)
- [**Winston Chang** wch/rgcookbook](https://github.com/wch/rgcookbook) | [website](http://r-graphics.org)
- [**RStudio** rstudio/rmarkdown-cookbook](https://github.com/rstudio/rmarkdown-cookbook) | [website](https://bookdown.org/yihui/rmarkdown-cookbook/)
- [**RStudio Education** rstudio-education/hopr](https://github.com/rstudio-education/hopr)
- [**swirl development team** swirldev/swirl](https://github.com/swirldev/swirl) | [website](http://swirlstats.com)
- [**JD Long** CerebralMastication/R-Cookbook](https://github.com/CerebralMastication/R-Cookbook)
- [**r-spark** r-spark/the-r-in-spark](https://github.com/r-spark/the-r-in-spark) | [website](http://therinspark.com)
- [**R for the Rest of Us** rfortherestofus/book](https://github.com/rfortherestofus/book)
- [**Michael Teske** mictes/Shiny_Tutorial](https://github.com/mictes/Shiny_Tutorial) | [website](https://mictes.github.io/Shiny_Tutorial/)
- [**jjallaire** jjallaire/hopr](https://github.com/jjallaire/hopr)
- [**Rohan Alexander** RohanAlexander/telling_stories](https://github.com/RohanAlexander/telling_stories/) | [website](https://rohanalexander.github.io/telling_stories/)
- [**Leonardo Collado-Torres** lcolladotor/cshl_rstats_genome_scale_2024](https://github.com/lcolladotor/cshl_rstats_genome_scale_2024) | [website](https://lcolladotor.github.io/cshl_rstats_genome_scale_2024)
- [**Sophie Lee** sophie-a-lee/Introduction_R_Tidyverse_course](https://github.com/sophie-a-lee/Introduction_R_Tidyverse_course) | [website](https://introduction-r-tidyverse.netlify.app)
- [**Sophie Lee** sophie-a-lee/intro-rstudio-mhclg](https://github.com/sophie-a-lee/introduction_rstudio_dluch) | [website](https://intro-r-dluch.netlify.app)
- [**Stephen Turner** stephenturner/workshops](https://github.com/stephenturner/workshops) | [website](http://stephenturner.github.io/workshops)
- [**Fred Hutch Data Science Lab** fhdsl/Tools_for_Reproducible_Workflows_in_R](https://github.com/fhdsl/Tools_for_Reproducible_Workflows_in_R) | [website](https://hutchdatascience.org/Tools_for_Reproducible_Workflows_in_R/)
- [**Aditya Dahiya** Aditya-Dahiya/ggplot2book3e](https://github.com/Aditya-Dahiya/ggplot2book3e/)
- [**posit::conf(2024)** posit-conf-2024/arrow](https://github.com/posit-conf-2024/arrow) | [website](https://posit-conf-2024.github.io/arrow/)
- [**posit::conf(2024)** posit-conf-2024/ds-workflows-r](https://github.com/posit-conf-2024/ds-workflows-r) | [website](https://posit-conf-2024.github.io/ds-workflows-r/)
- [**posit::conf(2024)** posit-conf-2024/databases](https://github.com/posit-conf-2024/databases) | [website](https://pos.it/databases-24)
- [**posit::conf(2024)** posit-conf-2024/pharmaverse](https://github.com/posit-conf-2024/pharmaverse) | [website](https://posit-conf-2024.github.io/pharmaverse/)
- [**posit::conf(2024)** posit-conf-2024/programming-r](https://github.com/posit-conf-2024/programming-r) | [website](https://posit-conf-2024.github.io/programming-r/)
- [**Northwestern IT Research Computing and Data Services** nuitrcs/R-intro-tidyverse-2025](https://github.com/nuitrcs/R-intro-tidyverse-2024)
- [**posit::conf(2024)** posit-conf-2024/tables](https://github.com/posit-conf-2024/tables)
- [**posit::conf(2024)** posit-conf-2024/pkg-dev](https://github.com/posit-conf-2024/pkg-dev)
- [**posit::conf(2024)** posit-conf-2024/r-in-production](https://github.com/posit-conf-2024/r-in-production)
- [**posit::conf(2024)** posit-conf-2024/databricks](https://github.com/posit-conf-2024/databricks) | [website](https://posit-conf-2024.github.io/databricks/)
- [**posit::conf(2024)** posit-conf-2024/wtf](https://github.com/posit-conf-2024/wtf)
- [**C. Li** cxli233/Quick_data_vis](https://github.com/cxli233/Quick_data_vis)
- [**Bruno Rodrigues** b-rodrigues/rap4all](https://github.com/b-rodrigues/rap4all) | [website](https://raps-with-r.dev)
- [**Rebecca Barter** rlbarter/r-workshop-book](https://github.com/rlbarter/r-workshop-book)

### Quarto

- [**Master of Environmental Data Science (MEDS) program** UCSB-MEDS/customizing-quarto-websites](https://github.com/UCSB-MEDS/customizing-quarto-websites) | [website](https://ucsb-meds.github.io/customizing-quarto-websites/)
- [**Master of Environmental Data Science (MEDS) program** UCSB-MEDS/creating-quarto-websites](https://github.com/UCSB-MEDS/creating-quarto-websites) | [website](https://ucsb-meds.github.io/creating-quarto-websites/)
- [**posit-conf-2023** posit-conf-2023/quarto-r](https://github.com/posit-conf-2023/quarto-r) | [website](https://posit-conf-2023.github.io/quarto-r/)
- [**Hamel Husain** hamelsmu/posit-python-quarto](https://github.com/hamelsmu/posit-python-quarto) | [website](https://bit.ly/pyquarto)
- [**Isabella Velásquez** ivelasq/2024-01-23_getting-started-with-report-writing-using-quarto](https://github.com/ivelasq/2024-01-23_getting-started-with-report-writing-using-quarto) | [website](https://ivelasq.quarto.pub/getting-started-with-report-writing-using-quarto/#/title-slide)
- [**Julien Roux** julien-roux/SIB_days_2024_workshop_EDI](https://github.com/julien-roux/SIB_days_2024_workshop_EDI/)
- [**posit::conf(2024)** posit-conf-2024/quarto-dashboards](https://github.com/posit-conf-2024/quarto-dashboards) | [website](https://posit-conf-2024.github.io/quarto-dashboards/)
- [**posit::conf(2024)** posit-conf-2024/quarto-websites](https://github.com/posit-conf-2024/quarto-websites) | [website](https://posit-conf-2024.github.io/quarto-websites/)

### Shiny

- [**Martin J Frigaard** mjfrigaard/shinypak](https://github.com/mjfrigaard/shinyap) | [website](https://mjfrigaard.github.io/shinypak/)
- [**Rami Krispin** RamiKrispin/shinylive-r](https://github.com/RamiKrispin/shinylive-r) | [website](https://ramikrispin.github.io/shinylive-r/)
- [**posit-dev** posit-dev/py-shiny-workshop](https://github.com/posit-dev/shiny-python-workshop-2023) | [website](https://posit-dev.github.io/py-shiny-workshop)
- [**posit-conf-2023** posit-conf-2023/shiny-r-intro](https://github.com/posit-conf-2023/shiny-r-intro) | [website](https://posit-conf-2023.github.io/shiny-r-intro/)
- [**posit-conf-2023** posit-conf-2023/shiny-r-ui](https://github.com/posit-conf-2023/shiny-r-ui) | [website](https://webdesign4shiny.rinterface.com)
- [**posit-conf-2023** posit-conf-2023/shiny-r-dashboard](https://github.com/posit-conf-2023/shiny-r-dashboard) | [website](https://posit-conf-2023.github.io/shiny-r-dashboard/)
- [**posit-conf-2023** posit-conf-2023/shiny-r-prod](https://github.com/posit-conf-2023/shiny-r-prod) | [website](https://posit-conf-2023.github.io/shiny-r-prod/)
- [**ThinkR** ThinkR-open/engineering-shiny-book](https://github.com/ThinkR-open/engineering-shiny-book) | [website](https://engineering-shiny.org)
- [**Ted Laderas** laderast/shinyowl](https://github.com/laderast/shinyowl/) | [website](https://laderast.github.io/shinyowl)
- [**posit-dev** posit-dev/intro-to-shiny-for-python](https://github.com/posit-dev/intro-to-shiny-for-python) | [website](https://posit-dev.github.io/intro-to-shiny-for-python/)
- [**posit::conf(2024)** posit-conf-2024/shiny-r-intro](https://github.com/posit-conf-2024/shiny-r-intro) | [website](https://posit-conf-2024.github.io/shiny-r-intro/)
- [**posit::conf(2024)** posit-conf-2024/level-up-shiny](https://github.com/posit-conf-2024/level-up-shiny) | [website](https://posit-conf-2024.github.io/level-up-shiny/)

### Julia

- [**Antonello Lobianco** sylvaticus/juliatutorial](https://github.com/sylvaticus/juliatutorial)
- [**JuliaAcademy** JuliaAcademy/JuliaTutorials](https://github.com/JuliaAcademy/JuliaTutorials) | [website](https://julialang.org/learning/)
- [**JuliaAcademy** JuliaAcademy/DataScience](https://github.com/JuliaAcademy/DataScience) | [website](https://juliaacademy.com/p/julia-for-data-science)
- [**JuliaAcademy** JuliaAcademy/Introduction-to-Julia](https://github.com/JuliaAcademy/Introduction-to-Julia) | [website](https://juliaacademy.com/p/intro-to-julia)
- [**JuliaAcademy** JuliaAcademy/JuliaProgrammingForNervousBeginners](https://github.com/JuliaAcademy/JuliaProgrammingForNervousBeginners) | [website](https://juliaacademy.com/p/julia-programming-for-nervous-beginners)
- [**JuliaAcademy** JuliaAcademy/DataFrames](https://github.com/JuliaAcademy/DataFrames)
- [**JuliaAcademy** JuliaAcademy/Foundations-of-Machine-Learning](https://github.com/JuliaAcademy/Foundations-of-Machine-Learning) | [website](https://juliaacademy.com/p/introduction-to-machine-learning)
- [**The Carpentries Incubator** carpentries-incubator/julia-novice](https://github.com/carpentries-incubator/julia-novice) | [website](https://carpentries-incubator.github.io/julia-novice)
- [**Antonello Lobianco** sylvaticus/SPMLJ](https://github.com/sylvaticus/SPMLJ) | [website](https://sylvaticus.github.io/SPMLJ/stable)
- [**Ben Lauwens** BenLauwens/ThinkJulia.jl](https://github.com/BenLauwens/ThinkJulia.jl)
- [**Claudia Solis-Lemus** crsl4/julia-workshop](https://github.com/crsl4/julia-workshop) | [website](https://crsl4.github.io/julia-workshop/)
- [**Samuel Omlin** omlins/julia-gpu-course](https://github.com/omlins/julia-gpu-course)

### Data visualization

- [**Bioinformatics, Rockefeller University** RockefellerUniversity/IGV_course](https://github.com/RockefellerUniversity/IGV_course) | [website](https://rockefelleruniversity.github.io/IGV_course/)
- [**Hadley Wickham** hadley/ggplot2-book](https://github.com/hadley/ggplot2-book) | [website](https://ggplot2-book.org)
- [**Christian Burkhart** ch-bu/ggplot2-fundamentals](https://github.com/ch-bu/ggplot2-fundamentals) | [website](https://ggplot2tor.com/courses/ggplot2fundamentals)
- [**The Carpentries Incubator** carpentries-incubator/intro-data-viz](https://github.com/carpentries-incubator/intro-data-viz) | [website](https://carpentries-incubator.github.io/intro-data-viz/)
- [**Teaching materials at the Harvard Chan Bioinformatics Core** hbctraining/publication_perfect](https://github.com/hbctraining/publication_perfect) | [website](https://hbctraining.github.io/publication_perfect/)
- [**C. Li** cxli233/FriendsDontLetFriends](https://github.com/cxli233/FriendsDontLetFriends)
- [**Claus Wilke** clauswilke/dataviz](https://github.com/clauswilke/dataviz) | [website](https://clauswilke.com/dataviz)
- [**Hands-On Data Visualization** HandsOnDataViz/book](https://github.com/handsondataviz/book) | [website](https://handsondataviz.org)
- [**Carson Sievert** cpsievert/plotly_book](https://github.com/cpsievert/plotly_book) | [website](https://plotly-r.com)
- [**Colin Diesh** cmdcolin/awesome-genome-visualization](https://github.com/cmdcolin/awesome-genome-visualization/ ) | [website](https://cmdcolin.github.io/awesome-genome-visualization/)
- [**UW Interactive Data Lab** uwdata/visualization-curriculum](https://github.com/uwdata/visualization-curriculum) | [website](https://idl.uw.edu/visualization-curriculum/)
- [**Fred Hutch Data Science Lab** fhdsl/better_plots](https://github.com/fhdsl/better_plots) | [website](https://hutchdatascience.org/better_plots)
- [**Kyran Dale** Kyrand/dataviz-with-python-and-js-ed-2](https://github.com/Kyrand/dataviz-with-python-and-js-ed-2)

### Java

- [**BioJava** biojava/biojava-tutorial](https://github.com/biojava/biojava-tutorial) | [website](http://www.biojava.org)

### GNU Make

- [**Software Carpentry** swcarpentry/make-novice](https://github.com/swcarpentry/make-novice) | [website](http://swcarpentry.github.io/make-novice)
- [**Chase Lambert** chaselambda/makefiletutorial](https://github.com/theicfire/makefiletutorial) | [website](http://makefiletutorial.com)

### MATLAB/Octave

- [**Software Carpentry** swcarpentry/matlab-novice-inflammation](https://github.com/swcarpentry/matlab-novice-inflammation) | [website](http://swcarpentry.github.io/matlab-novice-inflammation/)

### C/C++

- [**LiaBooks ... by LiaScript** LiaBooks/C-Programming](https://github.com/LiaBooks/C-Programming) | [website](https://liascript.github.io/course/)

### Rust

- [**Google** google/comprehensive-rust](https://github.com/google/comprehensive-rust) | [website](https://google.github.io/comprehensive-rust/)
- [**The Rust Programming Language** rust-lang/rustlings](https://github.com/rust-lang/rustlings) | [website](https://rustlings.cool)

### SPARQL

- [**SIB Swiss Institute of Bioinformatics** sib-swiss/sparql-training](https://github.com/sib-swiss/sparql-training)
- [**BiGCaT, Department of Translational Genomics** BiGCAT-UM/SPARQLTutorialBioSB2019](https://github.com/bigcat-um/SPARQLTutorialBioSB2019)

### LaTeX

- [**Fred Hutch Data Science Lab** fhdsl/Overleaf_and_LaTeX_for_Scientific_Articles](https://github.com/fhdsl/Overleaf_and_LaTeX_for_Scientific_Articles) | [website](https://hutchdatascience.org/Overleaf_and_LaTeX_for_Scientific_Articles/)

## Computational methods and pipelines


### Containerization

- [**awesome-workshop** awesome-workshop/docker-singularity-hats](https://github.com/awesome-workshop/docker-singularity-hats) | [website](https://awesome-workshop.github.io/docker-singularity-hats/index.html)
- [**The Carpentries Incubator** carpentries-incubator/docker-introduction](https://github.com/carpentries-incubator/docker-introduction) | [website](https://carpentries-incubator.github.io/docker-introduction/)
- [**The Carpentries Incubator** carpentries-incubator/singularity-introduction](https://github.com/carpentries-incubator/singularity-introduction) | [website](https://carpentries-incubator.github.io/singularity-introduction)
- [**SIB Swiss Institute of Bioinformatics** sib-swiss/containers-introduction-training](https://github.com/sib-swiss/containers-introduction-training) | [website](https://sib-swiss.github.io/containers-introduction-training/)
- [**PerMedCoE** PerMedCoE/mpi-in-container](https://github.com/permedcoe/mpi-in-container)
- [**Rami Krispin** RamiKrispin/Introduction-to-Docker](https://github.com/RamiKrispin/Introduction-to-Docker)

### Galaxy

- [**Erasmus Medical Center** ErasmusMC-Bioinformatics/galaxy-courses](https://github.com/ErasmusMC-Bioinformatics/galaxy-courses)
- [**Galaxy Project** galaxyproject/training-material](https://github.com/galaxyproject/training-material) | [website](https://training.galaxyproject.org)

### High performance computing

- [**The Carpentries Incubator** carpentries-incubator/hpc-intro](https://github.com/carpentries-incubator/hpc-intro) | [website](https://carpentries-incubator.github.io/hpc-intro/)
- [**ngs-docs** ngs-docs/2021-august-remote-computing](https://github.com/ngs-docs/2021-august-remote-computing) | [website](https://ngs-docs.github.io/2021-august-remote-computing)
- [**cambiotraining** cambiotraining/hpc-intro](https://github.com/cambiotraining/hpc-intro) | [website](https://cambiotraining.github.io/hpc-intro/)
- [**The Carpentries Incubator** carpentries-incubator/lesson-gpu-programming](https://github.com/carpentries-incubator/lesson-gpu-programming) | [website](https://carpentries-incubator.github.io/lesson-gpu-programming/)
- [**PerMedCoE** PerMedCoE/cluster-tutorial](https://github.com/permedcoe/cluster-tutorial)
- [**George G. Vega Yon** gvegayon/appliedhpcr](https://github.com/gvegayon/appliedhpcr)
- [**jhudsl** jhudsl/Computing_for_Cancer_Informatics](https://github.com/jhudsl/Computing_for_Cancer_Informatics) | [website](https://jhudatascience.org/Computing_for_Cancer_Informatics)

### Nextflow

- [**Sydney Informatics Hub** Sydney-Informatics-Hub/hello-nextflow](https://github.com/Sydney-Informatics-Hub/hello-nextflow) | [website](https://sydney-informatics-hub.github.io/hello-nextflow/)
- [**Sydney Informatics Hub** Sydney-Informatics-Hub/customising-nfcore-workshop](https://github.com/Sydney-Informatics-Hub/customising-nfcore-workshop) | [website](https://sydney-informatics-hub.github.io/customising-nfcore-workshop/)
- [**Firas Zemzem** Zemzemfiras1/nf-core-pre-hackathon_training2025](https://github.com/Zemzemfiras1/nf-core-pre-hackathon_training2025)

### Workflows

- [**Biocore@CRG** biocorecrg/CoursesCRG_Containers_Nextflow_May_2022](https://github.com/biocorecrg/CoursesCRG_Containers_Nextflow_May_2022) | [website](https://biocorecrg.github.io/CoursesCRG_Containers_Nextflow_May_2022/)
- [**Biocore@CRG** biocorecrg/ELIXIR_containers_nextflow](https://github.com/biocorecrg/ELIXIR_containers_nextflow) | [website](https://biocorecrg.github.io/ELIXIR_containers_nextflow/)
- [**Biocore@CRG** biocorecrg/SIB_course_nextflow_Nov_2021](https://github.com/biocorecrg/SIB_course_nextflow_Nov_2021) | [website](https://biocorecrg.github.io/SIB_course_nextflow_Nov_2021/docs/)
- [**Biodata Analysis Group** BiodataAnalysisGroup/intro-to-cwl-docker](https://github.com/BiodataAnalysisGroup/intro-to-cwl-docker) | [website](https://biodataanalysisgroup.github.io/intro-to-cwl-docker/)
- [**CRUK CI Bioinformatics Core** bioinformatics-core-shared-training/nextflow_september_2021](https://github.com/bioinformatics-core-shared-training/nextflow_september_2021)
- [**BovReg** BovReg/nf-workshop20](https://github.com/bovreg/nf-workshop20)
- [**The Carpentries Incubator** carpentries-incubator/snakemake-novice-bioinformatics](https://github.com/carpentries-incubator/snakemake-novice-bioinformatics) | [website](https://carpentries-incubator.github.io/snakemake-novice-bioinformatics)
- [**The Carpentries Incubator** carpentries-incubator/workflows-nextflow](https://github.com/carpentries-incubator/workflows-nextflow) | [website](https://carpentries-incubator.github.io/workflows-nextflow/)
- [**The Carpentries Incubator** carpentries-incubator/workflows-snakemake](https://github.com/carpentries-incubator/workflows-snakemake) | [website](https://carpentries-incubator.github.io/workflows-snakemake/)
- [**Sateesh_Peri** sateeshperi/nextflow_varcal](https://github.com/sateeshperi/nextflow_varcal) | [website](https://sateeshperi.github.io/nextflow_varcal/nextflow/)
- [**Seqera** nextflow-io/training](https://github.com/seqeralabs/nf-training-public) | [website](https://training.nextflow.io)
- [**VIB Technologies: Training material and software projects** vibbits/nextflow-workshop](https://github.com/vibbits/nextflow-workshop) | [website](https://liascript.github.io/course/)
- [**SIB Swiss Institute of Bioinformatics** sib-swiss/containers-snakemake-training](https://github.com/sib-swiss/containers-snakemake-training) | [website](https://sib-swiss.github.io/containers-snakemake-training/)
- [**The Carpentries Incubator** carpentries-incubator/cwl-novice-tutorial](https://github.com/carpentries-incubator/cwl-novice-tutorial) | [website](https://carpentries-incubator.github.io/cwl-novice-tutorial/)
- [**Romain Feron** RomainFeron/workshop-snakemake-sibdays2022](https://github.com/RomainFeron/workshop-snakemake-sibdays2022)
- [**Dockstore** dockstore/bcc2020-training](https://github.com/dockstore/bcc2020-training)
- [**Applied Genomics** Applied-Genomics-UTD/docs](https://github.com/Applied-Genomics-UTD/docs)
- [**Fred Hutch Data Science Lab** fhdsl/GitHub_Automation_for_Scientists](https://github.com/fhdsl/GitHub_Automation_for_Scientists) | [website](http://hutchdatascience.org/GitHub_Automation_for_Scientists/)

### Image analysis

- [**Andrew Jahn** andrewjahn/AndysBrainBook](https://github.com/andrewjahn/AndysBrainBook)
- [**The Carpentries Incubator** carpentries-incubator/SDC-BIDS-fMRI](https://github.com/carpentries-incubator/SDC-BIDS-fMRI) | [website](https://carpentries-incubator.github.io/SDC-BIDS-fMRI/)
- [**The Carpentries Incubator** carpentries-incubator/SDC-BIDS-IntroMRI](https://github.com/carpentries-incubator/SDC-BIDS-IntroMRI) | [website](https://carpentries-incubator.github.io/SDC-BIDS-IntroMRI)
- [**The Carpentries Incubator** carpentries-incubator/SDC-BIDS-sMRI](https://github.com/carpentries-incubator/SDC-BIDS-sMRI) | [website](https://carpentries-incubator.github.io/SDC-BIDS-sMRI/)
- [**The Carpentries Incubator** carpentries-incubator/SDC-BIDS-dMRI](https://github.com/carpentries-incubator/SDC-BIDS-dMRI) | [website](https://carpentries-incubator.github.io/SDC-BIDS-dMRI/)
- [**Data Carpentry** datacarpentry/image-processing](https://github.com/datacarpentry/image-processing) | [website](https://datacarpentry.org/image-processing)
- [**Dominic Waithe** dwaithe/model-training](https://github.com/dwaithe/model-training)
- [**NEUBIAS** NEUBIAS/training-resources](https://github.com/NEUBIAS/training-resources) | [website](https://neubias.github.io/training-resources)
- [**napari** napari/napari-workshop-template](https://github.com/napari/napari-workshop-template) | [website](https://napari.org/napari-workshop-template)
- [**Kyle I S Harrington** kephale/napari-workshop-mandm-2023](https://github.com/kephale/napari-workshop-mandm-2023)
- [**Chan Zuckerberg Initiative** chanzuckerberg/napari-segmentation-workshop](https://github.com/chanzuckerberg/napari-segmentation-workshop) | [website](https://chanzuckerberg.github.io/napari-segmentation-workshop/)

### Cloud computing

- [**Data Carpentry** datacarpentry/cloud-genomics](https://github.com/datacarpentry/cloud-genomics) | [website](https://datacarpentry.org/cloud-genomics/)
- [**AWS Samples** aws-samples/aws-hpc-tutorials](https://github.com/aws-samples/aws-hpc-tutorials) | [website](https://hpcworkshops.com)
- [**Eija Korpelainen** ekorpela/cloud-vm-workshop](https://github.com/ekorpela/cloud-vm-workshop/tree/master/materials)
- [**Lynn Langit** lynnlangit/gcp-for-bioinformatics](https://github.com/lynnlangit/gcp-for-bioinformatics) | [website](https://www.youtube.com/playlist?list=PL4Q4HssKcxYvcixWS08UFaYIH7y4IAV0z)

### Data mining

- [**SIB Swiss Institute of Bioinformatics** sib-swiss/SPARQL_course](https://github.com/sib-swiss/SPARQL_course)

## Omics analysis


### Genomics

- [**Canadian Bioinformatics Workshops** bioinformatics-ca/CAN_2021](https://github.com/bioinformatics-ca/CAN_2021)
- [**Canadian Bioinformatics Workshops** bioinformatics-ca/HTG_2021](https://github.com/bioinformatics-ca/HTG_2021)
- [**Papenfuss Lab** PapenfussLab/IntroductionToGenomicsWorkshop](https://github.com/PapenfussLab/IntroductionToGenomicsWorkshop)
- [**Computational Metagenomics** metagenomics/denbi-nanopore-training](https://github.com/metagenomics/denbi-nanopore-training)
- [**Computational Genomics with R** compgenomr/book](https://github.com/compgenomr/book) | [website](http://compgenomr.github.io/book)
- [**Wellcome Connecting Science** WCSCourses/SARS-COV-2_B4B](https://github.com/WCSCourses/SARS-COV-2_B4B) | [website](https://wcscourses.github.io/SARS-COV-2_B4B/)
- [**Functional Genomics Laboratory** Functional-Genomics-Lab/Applied-Genomics](https://github.com/Functional-Genomics-Lab/Applied-Genomics) | [website](https://functional-genomics-lab.github.io/Applied-Genomics/)
- [**cambiotraining** cambiotraining/sars-cov-2-genomics](https://github.com/cambiotraining/sars-cov-2-genomics) | [website](http://cambiotraining.github.io/sars-cov-2-genomics/)
- [**Data Carpentry** datacarpentry/genomics-workshop](https://github.com/datacarpentry/genomics-workshop) | [website](https://datacarpentry.org/genomics-workshop)
- [**Data Carpentry** datacarpentry/organization-genomics](https://github.com/datacarpentry/organization-genomics) | [website](https://datacarpentry.org/organization-genomics)
- [**The Gulbenkian Training Programme in Bioinformatics** GTPB/ELB19F](https://github.com/gtpb/ELB19F) | [website](https://gtpb.github.io/ELB19F/)
- [**The McDonnell Genome Institute** genome/bfx-workshop](https://github.com/genome/bfx-workshop)
- [**rapidspeciation** rapidspeciation/biodiversity_genomics_course](https://github.com/rapidspeciation/biodiversity_genomics_course)
- [**Fred Hutch Data Science Lab** fhdsl/Choosing_Genomics_Tools](https://github.com/fhdsl/Choosing_Genomics_Tools) | [website](http://hutchdatascience.org/Choosing_Genomics_Tools/)
- [**Raphael Mourad** raphaelmourad/LLM-for-genomics-training](https://github.com/raphaelmourad/LLM-for-genomics-training)

### Next generation sequencing

- [**CRUK CI Bioinformatics Core** bioinformatics-core-shared-training/cruk-summer-school-2020](https://github.com/bioinformatics-core-shared-training/cruk-summer-school-2020) | [website](https://bioinformatics-core-shared-training.github.io/cruk-summer-school-2020/ )
- [**Data Carpentry** datacarpentry/wrangling-genomics](https://github.com/datacarpentry/wrangling-genomics) | [website](https://datacarpentry.org/wrangling-genomics/)
- [**Teaching materials at the Harvard Chan Bioinformatics Core** hbctraining/Accessing_public_genomic_data](https://github.com/hbctraining/Accessing_public_genomic_data) | [website](https://hbctraining.github.io/Accessing_public_genomic_data)
- [**SIB Swiss Institute of Bioinformatics** sib-swiss/NGS-introduction-training](https://github.com/sib-swiss/NGS-introduction-training) | [website](https://sib-swiss.github.io/NGS-introduction-training/)
- [**SIB Swiss Institute of Bioinformatics** sib-swiss/NGS-variants-training](https://github.com/sib-swiss/NGS-variants-training) | [website](https://sib-swiss.github.io/NGS-variants-training/)
- [**Waldron Lab at the CUNY SPH** waldronlab/CNVWorkshop](https://github.com/waldronlab/CNVWorkshop) | [website](https://waldronlab.io/CNVWorkshop)
- [**The Griffith Lab** griffithlab/pmbio.org](https://github.com/griffithlab/pmbio.org) | [website](http://pmbio.org)
- [**NBIS - National Bioinformatics Infrastructure Sweden** NBISweden/workshop-ngsintro](https://github.com/NBISweden/workshop-ngsintro) | [website](https://NBISweden.github.io/workshop-ngsintro)
- [**Institut Français de Bioinformatique (IFB)** IFB-ElixirFr/EBAII](https://github.com/IFB-ElixirFr/EBAII) | [website](https://ifb-elixirfr.github.io/EBAII/)
- [**Cloud-SPAN** Cloud-SPAN/00genomics](https://github.com/cloud-span/00genomics) | [website](https://cloud-span.github.io/00genomics/)
- [**NBIS - National Bioinformatics Infrastructure Sweden** NBISweden/workshop-ngsintro](https://github.com/nbisweden/workshop-ngsintro/) | [website](https://NBISweden.github.io/workshop-ngsintro)

### Transcriptomics

- [**Biocore@CRG** biocorecrg/RNAseq_course_2019](https://github.com/biocorecrg/RNAseq_course_2019) | [website](https://biocorecrg.github.io/RNAseq_course_2019/)
- [**Canadian Bioinformatics Workshops** bioinformatics-ca/RNA_2021](https://github.com/bioinformatics-ca/RNA_2021)
- [**CRUK CI Bioinformatics Core** bioinformatics-core-shared-training/Bulk_RNASeq_Course_Nov21](https://github.com/bioinformatics-core-shared-training/Bulk_RNASeq_Course_Nov21) | [website](https://bioinformatics-core-shared-training.github.io/Bulk_RNASeq_Course_Nov21/)
- [**The Carpentries Incubator** carpentries-incubator/bioc-rnaseq](https://github.com/carpentries-incubator/bioc-rnaseq) | [website](https://carpentries-incubator.github.io/bioc-rnaseq)
- [**Teaching materials at the Harvard Chan Bioinformatics Core** hbctraining/Intro-to-DGE](https://github.com/hbctraining/DGE_workshop_salmon_online) | [website](https://hbctraining.github.io/Intro-to-DGE/)
- [**Teaching materials at the Harvard Chan Bioinformatics Core** hbctraining/Intro-to-bulk-RNAseq](https://github.com/hbctraining/Intro-to-rnaseq-hpc-salmon-flipped) | [website](https://hbctraining.github.io/Intro-to-bulk-RNAseq/)
- [**SIB Swiss Institute of Bioinformatics** sib-swiss/RNAseq-introduction-training](https://github.com/sib-swiss/RNAseq-introduction-training) | [website](https://sib-swiss.github.io/RNAseq-introduction-training/)
- [**Stefano Mangiola** stemangiola/bioc_2020_tidytranscriptomics](https://github.com/stemangiola/bioc_2020_tidytranscriptomics) | [website](https://stemangiola.github.io/bioc_2020_tidytranscriptomics/)
- [**Xueyi Dong** XueyiDong/RNAseq123workshop](https://github.com/XueyiDong/RNAseq123workshop)
- [**Amarinder Singh Thind** amarinderthind/RNA-seq-tutorial-for-gene-differential-expression-analysis](https://github.com/amarinderthind/RNA-seq-tutorial-for-gene-differential-expression-analysis)
- [**CRUK CI Bioinformatics Core** bioinformatics-core-shared-training/Bulk_RNASeq_Course_March23](https://github.com/bioinformatics-core-shared-training/Bulk_RNASeq_Course_March23) | [website](https://bioinformatics-core-shared-training.github.io/Bulk_RNASeq_Course_March23/)
- [**NBIS - National Bioinformatics Infrastructure Sweden** NBISweden/workshop-RNAseq](https://github.com/NBISweden/workshop-RNAseq) | [website](https://NBISweden.github.io/workshop-RNAseq)
- [**Health Data Science Sandbox** hds-sandbox/bulk_RNAseq_course](https://github.com/hds-sandbox/bulk_RNAseq_course) | [website](https://hds-sandbox.github.io/bulk_RNAseq_course/)
- [**Computational Biology and Bioinformatics at UCLouvain** UCLouvain-CBIO/WSBIM2122](https://github.com/UCLouvain-CBIO/WSBIM2122) | [website](https://uclouvain-cbio.github.io/WSBIM2122/)
- [**Saez Lab** saezlab/transcriptutorial](https://github.com/saezlab/transcriptutorial) | [website](https://saezlab.github.io/transcriptutorial/)
- [**The Gulbenkian Training Programme in Bioinformatics** GTPB/ADER19F](https://github.com/gtpb/ADER19F) | [website](http://gtpb.github.io/ADER19F)
- [**Khushbu Patel** kpatel427/YouTubeTutorials](https://github.com/kpatel427/YouTubeTutorials)
- [**BrainOmicsCourse** BrainOmicsCourse/BrainOmics2024](https://github.com/BrainOmicsCourse/BrainOmics2024)

### RNA-seq

- [**Teaching materials at the Harvard Chan Bioinformatics Core** hbctraining/BBS230B_2023](https://github.com/hbctraining/BBS230B_2023) | [website](https://hbctraining.github.io/BBS230B_2023/)
- [**Teaching materials at the Harvard Chan Bioinformatics Core** hbctraining/rnaseq-cb321](https://github.com/hbctraining/rnaseq-cb321)
- [**Teaching materials at the Harvard Chan Bioinformatics Core** hbctraining/RNA-seq-CB321qc_2022](https://github.com/hbctraining/RNA-seq-CB321qc_2022)
- [**Teaching materials at the Harvard Chan Bioinformatics Core** hbctraining/rnaseq_overview](https://github.com/hbctraining/rnaseq_overview)
- [**UC Davis Bioinformatics Core Training Page** ucdavis-bioinformatics-training/2023-June-RNA-Seq-Analysis](https://github.com/ucdavis-bioinformatics-training/2023-June-RNA-Seq-Analysis)
- [**bioinformatics.ca** bioinformaticsdotca/RNA_2023](https://github.com/bioinformaticsdotca/RNA_2023)
- [**bioinformatics.ca** bioinformaticsdotca/PNA_2023](https://github.com/bioinformaticsdotca/PNA_2023)
- [**The Griffith Lab** griffithlab/rnabio.org](https://github.com/griffithlab/rnabio.org) | [website](http://rnabio.org)
- [**Sydney Informatics Hub** Sydney-Informatics-Hub/rnaseq-workshop-2023](https://github.com/Sydney-Informatics-Hub/rnaseq-workshop-2023) | [website](https://sydney-informatics-hub.github.io/rnaseq-workshop-2023/)

### Single-cell sequencing

- [**Aedin Culhane** aedin/scRNAseqBasicWorkflow](https://github.com/aedin/scRNAseqBasicWorkflow)
- [**CRUK CI Bioinformatics Core** bioinformatics-core-shared-training/UnivCambridge_ScRnaSeq_Nov2021](https://github.com/bioinformatics-core-shared-training/UnivCambridge_ScRnaSeq_Nov2021) | [website](http://bioinformatics-core-shared-training.github.io/UnivCambridge_ScRnaSeq_Nov2021)
- [**fmicompbio** fmicompbio/adv_scrnaseq_2020](https://github.com/fmicompbio/adv_scrnaseq_2020)
- [**Teaching materials at the Harvard Chan Bioinformatics Core** hbctraining/Intro-to-scRNAseq](https://github.com/hbctraining/scRNA-seq_online) | [website](https://hbctraining.github.io/Intro-to-scRNAseq/)
- [**Kelly Street** kstreet13/bioc2020trajectories](https://github.com/kstreet13/bioc2020trajectories) | [website](https://kstreet13.github.io/bioc2020trajectories/)
- [**Leiden Computational Biology Center** LeidenCBC/MGC-BioSB-SingleCellAnalysis2021](https://github.com/LeidenCBC/MGC-BioSB-SingleCellAnalysis2021)
- [**Martin Morgan** mtmorgan/HCABiocTraining](https://github.com/mtmorgan/HCABiocTraining) | [website](https://mtmorgan.github.io/HCABiocTraining/)
- [**NBIS - National Bioinformatics Infrastructure Sweden** NBISweden/excelerate-scRNAseq](https://github.com/NBISweden/excelerate-scRNAseq) | [website](https://nbisweden.github.io/excelerate-scRNAseq/)
- [**NBIS - National Bioinformatics Infrastructure Sweden** NBISweden/single-cell_sib_scilifelab_2021](https://github.com/NBISweden/single-cell_sib_scilifelab_2021)
- [**NBIS - National Bioinformatics Infrastructure Sweden** NBISweden/workshop-scRNAseq](https://github.com/nbisweden/workshop-scRNAseq) | [website](https://nbisweden.github.io/workshop-scRNAseq/)
- [**SIB Swiss Institute of Bioinformatics** sib-swiss/single-cell-training](https://github.com/sib-swiss/single-cell-training) | [website](https://sib-swiss.github.io/single-cell-training/)
- [**Tidy-transcriptomics workshops** tidytranscriptomics-workshops/bioc2022_tidytranscriptomics](https://github.com/tidytranscriptomics-workshops/bioc2022_tidytranscriptomics) | [website](https://tidytranscriptomics-workshops.github.io/bioc2022_tidytranscriptomics/index.html)
- [**Yunshun Chen** yunshun/SingleCellWorkshop](https://github.com/yunshun/SingleCellWorkshop)
- [**Cellular Genetics Informatics** cellgeni/scRNA.seq.course](https://github.com/cellgeni/scRNA.seq.course) | [website](https://scrnaseq-course.cog.sanger.ac.uk/website/index.html)
- [**CRUK CI Bioinformatics Core** bioinformatics-core-shared-training/SingleCell_RNASeq_Jan23](https://github.com/bioinformatics-core-shared-training/SingleCell_RNASeq_Jan23) | [website](https://bioinformatics-core-shared-training.github.io/SingleCell_RNASeq_Jan23/)
- [**OSCA Source Code Management** OSCA-source/OSCA](https://github.com/OSCA-source/OSCA) | [website](https://bioconductor.org/checkResults/devel/books-LATEST/OSCA)
- [**The Carpentries Incubator** carpentries-incubator/scrna-seq-analysis](https://github.com/carpentries-incubator/scrna-seq-analysis) | [website](https://carpentries-incubator.github.io/scrna-seq-analysis/)
- [**Bioconductor** Bioconductor/ISMB.OSCA](https://github.com/Bioconductor/ISMB.OSCA) | [website](https://bioconductor.github.io/ISMB.OSCA/)
- [**Theis Lab** theislab/single-cell-best-practices](https://github.com/theislab/single-cell-best-practices) | [website](https://www.sc-best-practices.org)
- [**Health Data Science Sandbox** hds-sandbox/scRNASeq_course](https://github.com/hds-sandbox/scRNASeq_course) | [website](https://hds-sandbox.github.io/scRNASeq_course/)
- [**Broad Institute** broadinstitute/2020_scWorkshop](https://github.com/broadinstitute/2020_scWorkshop) | [website](https://broadinstitute.github.io/2020_scWorkshop/)
- [**Rhonda Bacher** rhondabacher/ISMB2019_SingleCellTutorial](https://github.com/rhondabacher/ISMB2019_SingleCellTutorial)
- [**UC Davis Bioinformatics Core Training Page** ucdavis-bioinformatics-training/2023-December-Single-Cell-RNA-Seq-Analysis](https://github.com/ucdavis-bioinformatics-training/2023-December-Single-Cell-RNA-Seq-Analysis)
- [**UC Davis Bioinformatics Core Training Page** ucdavis-bioinformatics-training/2023-June-Single-Cell-RNA-Seq-Analysis](https://github.com/ucdavis-bioinformatics-training/2023-June-Single-Cell-RNA-Seq-Analysis)
- [**UC Davis Bioinformatics Core Training Page** ucdavis-bioinformatics-training/2023-June-Advanced-Topics-in-Single-Cell-RNA-Seq-VDJ](https://github.com/ucdavis-bioinformatics-training/2023-June-Advanced-Topics-in-Single-Cell-RNA-Seq-VDJ)
- [**UC Davis Bioinformatics Core Training Page** ucdavis-bioinformatics-training/2020-Advanced_Single_Cell_RNA_Seq](https://github.com/ucdavis-bioinformatics-training/2020-Advanced_Single_Cell_RNA_Seq)
- [**UC Davis Bioinformatics Core Training Page** ucdavis-bioinformatics-training/2022-July-Advanced-Topics-in-Single-Cell-RNA-Seq-ATAC](https://github.com/ucdavis-bioinformatics-training/2022-July-Advanced-Topics-in-Single-Cell-RNA-Seq-ATAC)
- [**UC Davis Bioinformatics Core Training Page** ucdavis-bioinformatics-training/2021-August-Advanced-Topics-in-Single-Cell-RNA-Seq-Trajectory-and-Velocity](https://github.com/ucdavis-bioinformatics-training/2021-August-Advanced-Topics-in-Single-Cell-RNA-Seq-Trajectory-and-Velocity)
- [**bioinformatics.ca** bioinformaticsdotca/scRNA_2023](https://github.com/bioinformaticsdotca/scRNA_2023)
- [**Theis Lab** theislab/single-cell-tutorial](https://github.com/theislab/single-cell-tutorial)
- [**PAIR code** PAIR-code/understanding-umap](https://github.com/PAIR-code/understanding-umap) | [website](https://pair-code.github.io/understanding-umap)
- [**scverse** scverse/scverse-tutorials](https://github.com/scverse/scverse-tutorials) | [website](https://scverse-tutorials.readthedocs.io/en/latest/)
- [**CDSB** ComunidadBioInfo/cdsb2021_scRNAseq](https://github.com/comunidadbioinfo/cdsb2021_scRNAseq/) | [website](https://comunidadbioinfo.github.io/cdsb2021_scRNAseq/)
- [**Leiden Computational Biology Center** LeidenCBC/MGC-BioSB-SingleCellAnalysis2022](https://github.com/LeidenCBC/MGC-BioSB-SingleCellAnalysis2022)
- [**CRUK CI Bioinformatics Core** bioinformatics-core-shared-training/SingleCell_RNASeq_May23](https://github.com/bioinformatics-core-shared-training/SingleCell_RNASeq_May23) | [website](https://bioinformatics-core-shared-training.github.io/SingleCell_RNASeq_May23/)
- [**Alex's Lemonade Stand Foundation** AlexsLemonade/2023-june-training](https://github.com/alexslemonade/2023-june-training/)
- [**Alex's Lemonade Stand Foundation** AlexsLemonade/2023-march-training](https://github.com/alexslemonade/2023-march-training/)
- [**SIB Swiss Institute of Bioinformatics** sib-swiss/single-cell-python-training](https://github.com/sib-swiss/single-cell-python-training/) | [website](https://sib-swiss.github.io/single-cell-python-training/)

### Variant analysis

- [**Andries Marees** MareesAT/GWA_tutorial](https://github.com/MareesAT/GWA_tutorial)
- [**Teaching materials at the Harvard Chan Bioinformatics Core** hbctraining/Intro-to-variant-analysis](https://github.com/hbctraining/variant_analysis) | [website](https://hbctraining.github.io/Intro-to-variant-analysis/)
- [**NBIS - National Bioinformatics Infrastructure Sweden** NBISweden/workshop-pgip](https://github.com/NBISweden/workshop-pgip) | [website](https://nbisweden.github.io/workshop-pgip/)
- [**UC Davis Bioinformatics Core Training Page** ucdavis-bioinformatics-training/2020-Variant_Analysis_Workshop](https://github.com/ucdavis-bioinformatics-training/2020-Variant_Analysis_Workshop)
- [**UC Davis Bioinformatics Core Training Page** ucdavis-bioinformatics-training/2021-July-Genome-Wide-Association-Studies](https://github.com/ucdavis-bioinformatics-training/2021-July-Genome-Wide-Association-Studies)
- [**Nina Overgaard Therkildsen** nt246/lcwgs-guide-tutorial](https://github.com/nt246/lcwgs-guide-tutorial)
- [**Dipannita Ghosh** digo4/Clinical-Genomics](https://github.com/digo4/Clinical-Genomics)
- [**SIB Swiss Institute of Bioinformatics** sib-swiss/cancer-variants-training](https://github.com/sib-swiss/cancer-variants-training) | [website](https://sib-swiss.github.io/cancer-variants-training/)

### ChIP-seq

- [**CRUK CI Bioinformatics Core** bioinformatics-core-shared-training/Quantitative-ChIPseq-Workshop](https://github.com/bioinformatics-core-shared-training/Quantitative-ChIPseq-Workshop)
- [**Teaching materials at the Harvard Chan Bioinformatics Core** hbctraining/Intro-to-ChIPseq](https://github.com/hbctraining/Intro-to-ChIPseq) | [website](https://hbctraining.github.io/Intro-to-ChIPseq/)
- [**Kai Hu** hukai916/IntegratedChIPseqWorkshop](https://github.com/hukai916/IntegratedChIPseqWorkshop)
- [**Teaching materials at the Harvard Chan Bioinformatics Core** hbctraining/Investigating-chromatin-biology-ChIPseq](https://github.com/hbctraining/Intro-to-ChIPseq-flipped) | [website](https://hbctraining.github.io/Investigating-chromatin-biology-ChIPseq/)
- [**Teaching materials at the Harvard Chan Bioinformatics Core** hbctraining/Intro-to-peak-analysis](https://github.com/hbctraining/Peak_analysis_workshop) | [website](https://hbctraining.github.io/Intro-to-peak-analysis/)
- [**Denis Puthier** dputhier/EBA_2015_ChIP-Seq](https://github.com/dputhier/EBA_2015_ChIP-Seq)

### Comparative genomics

- [**Steven M. Van Belleghem** StevenVB12/stevenvb12.github.io](https://github.com/StevenVB12/stevenvb12.github.io)
- [**The Gulbenkian Training Programme in Bioinformatics** GTPB/CPANG19](https://github.com/gtpb/CPANG19) | [website](https://gtpb.github.io/CPANG19/)

### Epigenetics

- [**Haibo Liu** haibol2016/ATACseqQCWorkshop](https://github.com/haibol2016/ATACseqQCWorkshop)
- [**bioinformatics.ca** bioinformaticsdotca/EPI_2023](https://github.com/bioinformaticsdotca/EPI_2023)
- [**UC Davis Bioinformatics Core Training Page** ucdavis-bioinformatics-training/2020-Epigenetics_Workshop](https://github.com/ucdavis-bioinformatics-training/2020-Epigenetics_Workshop)
- [**NBIS - National Bioinformatics Infrastructure Sweden** NBISweden/workshop-epigenomics-RTDs](https://github.com/NBISweden/workshop-epigenomics-RTDs) | [website](https://nbis-workshop-epigenomics.readthedocs.io/en/latest/)

### Genome annotation

- [**Katharina Hoff** KatharinaHoff/BRAKER-TSEBRA-Workshop](https://github.com/KatharinaHoff/BRAKER-TSEBRA-Workshop)

### Genome assembly

- [**UC Davis Bioinformatics Core Training Page** ucdavis-bioinformatics-training/2020-Genome_Assembly_Workshop](https://github.com/ucdavis-bioinformatics-training/2020-Genome_Assembly_Workshop)
- [**ebp-nor** ebp-nor/genome-assembly-workshop-2023](https://github.com/ebp-nor/genome-assembly-workshop-2023)

### Metagenomics

- [**Canadian Bioinformatics Workshops** bioinformatics-ca/MIC_2021](https://github.com/bioinformatics-ca/MIC_2021)
- [**Matteo Calgaro** mcalgaro93/benchdamicWorkshop](https://github.com/mcalgaro93/benchdamicWorkshop)
- [**Waldron Lab at the CUNY SPH** waldronlab/curatedMetagenomicDataAnalyses](https://github.com/waldronlab/curatedMetagenomicDataAnalyses) | [website](https://waldronlab.io/curatedMetagenomicDataAnalyses/)
- [**The Carpentries Lab** carpentries-lab/metagenomics-workshop](https://github.com/carpentries-lab/metagenomics-workshop) | [website](https://carpentries-lab.github.io/metagenomics-workshop/)
- [**The Carpentries Lab** carpentries-lab/metagenomics-organization](https://github.com/carpentries-lab/metagenomics-organization) | [website](https://carpentries-lab.github.io/metagenomics-organization/)
- [**The Carpentries Lab** carpentries-lab/metagenomics-analysis](https://github.com/carpentries-lab/metagenomics-analysis) | [website](https://carpentries-lab.github.io/metagenomics-analysis/)
- [**The Carpentries Lab** carpentries-lab/metagenomics-R](https://github.com/carpentries-lab/metagenomics-R) | [website](https://carpentries-lab.github.io/metagenomics-R/)
- [**UC Davis Bioinformatics Core Training Page** ucdavis-bioinformatics-training/2021-May-Microbial-Community-Analysis](https://github.com/ucdavis-bioinformatics-training/2021-May-Microbial-Community-Analysis)
- [**bioinformatics.ca** bioinformaticsdotca/MIC_2023](https://github.com/bioinformaticsdotca/MIC_2023)
- [**bioinformatics.ca** bioinformaticsdotca/MIC_2022](https://github.com/bioinformaticsdotca/MIC_2022)
- [**bioinformatics.ca** bioinformaticsdotca/AMB_2024](https://github.com/bioinformaticsdotca/AMB_2024)

### Epidemiology

- [**Canadian Bioinformatics Workshops** bioinformatics-ca/EPI_2021](https://github.com/bioinformatics-ca/EPI_2021)
- [**Canadian Bioinformatics Workshops** bioinformatics-ca/IDE_2021](https://github.com/bioinformatics-ca/IDE_2021)
- [**Chloe Mirzayi** cmirzayi/EpiForBioWorkshop2020](https://github.com/cmirzayi/EpiForBioWorkshop2020) | [website](https://cmirzayi.github.io/EpiForBioWorkshop2020/)
- [**bioinformatics.ca** bioinformaticsdotca/IDE_2023](https://github.com/bioinformaticsdotca/IDE_2023)
- [**bioinformatics.ca** bioinformaticsdotca/IDE_2024](https://github.com/bioinformaticsdotca/IDE_2024)
- [**Alli Black** alliblk/genepi-book](https://github.com/alliblk/genepi-book) | [website](https://alliblk.github.io/genepi-book/)

### Microbiology

- [**bioinformatics.ca** bioinformaticsdotca/BMB_2024](https://github.com/bioinformaticsdotca/BMB_2024)

### Multiomics

- [**Waldron Lab at the CUNY SPH** waldronlab/MultiAssayWorkshop](https://github.com/waldronlab/MultiAssayWorkshop) | [website](https://waldronlab.github.io/MultiAssayWorkshop)
- [**SIB Swiss Institute of Bioinformatics** sib-swiss/multiomics-data-analysis-and-integration-training](https://github.com/sib-swiss/multiomics-data-analysis-and-integration-training)

### Spatial transcriptomics

- [**Davis Laboratory** DavisLaboratory/GeoMXAnalysisWorkflow](https://github.com/DavisLaboratory/GeoMXAnalysisWorkflow) | [website](https://davislaboratory.github.io/GeoMXAnalysisWorkflow/)
- [**dario righelli** drighelli/SpatialExperiment_Bioc2021](https://github.com/drighelli/SpatialExperiment_Bioc2021)
- [**Integrative Computational Biology and Multiomics Research Group** ncl-icbam/ismb-tutorial-2023](https://github.com/ncl-icbam/ismb-tutorial-2023)
- [**Sydney Precision Data Science Centre** SydneyBioX/StatialBioc2023](https://github.com/SydneyBioX/StatialBioc2023) | [website](https://SydneyBioX.github.io/StatialBioc2023/)
- [**UC Davis Bioinformatics Core Training Page** ucdavis-bioinformatics-training/2022-December-Spatial-Transcriptomics](https://github.com/ucdavis-bioinformatics-training/2022-December-Spatial-Transcriptomics)
- [**Lukas Weber** lmweber/BestPracticesST](https://github.com/lmweber/BestPracticesST) | [website](https://lmweber.org/PrinciplesSTA/)
- [**NBIS - National Bioinformatics Infrastructure Sweden** NBISweden/workshop-spatial](https://github.com/NBISweden/workshop-spatial)
- [**SIB Swiss Institute of Bioinformatics** sib-swiss/spatial-transcriptomics-training](https://github.com/sib-swiss/spatial-transcriptomics-training/) | [website](https://sib-swiss.github.io/spatial-transcriptomics-training/)
- [**ELIXIR Europe Training** elixir-europe-training/ELIXIR-SCO-spatial-omics](https://github.com/elixir-europe-training/ELIXIR-SCO-spatial-omics) | [website](https://elixir-europe-training.github.io/ELIXIR-SCO-spatial-omics/)
- [**Lukas Weber** lmweber/OSTA](https://github.com/lmweber/OSTA) | [website](https://lmweber.org/OSTA/)
- [**Estella Yixing Dong** estellad/BC2_Spatial_Transcriptomics](https://github.com/estellad/BC2_Spatial_Transcriptomics)
- [**Estella Yixing Dong** estellad/BC2_Spatial_Transcriptomics](https://github.com/estellad/BC2_Spatial_Transcriptomics)

### Long read sequencing

- [**SIB Swiss Institute of Bioinformatics** sib-swiss/NGS-longreads-training](https://github.com/sib-swiss/NGS-longreads-training) | [website](https://sib-swiss.github.io/NGS-longreads-training/)
- [**UC Davis Bioinformatics Core Training Page** ucdavis-bioinformatics-training/2021-August-Iso-Seq](https://github.com/ucdavis-bioinformatics-training/2021-August-Iso-Seq)
- [**Ryan Wick** rrwick/Perfect-bacterial-genome-tutorial](https://github.com/rrwick/Perfect-bacterial-genome-tutorial)
- [**Tim Kahlke** timkahlke/LongRead_tutorials](https://github.com/timkahlke/LongRead_tutorials/)
- [**Nanopore for Educators** nanoporenetwork/ebook-website](https://github.com/nanoporenetwork/ebook-website)

### Metabolomics

- [**bioinformatics.ca** bioinformaticsdotca/MET_2023](https://github.com/bioinformaticsdotca/MET_2023)

### Proteomics

- [**Computational Biology and Bioinformatics at UCLouvain** UCLouvain-CBIO/LSTAT2340](https://github.com/UCLouvain-CBIO/LSTAT2340) | [website](https://uclouvain-cbio.github.io/LSTAT2340/)
- [**Health Data Science Sandbox** hds-sandbox/proteomics-sandbox](https://github.com/hds-sandbox/proteomics-sandbox) | [website](https://hds-sandbox.github.io/proteomics-sandbox/index.html)
- [**statOmics** statOmics/PDA](https://github.com/statomics/PDA)
- [**The Gulbenkian Training Programme in Bioinformatics** GTPB/IBIP19](https://github.com/gtpb/IBIP19) | [website](https://gtpb.github.io/IBIP19/)
- [**The Gulbenkian Training Programme in Bioinformatics** GTPB/PDA19](https://github.com/gtpb/PDA19) | [website](https://gtpb.github.io/PDA19/)
- [**PickyBinders** PickyBinders/geometric-learning-protein-structures-course](https://github.com/PickyBinders/geometric-learning-protein-structures-course)

### Pathways and Networks

- [**Canadian Bioinformatics Workshops** bioinformatics-ca/PNA_2021](https://github.com/bioinformatics-ca/PNA_2021)
- [**Susan** Coort/tutorial-network-data](https://gitlab.com/Coort/tutorial-network-data)
- [**LaurenDupuis** LaurenDupuis/EJP-RD_Helis_Academy](https://github.com/laurendupuis/EJP-RD_Helis_Academy)

### Protein structure

- [**Gray Lab** Graylab/DL4Proteins-notebooks](https://github.com/Graylab/DL4Proteins-notebooks)

## Reproducibility and data management


### Data management

- [**CRUK CI Bioinformatics Core** bioinformatics-core-shared-training/Managing-your-research-data](https://github.com/bioinformatics-core-shared-training/Managing-your-research-data) | [website](https://bioinformatics-core-shared-training.github.io/Managing-your-research-data/)
- [**The Carpentries Incubator** carpentries-incubator/capstone-novice-spreadsheet-biblio](https://github.com/carpentries-incubator/capstone-novice-spreadsheet-biblio) | [website](http://carpentries-incubator.github.io/capstone-novice-spreadsheet-biblio/)
- [**ELIXIR Belgium** ELIXIR-Belgium/rdm-guide](https://github.com/ELIXIR-Belgium/rdm-guide) | [website](https://rdm.elixir-belgium.org)
- [**ELIXIR Europe** elixir-europe/rdmkit](https://github.com/elixir-europe/rdmkit) | [website](https://rdmkit.elixir-europe.org)
- [**ELIXIR-Norway Training** ELIXIR-Norway-Training/DMP-writing-workshop](https://github.com/ELIXIR-Norway-Training/DMP-writing-workshop) | [website](https://zenodo.org/doi/10.5281/zenodo.3693710)
- [**OpenSciency** opensciency/sprint-content](https://github.com/opensciency/sprint-content) | [website](https://opensciency.github.io/sprint-content/)
- [**Data Carpentry** datacarpentry/sql-ecology-lesson](https://github.com/datacarpentry/sql-ecology-lesson) | [website](http://datacarpentry.github.io/sql-ecology-lesson)
- [**Data Carpentry** datacarpentry/spreadsheet-ecology-lesson](https://github.com/datacarpentry/spreadsheet-ecology-lesson) | [website](https://datacarpentry.org/spreadsheet-ecology-lesson)
- [**SIB Swiss Institute of Bioinformatics** sib-swiss/ena-seqdata-training](https://github.com/sib-swiss/ena-seqdata-training) | [website](https://sib-swiss.github.io/ena-seqdata-training/)
- [**VIB Technologies: Training material and software projects** vibbits/rdm-introductory-course](https://github.com/vibbits/rdm-introductory-course)
- [**Utrecht University** UtrechtUniversity/dataprivacyhandbook](https://github.com/utrechtuniversity/dataprivacyhandbook) | [website](https://utrechtuniversity.github.io/dataprivacyhandbook/)
- [**NBIS - National Bioinformatics Infrastructure Sweden** NBISweden/module-dmp-dm-practices](https://github.com/NBISweden/module-dmp-dm-practices/) | [website](https://nbisweden.github.io/module-dmp-dm-practices/)
- [**NBIS - National Bioinformatics Infrastructure Sweden** NBISweden/module-data-publication-dm-practices](https://github.com/NBISweden/module-data-publication-dm-practices/) | [website](https://nbisweden.github.io/module-data-publication-dm-practices/)
- [**NBIS - National Bioinformatics Infrastructure Sweden** NBISweden/module-metadata-dm-practices](https://github.com/NBISweden/module-metadata-dm-practices/) | [website](https://nbisweden.github.io/module-metadata-dm-practices/)
- [**NBIS - National Bioinformatics Infrastructure Sweden** NBISweden/module-organising-data-dm-practices](https://github.com/NBISweden/module-organising-data-dm-practices/) | [website](https://nbisweden.github.io/module-organising-data-dm-practices/)
- [**NBIS - National Bioinformatics Infrastructure Sweden** NBISweden/module-open-science-dm-practices](https://github.com/NBISweden/module-open-science-dm-practices/) | [website](https://nbisweden.github.io/module-open-science-dm-practices/index.html)
- [**Health Data Science Sandbox** hds-sandbox/RDM_biodata_course](https://github.com/hds-sandbox/RDM_NGS_course) | [website](https://hds-sandbox.github.io/RDM_biodata_course/)
- [**SIB Swiss Institute of Bioinformatics** sib-swiss/Introduction-FAIR-RDM-DMP](https://github.com/sib-swiss/Introduction-FAIR-RDM-DMP) | [website](https://sib-swiss.github.io/Introduction-FAIR-RDM-DMP/)
- [**BioData.pt** BioData-PT/Ready4BioDataManagement](https://github.com/BioData-PT/Ready4BioDataManagement) | [website](https://biodata.pt/training/programmes/r4bdm)
- [**posit-conf-2023** posit-conf-2023/managing-os-project](https://github.com/posit-conf-2023/managing-os-project) | [website](https://posit-conf-2023.github.io/managing-os-project/)
- [**jhudsl** jhudsl/Adv_Reproducibility_in_Cancer_Informatics](https://github.com/jhudsl/Adv_Reproducibility_in_Cancer_Informatics) | [website](https://jhudatascience.org/Adv_Reproducibility_in_Cancer_Informatics)
- [**Fred Hutch Data Science Lab** fhdsl/Ethical_Data_Handling_for_Cancer_Research](https://github.com/fhdsl/Ethical_Data_Handling_for_Cancer_Research) | [website](https://hutchdatascience.org/Ethical_Data_Handling_for_Cancer_Research/)
- [**Fred Hutch Data Science Lab** fhdsl/NIH_Data_Sharing](https://github.com/fhdsl/NIH_Data_Sharing) | [website](https://hutchdatascience.org/NIH_Data_Sharing/)
- [**feichtingerm** feichtingerm/rdmlifesciunivie](https://github.com/feichtingerm/rdmlifesciunivie)
- [**OBOAcademy** OBOAcademy/obook](https://github.com/OBOAcademy/obook) | [website](https://oboacademy.github.io/obook/)

### FAIR data

- [**The Carpentries Incubator** carpentries-incubator/fair-bio-practice](https://github.com/carpentries-incubator/fair-bio-practice) | [website](https://carpentries-incubator.github.io/fair-bio-practice/)
- [**The Carpentries Incubator** carpentries-incubator/fair-for-leaders](https://github.com/carpentries-incubator/fair-for-leaders) | [website](https://carpentries-incubator.github.io/fair-for-leaders/)
- [**ELIXIR-Norway Training** ELIXIR-Norway-Training/fair-dm-lifesci-june-2022](https://github.com/ELIXIR-Norway-Training/fair-dm-lifesci-june-2022)
- [**FAIRplus** FAIRplus/the-fair-cookbook](https://github.com/FAIRplus/the-fair-cookbook) | [website](https://faircookbook.elixir-europe.org)
- [**NBIS - National Bioinformatics Infrastructure Sweden** NBISweden/module-repository-submission-dm-practices](https://github.com/NBISweden/module-repository-submission-dm-practices) | [website](https://nbisweden.github.io/module-repository-submission-dm-practices/)
- [**ELIXIR Europe Training** elixir-europe-training/ELIXIR-TrP-FAIR-training-handbook](https://github.com/elixir-europe-training/ELIXIR-TrP-FAIR-training-handbook) | [website](https://elixir-europe-training.github.io/ELIXIR-TrP-FAIR-training-handbook/)
- [**ELIXIR Europe Training** elixir-europe-training/ELIXIR-TrP-FAIR-Converge](https://github.com/elixir-europe-training/ELIXIR-TrP-FAIR-Converge) | [website](https://elixir-europe-training.github.io/ELIXIR-TrP-FAIR-Converge/)
- [**Institut Français de Bioinformatique (IFB)** IFB-ElixirFr/IFB-FAIR-bioinfo-training](https://github.com/IFB-ElixirFr/IFB-FAIR-bioinfo-training) | [website](https://ifb-elixirfr.github.io/IFB-FAIR-bioinfo-training)
- [**Institut Français de Bioinformatique (IFB)** IFB-ElixirFr/IFB-FAIR-data-training](https://github.com/ifb-elixirfr/IFB-FAIR-data-training)
- [**Sergio Martínez Cuesta** semacu/20180223_ORCID_Chemistry_Cambridge](https://github.com/semacu/20180223_ORCID_Chemistry_Cambridge)
- [**FAIR-by-Design-Methodology** FAIR-by-Design-Methodology/FAIR-by-Design_Book](https://github.com/fair-by-design-methodology/FAIR-by-Design_Book/) | [website](https://fair-by-design-methodology.github.io/FAIR-by-Design_Book/)
- [**The Carpentries Incubator** carpentries-incubator/FAIR-research-data-coursebook](https://github.com/carpentries-incubator/FAIR-research-data-coursebook) | [website](https://carpentries-incubator.github.io/FAIR-research-data-coursebook/)

### Reproducibility

- [**Teaching materials at the Harvard Chan Bioinformatics Core** hbctraining/Tools-for-reproducible-research](https://github.com/hbctraining/reproducibility-tools) | [website](https://hbctraining.github.io/Tools-for-reproducible-research/)
- [**NBIS - National Bioinformatics Infrastructure Sweden** NBISweden/workshop-reproducible-research](https://github.com/NBISweden/workshop-reproducible-research) | [website](https://nbisweden.github.io/workshop-reproducible-research/)
- [**The Carpentries Incubator** carpentries-incubator/managing-computational-projects](https://github.com/carpentries-incubator/managing-computational-projects) | [website](https://carpentries-incubator.github.io/managing-computational-projects)
- [**The Carpentries Incubator** carpentries-incubator/jekyll-pages-novice](https://github.com/carpentries-incubator/jekyll-pages-novice) | [website](https://carpentries-incubator.github.io/jekyll-pages-novice/)
- [**The Carpentries Incubator** carpentries-lab/good-enough-practices](https://github.com/carpentries-incubator/good-enough-practices) | [website](https://carpentries-lab.github.io/good-enough-practices/)
- [**Data Carpentry** datacarpentry/rr-organization1](https://github.com/datacarpentry/rr-organization1) | [website](http://www.datacarpentry.org/rr-organization1/)
- [**SIB Swiss Institute of Bioinformatics** sib-swiss/reproducible-analysis-training](https://github.com/sib-swiss/reproducible-analysis-training) | [website](https://sib-swiss.github.io/reproducible-analysis-training/)
- [**ELIXIR Europe Training** elixir-europe-training/ELIXIR-TrP-ContainersPython-CodeRep](https://github.com/elixir-europe-training/ELIXIR-TrP-ContainersPython-CodeRep) | [website](https://elixir-europe-training.github.io/ELIXIR-TrP-ContainersPython-CodeRep/)
- [**ELIXIR Europe Training** elixir-europe-training/ELIXIR-TrP-LiterateProgrammingR-CodeRep](https://github.com/elixir-europe-training/ELIXIR-TrP-LiterateProgrammingR-CodeRep) | [website](https://elixir-europe-training.github.io/ELIXIR-TrP-LiterateProgrammingR-CodeRep/)
- [**jhudsl** jhudsl/Reproducibility_in_Cancer_Informatics](https://github.com/jhudsl/Reproducibility_in_Cancer_Informatics) | [website](https://jhudatascience.org/Reproducibility_in_Cancer_Informatics/)
- [**jhudsl** jhudsl/Documentation_and_Usability](https://github.com/jhudsl/Documentation_and_Usability) | [website](https://jhudatascience.org/Documentation_and_Usability/)
- [**Alex's Lemonade Stand Foundation** AlexsLemonade/reproducible-research](https://github.com/AlexsLemonade/reproducible-research)

## Statistics and machine learning


### Data science

- [**Rafael A Irizarry** rafalab/dsbook](https://github.com/rafalab/dsbook)
- [**Stephanie Hicks** stephaniehicks/superwomen](https://github.com/stephaniehicks/superwomen) | [website](https://www.stephaniehicks.com/superwomen/)
- [**Hacking for Science** h4sci/h4sci-course](https://github.com/h4sci/h4sci-course)
- [**DataTalksClub** DataTalksClub/data-engineering-zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp)
- [**Jose A Dianes** jadianes/data-science-your-way](https://github.com/jadianes/data-science-your-way) | [website](http://jadianes.github.io/data-science-your-way)
- [**Jose A Dianes** jadianes/spark-r-notebooks](https://github.com/jadianes/spark-r-notebooks) | [website](http://jadianes.github.io/spark-r-notebooks)
- [**Data Carpentry** datacarpentry/python-ecology-lesson](https://github.com/datacarpentry/python-ecology-lesson) | [website](https://datacarpentry.org/python-ecology-lesson)
- [**Data Science in Practice** DataScienceInPractice/Site](https://github.com/datascienceinpractice/Site) | [website](https://datascienceinpractice.github.io)
- [**Shawn Rhoads** shawnrhoads/gu-psyc-347](https://github.com/shawnrhoads/gu-psyc-347) | [website](https://shawnrhoads.github.io/gu-psyc-347/)
- [**NBIS - National Bioinformatics Infrastructure Sweden** NBISweden/module-openrefine-dm-practices](https://github.com/NBISweden/module-openrefine-dm-practices/) | [website](https://nbisweden.github.io/module-openrefine-dm-practices/)
- [**Rafael A Irizarry** rafalab/dsbook-part-1](https://github.com/rafalab/dsbook-part-1)
- [**Rafael A Irizarry** rafalab/dsbook-part-2](https://github.com/rafalab/dsbook-part-2)
- [**Pablo Casas** pablo14/data-science-live-book](https://github.com/pablo14/data-science-live-book) | [website](http://livebook.datascienceheroes.com)
- [**Roger D. Peng** rdpeng/artofdatascience](https://github.com/rdpeng/artofdatascience)
- [**UC Berkeley Data 8** data-8/textbook](https://github.com/data-8/textbook) | [website](http://www.inferentialthinking.com)
- [**Federico Carrone** unbalancedparentheses/data_science_in_julia_for_hackers](https://github.com/unbalancedparentheses/data_science_in_julia_for_hackers) | [website](https://datasciencejuliahackers.com)
- [**UC Berkeley Data 100** DS-100/textbook](https://github.com/DS-100/textbook/) | [website](https://learningds.org)
- [**Edwin Thoen** EdwinTh/ADSwR](https://github.com/edwinth/ADSwR) | [website](https://edwinth.github.io/ADSwR/)
- [**tidyverse** tidyverse/datascience-box](https://github.com/tidyverse/datascience-box) | [website](https://datasciencebox.org)
- [**Modern Data Science with R** mdsr-book/mdsr-book.github.io](https://github.com/mdsr-book/mdsr-book.github.io)
- [**Lino Galiana** linogaliana/python-datascientist](https://github.com/linogaliana/python-datascientist) | [website](https://pythonds.linogaliana.fr)
- [**The Turing Way** the-turing-way/the-turing-way](https://github.com/the-turing-way/the-turing-way) | [website](http://the-turing-way.org)
- [**Michael Pyrcz** GeostatsGuy/DataScienceInteractivePython](https://github.com/GeostatsGuy/DataScienceInteractivePython)

### Statistics

- [**Aedin Culhane** aedin/PCAworkshop](https://github.com/aedin/PCAworkshop) | [website](https://aedin.github.io/PCAworkshop/)
- [**CRUK CI Bioinformatics Core** bioinformatics-core-shared-training/experimental-design](https://github.com/bioinformatics-core-shared-training/experimental-design) | [website](http://bioinformatics-core-shared-training.github.io/experimental-design)
- [**CRUK CI Bioinformatics Core** bioinformatics-core-shared-training/IntroductionToStats](https://github.com/bioinformatics-core-shared-training/IntroductionToStats) | [website](http://bioinformatics-core-shared-training.github.io/IntroductionToStats/)
- [**The Carpentries Incubator** carpentries-incubator/statistical-thinking-public-health](https://github.com/carpentries-incubator/statistical-thinking-public-health) | [website](https://carpentries-incubator.github.io/statistical-thinking-public-health)
- [**Richard McElreath** rmcelreath/stat_rethinking_2022](https://github.com/rmcelreath/stat_rethinking_2022)
- [**SIB Swiss Institute of Bioinformatics** sib-swiss/advanced-statistics](https://github.com/sib-swiss/advanced-statistics)
- [**SIB Swiss Institute of Bioinformatics** sib-swiss/intro-bayesian-statistics-training](https://github.com/sib-swiss/intro-bayesian-statistics-training) | [website](https://sib-swiss.github.io/intro-bayesian-statistics-training/)
- [**SIB Swiss Institute of Bioinformatics** sib-swiss/introduction-to-statistics-with-python-training](https://github.com/sib-swiss/introduction-to-statistics-with-python-training)
- [**SIB Swiss Institute of Bioinformatics** sib-swiss/Introduction-to-statistics-with-R](https://github.com/sib-swiss/Introduction-to-statistics-with-R)
- [**SIB Swiss Institute of Bioinformatics** sib-swiss/statistics-and-machine-learning-training](https://github.com/sib-swiss/statistics-and-machine-learning-training)
- [**Richard McElreath** rmcelreath/stat_rethinking_2023](https://github.com/rmcelreath/stat_rethinking_2023)
- [**David Dalpiaz** daviddalpiaz/appliedstats](https://github.com/daviddalpiaz/appliedstats) | [website](https://book.stat420.org)
- [**cambiotraining** cambiotraining/corestats](https://github.com/cambiotraining/corestats) | [website](https://cambiotraining.github.io/corestats/)
- [**David Dalpiaz** daviddalpiaz/r4sl](https://github.com/daviddalpiaz/r4sl) | [website](https://daviddalpiaz.github.io/r4sl/)
- [**Mojtaba Barzegari** mbarzegary/educational-bayesian](https://github.com/mbarzegary/educational-bayesian)
- [**SIB Swiss Institute of Bioinformatics** sib-swiss/Data-analysis-in-practice](https://github.com/sib-swiss/Data-analysis-in-practice)
- [**The Gulbenkian Training Programme in Bioinformatics** GTPB/PSLS22](https://github.com/gtpb/PSLS22) | [website](https://gtpb.github.io/PSLS22/)
- [**The Gulbenkian Training Programme in Bioinformatics** GTPB/PGDH19](https://github.com/gtpb/PGDH19) | [website](https://gtpb.github.io/PGDH19/)
- [**The Gulbenkian Training Programme in Bioinformatics** GTPB/PSLS20](https://github.com/gtpb/PSLS20) | [website](https://gtpb.github.io/PSLS20/)
- [**Paul Roback** proback/BeyondMLR](https://github.com/proback/BeyondMLR)
- [**Matthew B. Jané** MatthewBJane/guide-to-effect-sizes-and-confidence-intervals](https://github.com/MatthewBJane/guide-to-effect-sizes-and-confidence-intervals) | [website](https://matthewbjane.quarto.pub/guide-to-effect-sizes-and-confidence-intervals/)
- [**Richard McElreath** rmcelreath/stat_rethinking_2024](https://github.com/rmcelreath/stat_rethinking_2024)
- [**Monash Data Fluency** MonashDataFluency/r-linear](https://github.com/MonashDataFluency/r-linear) | [website](https://monashdatafluency.github.io/r-linear/)
- [**Causal Inference in R** r-causal/causal-inference-in-R](https://github.com/r-causal/causal-inference-in-R) | [website](https://www.r-causal.org)
- [**OpenIntro** OpenIntroStat/ims](https://github.com/OpenIntroStat/ims/) | [website](https://openintro-ims.netlify.app)
- [**Allen Downey** AllenDowney/ThinkBayes](https://github.com/AllenDowney/ThinkBayes)
- [**Måns Thulin** mthulin/mswr-book](https://github.com/mthulin/mswr-book)
- [**A. Solomon Kurz** ASKurz/Statistical_Rethinking_with_brms_ggplot2_and_the_tidyverse_2_ed](https://github.com/ASKurz/Statistical_Rethinking_with_brms_ggplot2_and_the_tidyverse_2_ed) | [website](https://bookdown.org/content/4857/)
- [**Allen Downey** AllenDowney/ThinkStats2](https://github.com/AllenDowney/ThinkStats2) | [website](http://allendowney.github.io/ThinkStats2/)
- [**Daniel Kaplan** dtkaplan/Lessons-in-statistical-thinking](https://github.com/dtkaplan/Lessons-in-statistical-thinking)
- [**Oslo Centre for Biostatistics and Epidemiology** ocbe-uio/teaching_mf9130e](https://github.com/ocbe-uio/teaching_mf9130e) | [website](https://ocbe-uio.github.io/teaching_mf9130e/)
- [**Oslo Centre for Biostatistics and Epidemiology** ocbe-uio/course_med3007](https://github.com/ocbe-uio/course_med3007) | [website](https://ocbe-uio.github.io/course_med3007/)
- [**Neuromatch Academy** NeuromatchAcademy/course-content](https://github.com/NeuromatchAcademy/course-content) | [website](https://compneuro.neuromatch.io)
- [**Norm Matloff** matloff/fastStat](https://github.com/matloff/fastStat)

### Machine learning

- [**Canadian Bioinformatics Workshops** bioinformatics-ca/MLE_2021](https://github.com/bioinformatics-ca/MLE_2021)
- [**The Carpentries Incubator** carpentries-incubator/machine-learning-novice-python](https://github.com/carpentries-incubator/machine-learning-novice-python) | [website](https://carpentries-incubator.github.io/machine-learning-novice-python/)
- [**The Carpentries Incubator** carpentries-incubator/machine-learning-novice-sklearn](https://github.com/carpentries-incubator/machine-learning-novice-sklearn) | [website](https://carpentries-incubator.github.io/machine-learning-novice-sklearn/)
- [**fast.ai** fastai/course20](https://github.com/fastai/course20) | [website](https://book.fast.ai)
- [**SIB Swiss Institute of Bioinformatics** sib-swiss/intro-machine-learning-training](https://github.com/sib-swiss/intro-machine-learning-training)
- [**Phillip Lippe** phlippe/uvadlc_notebooks](https://github.com/phlippe/uvadlc_notebooks/) | [website](https://uvadlc-notebooks.readthedocs.io/en/latest/)
- [**The Carpentries Incubator** carpentries-incubator/ml4bio-workshop](https://github.com/carpentries-incubator/ml4bio-workshop) | [website](https://carpentries-incubator.github.io/ml4bio-workshop/)
- [**Instill AI** instillai/TensorFlow-Course](https://github.com/instillai/TensorFlow-Course)
- [**Yury Kashnitsky** Yorko/mlcourse.ai](https://github.com/Yorko/mlcourse.ai) | [website](https://mlcourse.ai)
- [**fast.ai** fastai/course-nlp](https://github.com/fastai/course-nlp) | [website](https://www.fast.ai/2019/07/08/fastai-nlp/)
- [**girafe.ai** girafe-ai/ml-course](https://github.com/girafe-ai/ml-course)
- [**Paderborn University - LEA** upb-lea/reinforcement_learning_course_materials](https://github.com/upb-lea/reinforcement_learning_course_materials)
- [**Lex Fridman** lexfridman/mit-deep-learning](https://github.com/lexfridman/mit-deep-learning) | [website](https://deeplearning.mit.edu)
- [**cambiotraining** cambiotraining/intro-machine-learning](https://github.com/cambiotraining/intro-machine-learning/) | [website](https://cambiotraining.github.io/intro-machine-learning/)
- [**The Carpentries Incubator** carpentries-incubator/data-science-ai-senior-researchers](https://github.com/carpentries-incubator/data-science-ai-senior-researchers) | [website](https://carpentries-incubator.github.io/data-science-ai-senior-researchers/)
- [**The Carpentries Incubator** carpentries-incubator/deep-learning-intro](https://github.com/carpentries-incubator/deep-learning-intro) | [website](https://carpentries-lab.github.io/deep-learning-intro/)
- [**Sven Degroeve** sdgroeve/Machine-Learning-Course-2days](https://github.com/sdgroeve/Machine-Learning-Course-2days)
- [**Philip Bowsher** philbowsher/Workshop-R-Tensorflow-Scientific-Computing](https://github.com/philbowsher/Workshop-R-Tensorflow-Scientific-Computing)
- [**Nicola Rennie** nrennie/r-pharma-2023-tidymodels](https://github.com/nrennie/r-pharma-2023-tidymodels) | [website](https://nrennie.github.io/r-pharma-2023-tidymodels/)
- [**bioinformatics.ca** bioinformaticsdotca/MLE_2023](https://github.com/bioinformaticsdotca/MLE_2023)
- [**SIB Swiss Institute of Bioinformatics** sib-swiss/pytorch-practical-training](https://github.com/sib-swiss/pytorch-practical-training)
- [**Applied Machine Learning for Tabular Data** aml4td/website](https://github.com/aml4td/website) | [website](https://aml4td.org)
- [**tidymodels** tidymodels/workshops](https://github.com/tidymodels/workshops) | [website](https://workshops.tidymodels.org)
- [**posit-conf-2023** posit-conf-2023/python-modeling](https://github.com/posit-conf-2023/python-modeling)
- [**Emil Hvitfeldt** EmilHvitfeldt/smltar](https://github.com/EmilHvitfeldt/smltar) | [website](https://smltar.com)
- [**Navid Nobani** Naviden/ML-intro-with-Python](https://github.com/Naviden/ML-intro-with-Python)
- [**mlr-org** mlr-org/mlr3book](https://github.com/mlr-org/mlr3book) | [website](https://mlr3book.mlr-org.com)
- [**Inria** INRIA/scikit-learn-mooc](https://github.com/INRIA/scikit-learn-mooc) | [website](https://inria.github.io/scikit-learn-mooc)
- [**posit::conf(2024)** posit-conf-2024/vetiver](https://github.com/posit-conf-2024/vetiver) | [website](https://posit-conf-2024.github.io/vetiver/)
- [**posit::conf(2024)** posit-conf-2024/ml-python](https://github.com/posit-conf-2024/ml-python) | [website](https://posit-conf-2024.github.io/ml-python/)
- [**Emil Hvitfeldt** EmilHvitfeldt/feature-engineering-az](https://github.com/EmilHvitfeldt/feature-engineering-az) | [website](https://feaz-book.com)

### Artificial intelligence

- [**udlbook** udlbook/udlbook](https://github.com/udlbook/udlbook)
- [**Maxime Labonne** mlabonne/llm-course](https://github.com/mlabonne/llm-course) | [website](https://mlabonne.github.io/blog/)
- [**Fred Hutch Data Science Lab** fhdsl/AI_for_Decision_Makers](https://github.com/fhdsl/AI_for_Decision_Makers) | [website](https://hutchdatascience.org/AI_for_Decision_Makers/)
- [**Fred Hutch Data Science Lab** fhdsl/AI_for_Efficient_Programming](https://github.com/fhdsl/AI_for_Efficient_Programming) | [website](https://hutchdatascience.org/AI_for_Efficient_Programming/)

## Others


### General

- [**Amanda Miotto** amandamiotto/HackyHourBookmarks](https://github.com/amandamiotto/HackyHourBookmarks)
- [**biodatascience** biodatascience/compbio](https://github.com/biodatascience/compbio) | [website](https://biodatascience.github.io/compbio/)
- [**Bradley Boehmke** bradleyboehmke/data-science-learning-resources](https://github.com/bradleyboehmke/data-science-learning-resources)
- [**Ming Tang** crazyhottommy/getting-started-with-genomics-tools-and-resources](https://github.com/crazyhottommy/getting-started-with-genomics-tools-and-resources)
- [**Teaching materials at the Harvard Chan Bioinformatics Core** hbctraining/Training-modules](https://github.com/hbctraining/Training-modules) | [website](https://hbctraining.github.io/Training-modules/)
- [**Genome Informatics Facility** ISUgenomics/bioinformatics-workbook](https://github.com/ISUgenomics/bioinformatics-workbook) | [website](https://bioinformaticsworkbook.org)
- [**Melbourne Bioinformatics** melbournebioinformatics/MelBioInf_docs](https://github.com/melbournebioinformatics/MelBioInf_docs)
- [**Mike Lee** AstrobioMike/AstrobioMike.github.io](https://github.com/AstrobioMike/AstrobioMike.github.io) | [website](https://astrobiomike.github.io)
- [**liulab-dfci** liulab-dfci/bioinfo-combio](https://github.com/liulab-dfci/bioinfo-combio)
- [**Leighton Pritchard** widdowquinn/Teaching-IBioIC-Intro-to-Bioinformatics](https://github.com/widdowquinn/Teaching-IBioIC-Intro-to-Bioinformatics) | [website](https://widdowquinn.github.io/Teaching-IBioIC-Intro-to-Bioinformatics/)
- [**Ujjwal Karn** ujjwalkarn/DataScienceR](https://github.com/ujjwalkarn/DataScienceR)
- [**Salvatore Raieli** SalvatoreRa/tutorial](https://github.com/SalvatoreRa/tutorial)
- [**Alex's Lemonade Stand Foundation** AlexsLemonade/training-modules](https://github.com/alexslemonade/training-modules)
- [**Andrea Telatin** telatin/microbiome-bioinformatics](https://github.com/telatin/microbiome-bioinformatics/) | [website](https://telatin.github.io/microbiome-bioinformatics)
- [**Ronan Harrington** rnnh/bioinfo-notebook](https://github.com/rnnh/bioinfo-notebook) | [website](https://rnnh.github.io/bioinfo-notebook/)
- [**Women In Bioinformatics and Data Science Latin America** WomenBioinfoDataScLA/Workshops](https://github.com/WomenBioinfoDataScLA/Workshops)
- [**Common Fund Data Ecosystem** nih-cfde/training-and-engagement](https://github.com/nih-cfde/training-and-engagement) | [website](https://training.nih-cfde.org)
- [**Thomas Denecker** thomasdenecker/FAIR_Bioinfo](https://github.com/thomasdenecker/FAIR_Bioinfo)
- [**Eric C. Anderson** eriqande/eca-bioinf-handbook](https://github.com/eriqande/eca-bioinf-handbook)
- [**Computational Biology and Bioinformatics at UCLouvain** UCLouvain-CBIO/WSBIM1322](https://github.com/UCLouvain-CBIO/WSBIM1322) | [website](https://uclouvain-cbio.github.io/WSBIM1322/)
- [**UC Davis Bioinformatics Core Training Page** ucdavis-bioinformatics-training/2020-Bioinformatics_Prerequisites_Workshop](https://github.com/ucdavis-bioinformatics-training/2020-Bioinformatics_Prerequisites_Workshop) | [website](https://ucdavis-bioinformatics-training.github.io/2020-Bioinformatics_Prerequisites_Workshop/)
- [**posit-conf-2023** posit-conf-2023/devops](https://github.com/posit-conf-2023/devops)
- [**BioinformaNicks** BioinformaNicks/Bioinformatics-training-collection](https://github.com/BioinformaNicks/Bioinformatics-training-collection)
- [**Sex Chromosome Lab** SexChrLab/BioinformaticsIntroduction](https://github.com/SexChrLab/BioinformaticsIntroduction/)
- [**Harvard Informatics** harvardinformatics/learning-bioinformatics-at-home](https://github.com/harvardinformatics/learning-bioinformatics-at-home)
- [**jhudsl** jhudsl/Informatics_Research_Leadership](https://github.com/jhudsl/Informatics_Research_Leadership) | [website](https://jhudatascience.org/Informatics_Research_Leadership/)
- [**Pachter Lab** pachterlab/BI-BE-CS-183-2023](https://github.com/pachterlab/BI-BE-CS-183-2023)
- [**St. Jude Children's Research Hospital** stjude/learngenomics.dev](https://github.com/stjude/learngenomics.dev) | [website](https://learngenomics.dev)
- [**gladstone-institutes** gladstone-institutes/Bioinformatics-Workshops](https://github.com/gladstone-institutes/Bioinformatics-Workshops) | [website](https://github.com/gladstone-institutes/Bioinformatics-Presentations/wiki)

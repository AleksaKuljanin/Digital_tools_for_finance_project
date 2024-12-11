Momentum Strategy with US stocks - Testing different lookback periods
==============================

# Table of Contents

- [Project Overview](#project-overview)
    - [Introduction](#introduction)
    - [Methodology](#methodology)
    - [Data Basis](#data-basis)
- [Project Organization](#project-organization)
- [How to reproduce this project?](#how-to-reproduce-this-project)
    - [Using Docker](#using-docker)
    - [Using Anaconda environments](#using-anaconda-environments)


## Project overview

### Introduction
We are conducting a project to assess the effectiveness of various lookback periods in a momentum strategy targeting S&P 100 equities. The goal is to identify the optimal historical timeframes that enhance strategy performance and improve trading signals by analyzing past price trends.


### Methodology

We are testing both a long-short and a long-only strategy, with the number of stocks in each portfolio remaining constant. Stock selection is based on their recent performance, which varies according to the lookback period being tested. In the long-short strategy, we will take short positions in stocks with the worst performance and long positions in those with the best performance. In both strategies, stocks are equally weighted. The exposure for the long-only portfolio will be 100%, while the long-short portfolio will maintain a initial net exposure of 0%. In cases where the number of holdings is uneven, there will be one more long position than short positions. For example, with five holdings, there would be three long positions and two short positions.


### Data basis

- Data source: Bloomberg
- S&P 100 stocks
- Only monthly price data is considered
- Historical data from July 2004 to June 2024


## Project Organization

    ├── LICENSE
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docker_jupyter     <- Files for Jupyter Docker image & container
    ├── docker_tex         <- Files for Tex Docker image & container
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │
    ├── reports            <- Generated analysis as PDF & LaTeX
    │   ├── Graphics       <- Generated graphics and figures to be used in reporting
    │   ├── Tex            <- Tex files for reporting
    │   ├── styles         <- Styles for Tex files
    │   └── output         <- The final PDF files
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    └── src                <- Source code for use in this project.
        │
        ├── data           <- Scripts to download or generate data
        │
        └── features       <- Scripts to turn raw data into features

    

## How to reproduce this project?

### Using Docker

With the following instructions this project is fully reproducible using Docker.
We assume that the needed software (especially an IDE and Docker) is already installed on your machine.
1. Using a terminal of your choice `clone` the git repository to your roots folder.
    ```git clone PathToGitRepository```
2. Within the terminal navigate to the folder "Momentum Strategies" using `cd`
3. Start the docker-decompose file using `docker-compose up --build`
4. The docker image will be loaded and the containers are running.
5. The docker-tex container will create the resulting PDF-File from the main.tex file.
6. The docker-jupyter container is accessible through your webbrwoser of choice. The exact localhost URL will be provided within the terminal.
7. Open the localhost URL within your webbrowser. 
8. All the necessary data, python and jupyter notebook files are accessible and runnable within this jupyter container.


### Using Anaconda environments

With the following instructions this project is reproducible using Anaconda environments.
We assume that the needed software (especially an IDE and Anaconda) is already installed on your machine.
1. Using Anaconda Prompt create a new Anaconda environment with the following command:
   ```conda create --name NameForYourNewEnvironment pyhton=3.13```
2. Activate your new Anaconda environment using
   ```conda activate NameForYourNewEnvironment```
3. Install git within your environment `conda install git`
4. Clone this git repository using `git clone RepositoryURL`
5. Using `cd` switch into the project directory
6. Install the requirements using
   ```pip3 install -r requirements.txt``` or ```python.exe -m pip install -r requirements.txt```

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>

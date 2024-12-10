Momentum Strategy with US stocks - Testing different lookback periods
==============================

# Table of Contents
- [Project Overview](#project-overview)
    - [Introduction](#introduction)
    - [Data Basis](#data-basis)
- [Project Organization](#project-organization)
- [How to reproduce this project?](#how-to-reproduce-this-project)
    - [Using Docker](#using-docker)
    - [Using Anaconda environments](#using-anaconda-environments)

## Project overview
### Introduction
We are conducting a project to assess the effectiveness of various lookback periods in a momentum strategy targeting S&P 500 equities. The goal is to identify the optimal historical timeframes that enhance strategy performance and improve trading signals by analyzing past price trends.

We are testing both a long-short and a long-only strategy, with the number of stocks in each portfolio remaining constant. Stock selection is based on their recent performance, which varies according to the lookback period being tested. In the long-short strategy, we will take short positions in stocks with the worst performance and long positions in those with the best performance. In both strategies, stocks are equally weighted. The exposure for the long-only portfolio will be 100%, while the long-short portfolio will maintain a initial net exposure of 0%. 

### Data basis
- Data source: Bloomberg
- S&P 100 stocks
- Monthly price data
- Historical data from July 2014 to July 2024


## Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io

## How to reproduce this project?

### Using Docker
With the following instructions this project is fully reproducible using Docker.
We assume that the needed software (especially an IDE and Docker) is already installed on your machine.
1. Using a terminal of your choice 'clone' the git repository to your roots folder.
    'git clone PathToGitRepository'
2. Within the temrinal navigate to the folder "Momentum Strategies" using 'cd'
3. Start the docker-decompose file using 'docker-decompose up --build'
4. The docker image will be loaded and the containers are running.
5. The docker-tex container will create the resulting PDF-File from the main.tex file.
6. The docker-jupyter container is accessible through your webbrwoser of choice. The exact localhost URL will be provided within the terminal.
7. Open the localhost URL within your webbrowser. 
8. All the necessary data, python and jupyter notebook files are accessible and runnable within this jupyter container.

### Using Anaconda environments




--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>

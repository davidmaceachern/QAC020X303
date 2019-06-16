# summative-assignment
==============================

## Datasets

[pricing data](http://landregistry.data.gov.uk/app/ppd/ppd_data?et%5B%5D=lrcommon%3Afreehold&et%5B%5D=lrcommon%3Aleasehold&limit=1000&max_date=4+June+2019&min_date=1+June+2013&nb%5B%5D=true&nb%5B%5D=false&ptype%5B%5D=lrcommon%3Adetached&ptype%5B%5D=lrcommon%3Asemi-detached&ptype%5B%5D=lrcommon%3Aterraced&ptype%5B%5D=lrcommon%3Aflat-maisonette&ptype%5B%5D=lrcommon%3AotherPropertyType&tc%5B%5D=ppd%3AstandardPricePaidTransaction&tc%5B%5D=ppd%3AadditionalPricePaidTransaction&town=london)
[postcode data](https://geoportal.statistics.gov.uk/datasets/national-statistics-postcode-lookup-may-2019)

## Preprocessing

### Missing Values

MCAR Missing Values test

### Geocoding Postcodes

1. check for NaN in python list
2. for each 100 items
3. call the api
4. parse the response
5. map the response

### CSV Lookup

1. load df with postcodes
2. batch by area code
3. groupby areacode
4. open respective csv file ('NSPL_MAY_2019_UK_{}.csv').format(areacode)
5. choose columns wanted, lookup and append to respective row in df

### Joining Tables

1. postcode lookup (2628568, 41)
2. our addresses (345551, 16)
3. our merged (157472, 57)
4. this means that 188,079 addresses were actually duplicates?

## Build Features

- Combine the lat and the long into 1 feature
- Imputation
- Correlation/covariance
- Feature Selection
- Plot postcodes on Map
- Plot GPS Coordinates

### Unique Id

This work very well if you have few categories, however in the case of thousands of IDs this will increase your dimensionality too much. What you can do is collect statistics about the target and other features per group and join these onto your set and then remove your categories. This is what is usually done with a high number of categories. You have to be careful not to leak any information about your target into your features though (problem called label leaking).

## Train Models

- Transformation
- Normal Distribution
- Cross Validation
- Linear Regression
- Support Vector Machine
- PCA
- Gaussian and NB
- KNN
- Naive Bayes
- [Neural Net](https://towardsdatascience.com/how-to-build-your-own-neural-network-from-scratch-in-python-68998a08e4f6)



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
    └── tox.ini            <- tox file with settings for running tox; see tox.testrun.org


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>

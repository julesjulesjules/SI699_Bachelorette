# SI699_Bachelorette
##### Mastery Project
##### Jillian Peacock & Julie Gilbert


# Data Files:
### Original files from outside sources
* bachelorette_538.csv - contains contestant information as well as rose, date, and elimination data; from fivethirtyeight.com
* bachelor-contestants.csv - contains contestant demographic information from The Bachelor
* bachelorette-contestants.csv - contains contestant demographic information from The Bachelorette
* bachelors.csv - contains demographic information on the bachelors from The Bachelor
* bachelorettes.csv - contains demographic information on the bachelorettes from The Bachelorette
### Compiled Files, Created
* AgeComparisons.csv - for each season of data available in 'bachelor-contestants.csv' and 'bachelorette-contestants.csv' reports the age of the winner compared to the mean age of the contestant pool, as well as the difference between those two values
* the_bachelor.csv - combined bachelor-contestants.csv and bachelors.csv
* the_bachelorette.csv - combined bachelor-contestants.csv and bachelorettes.csv
* elimiation_long_form.csv - long form data version of bachelorette_538.csv
* slim_set_bachelor.csv - slim set of variables for bachelor prediction
* ette_cont_occ_group.csv - bachelorette-contestants.csv with extra column for new occupation grouping
### Information Files
* occupation_categories.txt - contains information on groupings determined for occupation groups

# Code Bits
* Exploratory.ipynb - initial exploration of the show contestant information; no external files made
* Munging.ipynb - combining demographic data into large sets; the_bachelor.csv, the_bachelorette.csv, and elimination_long_form.csv made
* VariableCreation.ipynb - creating new variables to use for bachelor prediction; slim_set_bachelor.csv made
* BaselineModel.ipynb - contains code for the 'baseline model' to use for grading the final model

# slim_set_bachelor.csv
| Variable                 | DataType | Description |
| ------------------------ |:--------:| -----------:|
| SEASON                   |  int64   | The Bachelor television season number |
| CONTESTANT               |  object  | Name of contestant |
| CONTESTANT_JOB           |  object  | Occupation of the contestant |
| CONTESTANT_HEIGHT        |  float64 | Contestant height in inches |
| HEIGHT_DIFF              |  float64 | Difference in height between the contestant and the Bachelor (Bachelor height - Contestant height) |
| HEIGHT_BIN               |  int32   | Height difference binned into levels, 2: Taller, 1: Same Height, 0: Shorter, 4: Missing |
| CONTESTANT_HOMETOWN_CITY |  object  | Hometown of the contestant |
| SAME_CITY                |  int32   | Binary, 1: Hometown city is the same between the contestant and Bachelor, 0: different |
| SAME_STATE               |  int32   | Binary, 1: Hometown state is the same between the contestant and Bachelor, 0: different |
| CONTESTANT_HOMETOWN_STATE|  object  | Hometown state of the Contestant |
| CONTESTANT_REGION        |  object  | Region of the hometown state of the contestant, N - North East, W - West, M - Mid West, S - South, O - Other |
| SAME_REGION              |  int32   | Binary, 1: Hometown state region is the same between the contestant and the Bachelor, 0: different |
| AGE_DIFF                 |  float64 | Age difference between the Bachelor and the contestant (Bachelor Age - Contestant Age) |
| AGE_DIFF_MEAN_POOL       |  float64 | Age difference between the contestant and the mean age of the contestant pool (Contestant - Pool) |
| AGE_DIFF_BACH_POOL       |  float64 | Age difference between the Bachelor and the mean age of the contestant pool (Bachelor - Pool) |
| AGE_DIFF_CAT             |  int32   | Age difference categorical, Contestants are 2: Younger, 1: Same, 0: Older, 4: Missing |
| CONTESTANT_ELIMWEEK      |  float64 | Week the contestant was eliminated from their season |
| WINNER                   |  int32   | Binary, 1: Winner, 0: Loser |    

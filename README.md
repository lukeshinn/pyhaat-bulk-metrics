# pyhaat-bulk-metrics

## :construction: This is a work in progress :construction:

### Installation

:bangbang: You must have Github SSH setup. If `git clone git@github.com:hudl/hudl-organizations.git` fails you likely dont have SSH setup

From the repository root execute:

`python3 -m venv venv`

`source venv/bin/activate`

`pip3 install -r requirements.txt --no-cache-dir`

`pip install --extra-index-url http://pypi.hudltools.com --trusted-host pypi.hudltools.com pyhaat`

### Usage

`python3 get_historical_pyhaat_data.py <DirectoryPath> <StartDate> <EndDate> <Frequency>`

#### Inputs

| Input Name    | description                                                                                                                                               | Example              |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- |
| DirectoryPath | System path that should point at a direcotry of repos                                                                                                     | `~/Developer/Github` |
| StartDate     | Start date to run analysis on in mm/dd/yyy format                                                                                                         | `01/01/2023`         |
| EndDate       | End date to run analysis on in mm/dd/yyy format                                                                                                           | `06/01/2023`         |
| Frequency     | Cadence to run analysis on. Can be any option from [this param list](https://pandas.pydata.org/docs/user_guide/timeseries.html#timeseries-offset-aliases) | `m`                  |

### Example

From the repo root

`python3 get_historical_pyhaat_data.py ~/repos/pyhaat-bulk-metrics/hudl_repos 04/01/2024 06/01/2024 m`

- You will see a generated -rmetrics.csv and -bmetrics.csv which will hold rest and bifrost data

### TODOS and Bugs

- :bug: Critical: master vs main on some repos
- :bug: Critical: Validation for frequency arg. Right now it will break if you enter anything besides d/m/y
- Make terminal stdout formatting more readable

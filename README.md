# pyhaat-bulk-metrics

## :construction: This is a work in progress :construction:

### Installation

From the repository root execute:
`python3 -m venv venv`

`source venv/bin/activate`

`pip3 install -r requirements.txt --no-cache-dir`

`pip install --extra-index-url http://pypi.hudltools.com --trusted-host pypi.hudltools.com pyhaat`

### Usage

1. Start virtual environment and install requirements
2. run `python3 main.py startDate {mm/dd/yyyy} endDate {mm/dd/yyyy} frequency{d/m/y} requestType{-r/-b}`
3. This will iterate through the seed_data.py AllRepos class attribute. Set the repository state at master for the given date. Then run pyhaat-coverage on a repo group. The results will be output to {-r/-b}metrics.csv
4. There are a couple of critical issues listed in the todo.md

### Example

From the repo root

`python3 main.py 8/20/2023 5/20/2024 m -r`

- This will read from the seed_data.py class attribute and run analysis once a month between the date ranges provided. The results will be output to -rmetrics.csv

- You will see in the -rmetrics.csv generated that feedproduces, profiles, and organizations have low REST coverage numbers (0/5.1/0)
- You will also see a pivot-rmetrics.csv this is experimental and doesn't seem to format correctly. There is a run_date row that is always blank which makes graphing an issue.

### TODOS and Bugs

- Critical: master vs main on some repos
- Critical: Validation for frequency arg. Right now it will break if you enter anything besides d/m/y
- Critical: If you dont clear out hudl_repos/competitive/etc on a new run it will
- Add args params several places instead of hard coding business units/dates/etc
- add support for ELITE repos or another business unit besides competitive
- Make terminal stdout formatting more readable

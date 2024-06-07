# pyhaat-bulk-metrics

## :construction: This is a work in progress :construction:

### Usage

1. Start virtual environment and install requirements
2. run `python3 main.py {mm/dd/yyyy} -{r/b} --seed {competitive/elite}` (you only need to include the seed flag when you want to clone a list of repos from the seed data file
3. This will iterate through the seed_data.py AllRepos class attribute. Set the repository state at master for the given date. Then run pyhaat-coverage on a repo group. The results will be output to {-r/-b}metrics.csv
4. There are a couple of critical issues listed in the todo.md

### Example

From the repo root

`python3 main.py 6/20/2023 -r --seed competitive`

- You will see in the -rmetrics.csv generated that feedproduces, profiles, and organizations have low REST coverage numbers (0/5.1/0)

`python3 main.py 5/20/2024 -r`

- You will see in -rmetrics.csv an appended table with update metrics that match 5/20's coverage metrics

### TODOS and Bugs

- Critical: master vs main on some repos
- Add args params several places instead of hard coding business units/dates/etc
- update seed data with a larger list of repos
- add support for ELITE repos or another business unit besides competitive
- Make terminal stdout formatting more readable

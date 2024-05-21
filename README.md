# pyhaat-bulk-metrics

### Usage
1. Start virtual environment and install requirements
2. run `python3 main.py {mm/dd/yyyy} --seed competitive` (you only need to include the seed flag when you want to clone a list of repos from the seed data file
4. This will iterate through the seed_data.py AllRepos class attribute. Set the repository state at master for the given date. Then run pyhaat-coverage on a repo group. The results will be output to test.csv.
5. There are a couple of critical issues listed in the todo.md


### Example
From the repo root
`python3 main.py 6/20/2023 --seed competitive`
- You will see in the test.csv generated that feedproduces, profiles, and organizations have low REST coverage numbers (0/5.1/0)
`python3 main.py 5/20/2024`
- You will see in test.csv an appended table with update metrics that match 5/20's coverage metrics

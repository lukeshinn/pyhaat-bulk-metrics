import subprocess
from seed_data import AllRepos


def create_seed_data(seed):
    business_unit = getattr(AllRepos, seed)
    for repo in business_unit:
        result = subprocess.Popen(
            f'git clone git@github.com:hudl/{repo}.git',
            shell=True,
            # TODO: Make directory when seeding data instead of hardcoding path
            cwd="hudl_repos/competitive",
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        out, err = result.communicate()
        print(out) if out else print(err)

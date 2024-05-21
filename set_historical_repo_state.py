""" Gets the revision list for a given repository and checks out the first """

import subprocess
import json
import csv
import logging
from seed_data import AllRepos

# git checkout `git rev-list -n 1 --first-parent --before="2009-07-27 13:37" master`

logger = logging.getLogger(__name__)


def set_historical_repo_state(business_unit_to_run_analysis_on, date_to_run_analysis_on):
    command = f'git checkout `git rev-list -n 1 --first-parent --before="{date_to_run_analysis_on}" master`'
    print(command)
    # TODO: theres probably a better way to handle retrieving a property of class than below
    business_unit = getattr(AllRepos, business_unit_to_run_analysis_on)
    for repo in business_unit:
        print(repo)
        result = subprocess.Popen(
            command,
            shell=True,
            # TODO: Make business unit param instead of hard coding IE: /competitive, /elite etc...
            cwd=f"hudl_repos/competitive/{repo}",
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        out, err = result.communicate()
        print(out) if out else print(err)

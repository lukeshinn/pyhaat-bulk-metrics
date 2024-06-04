""" Checks out master for a list of repositories """

import subprocess
import logging
from seed_data import AllRepos

logger = logging.getLogger(__name__)


def reset_repo_state(business_unit_to_run_analysis_on):
    command = 'git checkout master && git pull origin master'
    # TODO: theres probably a better way to handle retrieving a property of class than below
    business_unit = getattr(AllRepos, business_unit_to_run_analysis_on)
    print('=========== Running checkout master and pull on all repos ===========')
    for repo in business_unit:
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

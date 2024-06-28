""" Gets the revision list for a given repository and checks out the first commit before that date """

import subprocess
import logging
from seed_data import AllRepos

logger = logging.getLogger(__name__)
Debug = False


def set_historical_repo_state(repo_dirs, date_to_run_analysis_on):
    command = f'git checkout `git rev-list -n 1 --first-parent --before="{date_to_run_analysis_on}" master`'
    print(command) if Debug else None
    # business_unit = getattr(AllRepos, business_unit_to_run_analysis_on)
    for repo in repo_dirs:
        print(repo) if Debug else None
        result = subprocess.Popen(
            command,
            shell=True,
            cwd=f"{repo}",
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        out, err = result.communicate()
        print(out) if out else print(err)

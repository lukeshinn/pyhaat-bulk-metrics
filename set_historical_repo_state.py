""" Gets the revision list for a given repository and checks out the first commit before that date """

import subprocess
from analysis_logging import configure_logger


def set_historical_repo_state(repo_dirs, date_to_run_analysis_on):
    logger = configure_logger(True)
    command = f'git checkout `git rev-list -n 1 --first-parent --before="{date_to_run_analysis_on}" master`'
    logger.info(f'Running... {command}')
    for repo in repo_dirs:
        result = subprocess.Popen(
            command,
            shell=True,
            cwd=f"{repo}",
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        out, err = result.communicate()
        print(out) if out else print(err)

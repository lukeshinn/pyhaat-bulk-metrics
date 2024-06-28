""" Checks out master for a list of repositories """

import subprocess
import logging
from seed_data import AllRepos

logger = logging.getLogger(__name__)


def reset_repo_state(repo_dirs):
    command = 'git checkout master && git pull origin master'
    print('==== Running checkout master and pull on all repos ====')
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

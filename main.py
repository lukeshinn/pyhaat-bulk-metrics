#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Luke Shinn"
__version__ = "0.1.0"
__license__ = "MIT"

import argparse
import logging
from create_seed_data import create_seed_data
from analyze_business_unit import analyze_business_unit
from set_historical_repo_state import set_historical_repo_state
from reset_repo_state import reset_repo_state 
import os
from datetime import date
import re



logger = logging.getLogger(__name__)

def expected_date_string(arg_value, pattern=re.compile(r"([0-9]+(/[0-9]+)+(/[0-9]{4}$))")):
    if not pattern.match(arg_value):
        raise argparse.ArgumentTypeError("Date format must be in mm/dd/yyyy format")
    return arg_value

def main(args):
    logging.basicConfig(filename='myapp.log', level=logging.INFO)
    if args.seed:
        create_seed_data(args.seed)
    # set repo state to the desired date for analysis
    set_historical_repo_state("competitive", args.date_to_run_analysis_on)
    # analyze repo group after each repository has been set to the desired states date
    if args.rest:
        analyze_business_unit("-r", args.date_to_run_analysis_on)
    elif args.bifrost:
        analyze_business_unit("-b", args.date_to_run_analysis_on)
    elif args.graphql:
        print("GraphQL analysis is still a work in progress")
    # reset repo state back to master for subsequent runs
    reset_repo_state("competitive")

    print(args)

if __name__ == "__main__":
    """ This is executed when run from the command line """
    parser = argparse.ArgumentParser()

    # parser.add_argument("--business_unit_to_run_analysis_on", choices=['competitive', 'elite'] help="Which business unit to run analysis on")

    parser.add_argument('date_to_run_analysis_on', nargs="?", type=expected_date_string, default=date.today().strftime('%m/%d/%Y'),  help="Date format must be in mm/dd/yyyy format")

    # parser.add_argument("--b",
    #                     help="Business unit to run analysis on",
    #                     choices=['competitive', 'elite'])

    # Mutually exclusive required args
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-r", "--rest", action="store_true", help="REST API Parser")
    group.add_argument("-b", "--bifrost", action="store_true", help="Bifrost API Parser")
    group.add_argument("-g", "--graphql", action="store_true", help="GRAPHQL API Parser")

    parser.add_argument("--seed",
                        help="Clone a list of repos to a directory",
                        default=False,
                        choices=['competitive', 'elite'])
   
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s (version {version})".format(version=__version__))

    args = parser.parse_args()
    main(args)

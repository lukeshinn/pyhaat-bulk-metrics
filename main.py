#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Luke Shinn"
__version__ = "0.1.0"
__license__ = "MIT"

import argparse
import logging
import pandas as pd
import re
from datetime import date
from create_seed_data import create_seed_data
from analyze_business_unit import analyze_business_unit
from set_historical_repo_state import set_historical_repo_state
from reset_repo_state import reset_repo_state 



logger = logging.getLogger(__name__)

def expected_date_string(arg_value, pattern=re.compile(r"([0-9]+(/[0-9]+)+(/[0-9]{4}$))")):
    if not pattern.match(arg_value):
        raise argparse.ArgumentTypeError("Date format must be in mm/dd/yyyy format")
    return arg_value

def expected_frequency_string(arg_value, pattern=re.compile("m")):
    if not pattern.match(arg_value):
        raise argparse.ArgumentTypeError("Date format must be in mm/dd/yyyy format")
    return arg_value

def main(args):
    logging.basicConfig(filename='myapp.log', level=logging.INFO)
    date_range = pd.date_range(start=args.start_date_to_run_analysis_on, end=args.end_date_to_run_analysis_on, freq=args.analysis_frequency).strftime('%m/%d/%Y')
    if args.seed:
        create_seed_data(args.seed)
    for date in date_range:
        set_historical_repo_state("competitive", date)
        if args.rest:
            analyze_business_unit("-r", date)
        elif args.bifrost:
            analyze_business_unit("-b", date)
        elif args.graphql:
            print("GraphQL analysis is still a work in progress")
        reset_repo_state("competitive")

    print(args)

if __name__ == "__main__":
    """ This is executed when run from the command line """
    parser = argparse.ArgumentParser()

    parser.add_argument('start_date_to_run_analysis_on', type=expected_date_string, default=date.today().strftime('%m/%d/%Y'),  help="Date format must be in mm/dd/yyyy format")
    parser.add_argument('end_date_to_run_analysis_on', type=expected_date_string, default=date.today().strftime('%m/%d/%Y'),  help="Date format must be in mm/dd/yyyy format")
    parser.add_argument('analysis_frequency', help="Frequency to run analysis for. Examples: D/M/Y")

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

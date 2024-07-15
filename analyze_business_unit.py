import subprocess
import json
import csv
import logging
import pandas as pd
import os.path as path
import re
from analysis_logging import configure_logger

logger = logging.getLogger(__name__)


def analyze_business_unit(all_files_root, api_format, start_date_to_run_analysis_on):
    logger = configure_logger(True)
    command = ['pyhaat-coverage', api_format, '-l', '-rg', all_files_root]
    logger.info(f"Running {command}")
    bulk_coverage_output = subprocess.run(command, stdout=subprocess.PIPE).stdout.decode('utf-8').replace("'", '"')
    parse_stdout_for_no_endpoints_found(bulk_coverage_output)
    logger.info(bulk_coverage_output)
    bulk_coverage_dictionary = json.load(open("results.json", "r"))
    csv_file_path = f'{api_format}metrics.csv'
    if path.exists(csv_file_path):
        csv_data = pd.read_csv(csv_file_path)
        incomming_data = pd.DataFrame(bulk_coverage_dictionary['services'])
        format_dataframe_for_csv(incomming_data, api_format, start_date_to_run_analysis_on)
        formatted_data = pd.concat([csv_data, incomming_data], join="inner")
    else:
        data = pd.DataFrame(data=bulk_coverage_dictionary['services'])
        formatted_data = format_dataframe_for_csv(data, api_format, start_date_to_run_analysis_on)
    formatted_data.to_csv(csv_file_path, index=False)
    # write_pivot_table(api_format, csv_file_path, formatted_data)


def parse_stdout_for_no_endpoints_found(std_output):
    services_without_coverage = []
    for line in std_output.splitlines():
        if line.startswith('No endpoints found'):
            parts = line.split(';')
            service_name = parts[0].split()[-1]
            services_without_coverage.append(service_name)
    return services_without_coverage


def write_pivot_table(api_format, csv_file_path, data):
    if api_format == "-r":
        pivot_table = pd.pivot_table(
            data, index=["run_date"], columns=["service_name"], values=["rest_api_cov", "rest_endpoint_hit_rate"], aggfunc="sum", fill_value=0
        )
        pivot_table.to_csv(f"pivot{csv_file_path}")
    elif api_format == "-b":
        pivot_table = pd.pivot_table(
            data, index=["run_date"], columns=["service_name"], values=["bifrost_api_cov", "bifrost_endpoint_hit_rate"], aggfunc="sum", fill_value=0
        )
        pivot_table.to_csv(f"pivot{csv_file_path}")


def format_dataframe_for_csv(data, api_format, start_date_to_run_analysis_on):
    data['run_date'] = start_date_to_run_analysis_on
    if api_format == "-r":
        indexed_data = data.reindex(columns=['service_name', 'run_date', 'rest_api_cov', 'rest_endpoint_hit_rate'])
    elif api_format == "-b":
        indexed_data = data.reindex(columns=['service_name', 'run_date', 'bifrost_api_cov', 'bifrost_endpoint_hit_rate'])
    return indexed_data

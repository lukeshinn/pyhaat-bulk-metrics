import subprocess
import json
import csv
import logging
import pandas as pd
import os.path as path

from IPython.display import display


logger = logging.getLogger(__name__)

debug = True


def analyze_business_unit(api_format, date_to_run_analysis_on):
    command = ['pyhaat-coverage', api_format, '-l', '-rg', 'hudl_repos/competitive']
    print(api_format)
    print(f"==== Running {command} ====")
    print(f"==== this could take a bit to run..... ====")
    bulk_coverage_output = subprocess.run(command, stdout=subprocess.PIPE).stdout.decode('utf-8').replace("'", '"')
    # TODO: CRITICAL: Handle "No endpoints found for {serviceName}; skipping coverage check"
    bulk_coverage_dictionary = json.loads(bulk_coverage_output)
    services_json_data = bulk_coverage_dictionary['services']
    csv_file_path = f'{api_format}metrics.csv'
    if path.exists(csv_file_path):
        csv_data = pd.read_csv(csv_file_path)
        incomming_data = pd.DataFrame(services_json_data)
        format_dataframe_for_csv(incomming_data, api_format, date_to_run_analysis_on)
        formatted_data = pd.concat([csv_data, incomming_data], join="inner")
    else:
        data = pd.DataFrame(data=services_json_data)
        formatted_data = format_dataframe_for_csv(data, api_format, date_to_run_analysis_on)
    formatted_data.to_csv(csv_file_path, index=False)


def format_dataframe_for_csv(data, api_format, date_to_run_analysis_on):
    data['run_date'] = date_to_run_analysis_on
    if api_format == "-r":
        indexed_data = data.reindex(columns=['service_name', 'run_date', 'rest_api_cov', 'rest_endpoint_hit_rate'])
    if api_format == "-b":
        indexed_data = data.reindex(columns=['service_name', 'run_date', 'bifrost_api_cov', 'bifrost_endpoint_hit_rate'])
    return indexed_data

import subprocess
import json
import csv
import logging
import pandas as pd
import os.path as path
from IPython.display import display


logger = logging.getLogger(__name__)


def analyze_business_unit(api_format, date_to_run_analysis_on):
    command = ['pyhaat-coverage', api_format, '-l', '-rg', 'hudl_repos/competitive']
    print(api_format)
    print(f"======== Running {command} ========")
    print("============ this could take up to a minute ============")
    bulk_coverage_output = subprocess.run(command, stdout=subprocess.PIPE).stdout.decode('utf-8').replace("'", '"')
    # TODO: CRITICAL: Handle "No endpoints found for {serviceName}; skipping coverage check"
    # print("==== outputting bulk coverage ====")
    # print(bulk_coverage_output)
    bulk_coverage_dictionary = json.loads(bulk_coverage_output)
    data = bulk_coverage_dictionary['services']
    csv_file_path = f'metrics.csv'
    if path.exists(csv_file_path):
        data = pd.read_csv(csv_file_path)
        display(data)
        incomming_data = pd.DataFrame(data)
        incomming_data['run_date'] = date_to_run_analysis_on
        display(incomming_data)
        data = pd.concat([data, incomming_data], join="inner")
        display(data)
    else:
        # formatted_data = [{'service_name': node['service_name'], **{key: value for key, value in node.items() if key != 'service_name'}} for node in data]
        data = pd.DataFrame(data=data)
        data['run_date'] = date_to_run_analysis_on
        display(data)
        data = data.reindex(columns=['service_name', 'run_date', 'rest_api_cov', 'rest_endpoint_hit_rate'])
        display(data)
    data.to_csv(csv_file_path, index=False)


def format_dataframe_for_csv(data, api_format, date_to_run_analysis_on):
    print("works")

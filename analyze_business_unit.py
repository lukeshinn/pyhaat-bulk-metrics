import subprocess
import json
import csv
import logging
import pandas as pd
import os.path as path


logger = logging.getLogger(__name__)


def analyze_business_unit(api_format, date_to_run_analysis_on):
    # fields = ['bifrost_api_cov', 'bifrost_endpoint_hit_rate', 'service_name']
    fields = ['service_name', date_to_run_analysis_on, 'bifrost_api_cov']
    command = ['pyhaat-coverage', api_format, '-l', '-rg', 'hudl_repos/competitive']
    print(api_format)
    print(f"======== Running {command} ========")
    print("============ this could take up to a minute ============")
    bulk_coverage_output = subprocess.run(command, stdout=subprocess.PIPE).stdout.decode('utf-8').replace("'", '"')
    # TODO: CRITICAL: Handle "No endpoints found for {serviceName}; skipping coverage check"
    print("==== outputting bulk coverage ====")
    print(bulk_coverage_output)
    bulk_coverage_dictionary = json.loads(bulk_coverage_output)
    data = bulk_coverage_dictionary['services']
    csv_file_path = f'metrics.csv'
    if path.exists(csv_file_path):
        df = pd.read_csv(csv_file_path)
        incomming_data = pd.DataFrame(data)
        format_column_names_to_have_date(incomming_data, date_to_run_analysis_on)
        df = df.merge(incomming_data, how="inner", on="service_name")
    else:
        # TODO: This is so ugly :( On our first run, to set a precedent for our CSV we need to re arrange the services list so that in each node, service_name is first. Otherwise it will make the CSV tough to read.
        # "services": [
        #     {"bifrost_api_cov": 42.03, "bifrost_endpoint_hit_rate": 33.41, "service_name": "hudl-organizations"},
        #     {"bifrost_api_cov": 52.5, "bifrost_endpoint_hit_rate": 44.39, "service_name": "hudl-feedproducer"},
        #     {"bifrost_api_cov": 90.0, "bifrost_endpoint_hit_rate": 90.0, "service_name": "hudl-profiles"},
        # ],
        formatted_data = [{'service_name': node['service_name'], **{key: value for key, value in node.items() if key != 'service_name'}} for node in data]
        df = pd.DataFrame(data=formatted_data)
        format_column_names_to_have_date(df, date_to_run_analysis_on)
    df.to_csv(csv_file_path, index=False)


def format_column_names_to_have_date(data_frame, date_to_run_analysis_on):
    data_frame.rename(
        columns={'rest_api_cov': f'rest_api_cov {date_to_run_analysis_on}', 'rest_endpoint_hit_rate': f'rest_endpoint_hit_rate {date_to_run_analysis_on}'},
        inplace=True,
    )
    return data_frame

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
    print(f"======== Running {command} ========")
    print("======== this could take up to a minute ========")
    bulk_coverage_output = subprocess.run(command, stdout=subprocess.PIPE).stdout.decode('utf-8').replace("'", '"')
    # TODO: CRITICAL: Handle "No endpoints found for {serviceName}; skipping coverage check"
    print("==== outputting bulk coverage ====")
    print(bulk_coverage_output)
    bulk_coverage_dictionary = json.loads(bulk_coverage_output)
    # TODO Write new file with date instead of alwyas appending to test.csv
    # with open('test.csv', 'a', newline='') as file:
    #     writer = csv.DictWriter(file, fieldnames=fields)
    #     writer.writeheader()
    #     for i in bulk_coverage_dictionary['services']:
    #         print(i)
    #         logger.info(f'writing {i} to csv')
    #         writer.writerow(i)

    # ===========================================================
    mydataset = {'cars': ["competitions", "organizations", "feed"], 'sept': [3, 7, 2]}
    mydataset2 = {'cars': ["competitions", "organizations", "feed"], 'oct': [11, 12, 13]}
    csv_file_path = 'metrics.csv'
    if path.exists('metrics.csv'):
        print('exists')
        df = pd.read_csv(csv_file_path)
        df = df.merge(pd.DataFrame(mydataset2), how="inner", on="cars")
    else:
        df = pd.DataFrame(data=mydataset)

    # df = pd.read_csv(csv_file_path)

    # Step 2: Define the values for the new "City" column
    # new_city_values = ['New York', 'Los Angeles', 'Chicago', 'San Francisco']

    # Step 3: Add the new "City" column to the DataFrame
    # df['City'] = new_city_values

    # Step 4: Write the DataFrame back to the CSV file
    df.to_csv(csv_file_path, index=False)

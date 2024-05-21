import subprocess
import json
import csv
import logging


logger = logging.getLogger(__name__)


def analyze_business_unit(seed):
    fields = ['rest_endpoint_hit_rate', 'rest_api_cov', 'service_name']
    command = ['pyhaat-coverage', '-r', '-l', '-rg', 'hudl_repos/competitive']
    bulk_coverage_output = subprocess.run(command, stdout=subprocess.PIPE).stdout.decode('utf-8').replace("'", '"')
    # TODO: CRITICAL: Handle "No endpoints found for {serviceName}; skipping coverage check"
    print("==== outputting bulk coverage ====")
    print(bulk_coverage_output)
    bulk_coverage_dictionary = json.loads(bulk_coverage_output)
    # TODO Write new file with date instead of alwyas appending to test.csv
    with open('test.csv', 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        for i in bulk_coverage_dictionary['services']:
            logger.info(f'writing {i} to csv')
            writer.writerow(i)

import sys
import os
import json
import platform
import argparse

# Add the utils directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'utils')))

# Create the parser
parser = argparse.ArgumentParser(description="command-line arguments.")
parser.add_argument('--host', type=str, help='Host Application Code', required=False)

from hs_campaign import get_campaign_ids, get_host_json
from visualize import visualize_message, style_message


# Open and read the JSON file
with open('data/paths.json', 'r') as file:
    data = json.load(file)

visualize_message("Start Fetching Campaign Id and Variant Id", '█', '-', 100)

platform = platform.system()
sep = '\\' if platform == 'Windows' else '/'

# Parse the arguments
args = parser.parse_args()
host = args.host or 'PHXS'

json_files = get_host_json(data[platform]['HomescreenData'], host)

if not json_files:
    style_message('Json file not present for the host', 'red')

for files in json_files:
    host = (files.split(sep)[-1]).split('-')[:3]
    print('')
    style_message(host, 'yellow')
    get_campaign_ids(files, 'CCX_Start_4.0_Toast')
    get_campaign_ids(files, 'CCX_Start_4.0_Whats_New')
    get_campaign_ids(files, 'CCX_Start_4.0_Home')


visualize_message("Completed Fetching Campaign Id and Variant Id", '-', '█', 100)

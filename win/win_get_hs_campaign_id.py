import sys
import os

# Add the utils directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'utils')))

from hs_campaign import get_campaign_ids, get_host_json
from visualize import visualize_message, style_message

visualize_message("Start Fetching Campaign Id and Variant Id", '█', '-', 100)

hosts = ['PHXS', 'PHSP']
for host in hosts:
    json_files = get_host_json('AppData\\Roaming\\Adobe\\CCX Welcome\\data', host)

    if not json_files:
        style_message('Json file not present for the host', 'red')

    for files in json_files:
        host = (files.split('\\')[-1]).split('-')[:3]
        print('')
        style_message(host, 'yellow')
        get_campaign_ids(files, 'CCX_Start_4.0_Toast')
        get_campaign_ids(files, 'CCX_Start_4.0_Whats_New')
        get_campaign_ids(files, 'CCX_Start_4.0_Home')



visualize_message("Completed Fetching Campaign Id and Variant Id", '-', '█', 100)
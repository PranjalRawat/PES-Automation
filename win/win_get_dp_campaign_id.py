import sys
import os

# Add the utils directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'utils')))

from dp_campaign import get_campaign_ids, get_host_json
from visualize import visualize_message, style_message

visualize_message("Start Fetching Discover Panel Campaign Id and Variant Id", '█', '-', 100)

hosts = ['PHXS', 'PHSPBETA']

for host in hosts:
    json_files = get_host_json('AppData\\Roaming\\Adobe\\CCX Welcome\\discover_panel', host)

    if not json_files:
        style_message('Json file not present for the host', 'red')

    for files in json_files:
        host = (files.split('\\')[-1]).split('-')[:3]
        print('')
        style_message(host, 'yellow')
        get_campaign_ids(files, 'Discover_Panel')
        get_campaign_ids(files, 'in_app_contextual_notifications')
        get_campaign_ids(files, 'DP_Tool_Techniques_v1')


visualize_message("Completed Fetching Campaign Id and Variant Id", '-', '█', 100)

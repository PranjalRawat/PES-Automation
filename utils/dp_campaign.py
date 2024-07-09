import glob
import os
import json
from visualize import style_message

def get_host_json(relative_path, host = 'PHXS'):
    """
    Get the specified json file.

    :param relative_path: Relative path from the user's home directory to json file.
    """
    home_directory = os.path.expanduser("~")  # Get the current user's home directory
    folder_path = os.path.join(home_directory, relative_path)

    search_pattern = os.path.join(folder_path, host + '*')

    # Use glob to find files matching the pattern
    json_files = glob.glob(search_pattern)
    return json_files


def get_campaign_ids(json_file, surface):
    style_message(f"\n {' '*2} - {surface} : ", 'green')
    try:
        with open(json_file, 'r') as file:
            data = json.load(file)

        containers = data["surfaces"][surface]["containers"]
        for container in containers:
            containerLabel = container['containerLabel']
            campaign_id = container["containerAnalyticsData"]["campaignId"]
            variant_id = container["containerAnalyticsData"]["variationId"]

            style_message(f"\n {' '*7} => Container Label: {containerLabel}", 'yellow')
            style_message(f" {' '*10} * Campaign ID: {campaign_id}", 'cyan')
            style_message(f" {' '*10} * Variant ID: {variant_id}", 'cyan')

    except Exception:
        failedContainers = containers = data["surfaces"][surface]["failedContainers"]
        for container in failedContainers:
            containerLabel = container['containerLabel']
            errorCode = container["errorCode"]
            errorMessage = container["errorMessage"]

            style_message(f"\n {' '*7} => Container Label: {containerLabel}", 'yellow')
            style_message(f" {' '*10} * Error Code: {errorCode}", 'red')
            style_message(f" {' '*10} * Error Message: {errorMessage}", 'red')

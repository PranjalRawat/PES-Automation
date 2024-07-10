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

from delete_dir import delete_directory
from end_process import end_process_by_name
from visualize import visualize_message


# Open and read the JSON file
with open('data/paths.json', 'r') as file:
    data = json.load(file)

visualize_message("Simulate Second Launch", '█', '-', 100)

platform = platform.system()

# Parse the arguments
args = parser.parse_args()
host = args.host or 'PHXS'

# Stop Adobe Host Application
end_process_by_name(data[platform][host]['Title'])

# Delete CCX Welcome
delete_directory(data[platform]['CCXWelcome'])


visualize_message("Completed Second Launch Simulation", '-', '█', 100)

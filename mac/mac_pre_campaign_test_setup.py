import sys
import os

# Add the utils directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'utils')))

from delete_dir import delete_directory, delete_file
from end_process import end_process_by_name
from visualize import visualize_message

visualize_message("Starting Pre Campaign Test Setup for Adobe Photoshop", '█', '-', 100)



# Stop Adobe Photoshop
end_process_by_name('Adobe Photoshop 2024')

# Stop Creative Cloud Process
end_process_by_name('Creative Cloud')

# Delete CCX Welcome
delete_directory('Library/Caches/Adobe/CCX Welcome')

# Delete Plugin Storage
delete_directory('Library/Application Support/Adobe/UXP/PluginsStorage')

# Delete Photoshop Preferences
delete_directory('Library/Preferences/Adobe Photoshop 2024 Settings')
delete_directory('Library/Preferences/Adobe Photoshop (Beta) Settings')
delete_file('Library/Preferences/Adobe Photoshop 2024 Paths')



visualize_message("Completed Pre Campaign Test Setup for Adobe Photoshop", '-', '█', 100)

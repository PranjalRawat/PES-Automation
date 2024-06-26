import sys
import os

# Add the utils directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'utils')))

from delete_dir import delete_directory
from end_process import end_process_by_name
from visualize import visualize_message

visualize_message("Starting Pre Campaign Test Setup for Adobe Photoshop", '█', '-', 100)



# Stop Adobe Photoshop
end_process_by_name('Photoshop.exe')

# Stop Creative Cloud Process
end_process_by_name('Creative Cloud.exe')

# Delete CCX Welcome
delete_directory("AppData\\Roaming\\Adobe\\CCX Welcome")

# Delete Plugin Storage
delete_directory('AppData\\Roaming\\Adobe\\UXP\\PluginsStorage')

# Delete Photoshop Preferences
delete_directory('AppData\\Roaming\\Adobe\\Adobe Photoshop 2024')
delete_directory('AppData\\Roaming\\Adobe\\Adobe Photoshop (Beta)')


visualize_message("Completed Pre Campaign Test Setup for Adobe Photoshop", '-', '█', 100)

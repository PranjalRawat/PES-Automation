import sys
import os

# Add the utils directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'utils')))

from delete_dir import delete_directory
from end_process import end_process_by_name
from visualize import visualize_message

visualize_message("Simulate Second Launch for Adobe Photoshop", '█', '-', 100)


# Stop Adobe Photoshop
end_process_by_name('Adobe Photoshop 2024')

# Delete CCX Welcome
delete_directory('Library/Caches/Adobe/CCX Welcome')



visualize_message("Completed Second Launch Simulation for Adobe Photoshop", '-', '█', 100)

import psutil
import time
from visualize import style_message

def print_progress_bar(duration):
    """
    Prints a progress bar for the given duration.

    :param duration: Total time in seconds for the progress bar.
    """
    total_ticks = 20
    interval = duration / total_ticks
    print("Terminating Process: ", end='', flush=True)
    for _ in range(total_ticks):
        time.sleep(interval)
        print("█", end='', flush=True)
    style_message(" Done", 'green')


def end_process_by_name(process_name):
    """
    Ends processes with the given name.

    :param process_name: Name of the process to be terminated.
    """
    process_found = False

    # Find all processes with the specified name
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            if process_name == proc.info['name']:
                process_found = True
                proc.terminate()
                print_progress_bar(5)
                style_message(f"Process terminated successfully ==>> '{proc.info['name']}': (PID: {proc.info['pid']})", 'green')

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess) as e:
            style_message(f"Error terminating process ==>> '{proc.info['name']}': {e}", 'red')

    if not process_found:
        style_message(f"Process is not running ==>> '{process_name}'", 'cyan')

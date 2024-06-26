def visualize_message(message, upper_border='█', lower_border='*', length=100):
    """
    Visualizes the message with a decorative border in the terminal.

    :param message: The message content to visualize.
    :param upper_border: Optional. Character used for the border. Defaults to '█'.
    :param lower_border: Optional. Character used for the border. Defaults to '*'.
    :param length: Optional. Length of the border. Defaults to 100.
    """
    message = f"\n{upper_border * length}\n {message} \n{lower_border * length}\n"
    style_message(message, 'yellow')


def style_message(message, style='normal'):
    """
    Styles the output message for terminal printing.

    :param message: The message content to style.
    :param style: Optional. Style of the message.
    Defaults to 'normal'.
    """
    styles = {
        'bold': '\033[1m',         # Bold or increased intensity
        'red': '\033[91m',         # Red color
        'green': '\033[92m',       # Green color
        'cyan': '\033[96m',        # Cyan color
        'yellow': '\033[93m',      # yellow color

    }

    if style in styles:
        print(f"{styles[style]}{message}\033[0m")
    else:
        print(message)  # Print message as-is if style not found

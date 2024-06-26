# PES Campaign Testing

## Description

As Quality Engineers we are responsible for testing the PES campaigns. Below are steps to execute the scripts which will help with campaign testing.

## Installation

- ### Python Installation

  - **Using Python.org Installer:**
    - Visit [python.org](https://www.python.org/downloads/) to download the latest version of Python3.
    - Run the installer and follow the prompts to install Python.
    - After installation, you can verify by opening Terminal and typing:
      ```bash
      python3 --version
      ```

- ### `psutil` Installation

  After installing Python, you may need to install `psutil`, a Python library for system and process utilities.

  - #### Using pip

    Open your terminal and run the following command:

    ```bash
    pip3 install psutil
    ```

## Usage

- ### Mac

  - Open terminal in the project root directory
  - **Pre Campaign Setup** - Executing pre campaign testing script to clear all caches and terminate application
    ```bash
    python3 mac/mac_pre_campaign_test_setup.py
    ```
  - **Simulate First Launch** - Executing simulate first launch script to simulate the first launch on PS
    ```bash
    python3 mac/mac_simulate_first_launch.py
    ```
  - **Simulate Second Launch** - Executing simulate second launch script to simulate the second launch on PS
    ```bash
    python3 mac/mac_simulate_second_launch.py
    ```
  - **Get HomeScreen Campaign and Variant Ids** - Executing get hs campaign id script to fetch campaign and variant id
    ```bash
    python3 mac/mac_get_hs_campaign_id.py
    ```

- ### Win

  - Open Command-Line in the project root directory
  - **Pre Campaign Setup** - Executing pre campaign testing script to clear all caches and terminate application
    ```bash
    python3 win\win_pre_campaign_test_setup.py
    ```
  - **Simulate First Launch** - Executing simulate first launch script to simulate the first launch on PS
    ```bash
    python3 win\win_simulate_first_launch.py
    ```
  - **Simulate Second Launch** - Executing simulate second launch script to simulate the second launch on PS
    ```bash
    python3 win\win_simulate_second_launch.py
    ```
  - **Get HomeScreen Campaign and Variant Ids** - Executing get hs campaign id script to fetch campaign and variant id
    ```bash
    python3 win\win_get_hs_campaign_id.py
    ```

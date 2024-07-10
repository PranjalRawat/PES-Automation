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

## Application Supports

Currently the script only support Adobe Photoshop (GA) and Adobe Photoshop (Beta). To execute scripts for particular hosts we use the host SAP code as a argument with the command via the terminal.

#### Note: By default Adobe Photoshop (GA) is used as host application if no host SAP code is not provided as a argument.

- Here are the supported host applications and their respective SAP codes:

  ```bash
  - Adobe Photoshop (GA) = PHXS
  - Adobe Photoshop (Beta) = PHSPBETA
  ```

## Usage

- ### Mac and Win

  - Open terminal in the project root directory
  - **Pre Campaign Setup** - Executing pre campaign testing script to clear all caches and terminate application

    ```bash
    python3 src/pre_campaign_test_setup.py --host PHXS

    python3 src/pre_campaign_test_setup.py --host PHSPBETA
    ```

  - **Simulate First Launch** - Executing simulate first launch script to simulate the first launch

    ```bash
    python3 src/simulate_first_launch.py --host PHXS

    python3 src/simulate_first_launch.py --host PHSPBETA
    ```

  - **Simulate Second Launch** - Executing simulate second launch script to simulate the second launch

    ```bash
    python3 src/simulate_second_launch.py --host PHXS

    python3 src/simulate_second_launch.py --host PHSPBETA
    ```

  - **Get HomeScreen Campaign and Variant Ids** - Executing get hs campaign id script to fetch campaign and variant id

    ```bash
    python3 src/get_hs_campaign_id.py --host PHXS

    python3 src/get_hs_campaign_id.py --host PHSPBETA
    ```

  - **Get Discover Panel Campaign and Variant Ids** - Executing get dp campaign id script to fetch campaign and variant id

    ```bash
    python3 src/get_dp_campaign_id.py --host PHXS

    python3 src/get_dp_campaign_id.py --host PHSPBETA
    ```

<img width=60px align="right" src="https://github.com/Ahsxka/python-automation/assets/162576190/2c3398bb-f9bf-4a28-9873-ea1d80310888"></img>

# Cisco IOS SSH automation

This Python script is designed to perform configuration tasks on Cisco IOS devices. It reads commands from a file and executes them on the specified devices.

## Features

- Supports configuration of Cisco IOS devices.
- Provides an interactive mode to select the desired operation.
- Easy-to-use command-line interface.

## Use case

<img align="right" width=60px src=https://github.com/Ahsxka/python-automation/assets/162576190/00468e89-15ce-4ed9-b44e-ba91a77a8fa5></img>


- Configuring multiple cisco IOS equipments with the same configuration
- Saving show commands _(e.g. show tech-support)_ from multiple equipments

## Tested environment

The script is developed using Python 3.12 and relies on [Netmiko](https://github.com/ktbyers/netmiko) version 4.3.0.

## Installation

1. Clone this repository to your local machine:
```
git clone https://github.com/Ahsxka/python-automation.git
```

2. Navigate to the project directory:
```
cd python-automation
```

3. Install the required dependencies:
```
pip install -r requirements.txt
```

4. You´re ready to go !

> [!NOTE]
> It is recommended to use a *[virtual environment](https://docs.python.org/3/library/venv.html)* to avoid dependency conflicts.


## Using cisco-ssh.py
1. Execute `cisco-ssh.py` :
```
python cisco-ssh.py
```

2. Choose an IP file _(should be **1 IP per line**)_ :

<img width="600" alt="image" src="https://github.com/Ahsxka/python-automation/assets/162576190/8daa9435-e41b-47c8-9e2c-744d5735486a">

3. Choose an export folder, where the `.log` files will be saved :

<img width="600" alt="image" src="https://github.com/Ahsxka/python-automation/assets/162576190/aa727361-778f-4843-b949-53ccd17e8435">

4. Choose between the 2 modes : **Show commands** or **Config commands** :

<img width="600" alt="image" src="https://github.com/Ahsxka/python-automation/assets/162576190/fe46c641-48a0-4d2a-b228-7c47799ef69b">


5. Choosing the Show commands mode, you're prompted to choose the command you want to use. If you want to use another show command, you have to write the whole command, **without shortcut** :

<img width="600" alt="image" src="https://github.com/Ahsxka/python-automation/assets/162576190/c5f9fa6a-fe41-4b13-88a6-7c60f05d0185">

  
6. Choosing the Config commands mode, you're prompted to choose the configuration file you want to import :

<img width="600" alt="image" src="https://github.com/Ahsxka/python-automation/assets/162576190/e2e5d302-fc36-44d0-bd0e-8ce2ed2d7bda">

7. Enter username, password (and enable password) of your cisco equipement, and if you want the script to enter in verbose mode :

<img width="450" alt="image" src="https://github.com/Ahsxka/python-automation/assets/162576190/65b3a433-86cc-42b3-aea4-9348d504a573">

7. Last step is verifying your settings.

<img width="450" alt="image" src="https://github.com/Ahsxka/python-automation/assets/162576190/4c443a1b-7db2-4b98-a831-8153f92d14ca">

>[!WARNING]
> Be sure that everything is fine before executing this last part !!!!


<!--<img width="303" alt="image" src="https://github.com/Ahsxka/python-automation/assets/162576190/de3b3e00-9a7f-4863-bc4f-1da49f4bf84f">-->

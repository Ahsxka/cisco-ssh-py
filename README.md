# Cisco IOS SSH automation

This Python script is designed to perform configuration tasks on Cisco IOS devices. It reads commands from a file and executes them on the specified devices.

## Features

- Supports configuration of Cisco IOS devices.
- Provides an interactive mode to select the desired operation.
- Easy-to-use command-line interface.

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


## Using Cisco IOS SSH automation
1. Execute `cisco-ssh.py` :
```
python cisco-ssh.py
```

2. Choose an IP file :
<img width="600" alt="image" src="https://github.com/Ahsxka/python-automation/assets/162576190/8daa9435-e41b-47c8-9e2c-744d5735486a">

3. Choose an export folder, where the `.log` files will be saved :
<img width="600" alt="image" src="https://github.com/Ahsxka/python-automation/assets/162576190/aa727361-778f-4843-b949-53ccd17e8435">

4. Choose between the 2 modes : Show commands or Config commands :

5. Choosing the Show commands mode :

  
6. Choosing the Config commands mode :

<img width="600" alt="image" src="https://github.com/Ahsxka/python-automation/assets/162576190/e2e5d302-fc36-44d0-bd0e-8ce2ed2d7bda">

7. Verifying settings

<img width="492" alt="image" src="https://github.com/Ahsxka/python-automation/assets/162576190/4c443a1b-7db2-4b98-a831-8153f92d14ca">




<!--<img width="303" alt="image" src="https://github.com/Ahsxka/python-automation/assets/162576190/de3b3e00-9a7f-4863-bc4f-1da49f4bf84f">-->

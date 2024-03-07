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

```
python cisco-ssh.py
```

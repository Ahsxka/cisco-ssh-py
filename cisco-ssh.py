import sys
import tkinter as tk
from tkinter import filedialog
import datetime
from netmiko import ConnectHandler
import os


######################################
#               COLORS               #
######################################
class colors:
    RESET = '\033[0m'
    ROUGE = '\033[91m'
    VERT = '\033[92m'
    JAUNE = '\033[93m'
    BLEU = '\033[94m'


class color_format:
    @staticmethod
    def print_error(message, end='\n'):
        print(f"{colors.ROUGE}Error   : {message}{colors.RESET}", end=end)

    @staticmethod
    def print_success(message, end='\n'):
        print(f"{colors.VERT}Succes  : {message}{colors.RESET}", end=end)

    @staticmethod
    def print_warning(message, end='\n'):
        print(f"{colors.JAUNE}Warning : {message}{colors.RESET}", end=end)

    @staticmethod
    def print_info(message, end='\n'):
        print(f"{colors.BLEU}Info    : {message}{colors.RESET}", end=end)


def choose_folder():
    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', 1)

    # Open directory picker
    folder = filedialog.askdirectory()
    return folder


def choose_file():
    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', 1)

    # Open file picker
    archivo = filedialog.askopenfilename()
    return archivo


def read_file(file_name):  # returns a list containing each line of a given file.
    if len(file_name) != 0:
        lines = []
        with open(file_name, 'r') as f:
            for line in f:
                lines.append(line.strip())
        if len(lines) != 0:
            return lines


def version(basename, mode, command):  # return an incremental file name, according to existing files in directory
    base, ext = os.path.splitext(basename)
    v = 0
    new_filename = basename
    if mode == "show":
        ncommand = command.replace(" ", "-")
        new_filename = f"{base}-{ncommand}-{v}{ext}"
        while os.path.exists(new_filename):
            v += 1
            new_filename = f"{base}-{ncommand}-{v}{ext}"
    else:
        while os.path.exists(new_filename):
            v += 1
            new_filename = f"{base}-{v}{ext}"
    return new_filename


# MAIN FUNCTION : EXECUTING COMMANDS

def execute_commands(ip, username, password, secret, commands, verbose, mode, export_folder):
    try:

        errors = 0
        # Create SSH connection, and elevate to enable user
        client = ConnectHandler(ip=ip, username=username, password=password, device_type="cisco_ios", secret=secret)
        prompt = client.find_prompt()[:-1]
        if not client.check_enable_mode():
            color_format.print_info(f"Upgrading to enable mode on host {ip}")
            client.enable()

        if verbose == "y":
            color_format.print_info(f"Enable Mode {client.check_enable_mode()}")

        basename = f'{export_folder}/{ip}.log'
        new_filename = version(basename, mode, commands)
        with open(new_filename, 'w', encoding='utf-8') as f:

            f.write(f"Hostname        : {prompt}\n")
            f.write(f"IP address      : {ip}\n")
            f.write(f"Execution start : {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            output = ""

            if mode == "config":
                total_commands = len(commands)
                for command in commands:
                    if verbose == "y":
                        color_format.print_info(f"Executing command : {command}")

                    if r"\n" in command:
                        command = command.replace(r"\n", "")
                        cmd_list = [
                            [f"{command}", r"confirm"],
                            ["\n", r""],
                        ]
                        if verbose == "y":
                            print(cmd_list)
                        try:
                            result = client.send_multiline(cmd_list, expect_string=prompt)
                        except:
                            result = "None"

                    else:
                        result = client.send_command(command, expect_string=prompt, read_timeout=120)

                    output += f"Command executed : {command}\n"

                    if result:
                        if verbose == "y":
                            print(result)
                        output += f"\nresult : \n{result}\n\n"

                        # Testing for execution errors :
                        if result.__contains__("Invalid input detected") \
                                or result.__contains__("Unknown command or computer name") \
                                or result.__contains__("Incomplete command") \
                                or result.__contains__("Ambiguous command"):
                            errors += 1

            if mode == "show":
                total_commands = 1
                command = commands

                if verbose == "y":
                    color_format.print_info(f"Executing command : {command}")
                result = client.send_command(command, read_timeout=120)
                output += f"Command executed : {command}\n"

                if result:
                    if verbose == "y":
                        result_lines = result.splitlines()
                        for line in result_lines[:10]:  # print only the first 10 lines of the result
                                print(line)
                        print(f"\n[Output omitted......]")
                    output += f"\nresult : \n{result}\n\n"

                    if result.__contains__("Invalid input detected") \
                            or result.__contains__("Unknown command or computer name") \
                            or result.__contains__("Incomplete command") \
                            or result.__contains__("Ambiguous command"):
                        errors += 1

            # Writing log info :
            f.write(f"Execution end   : {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Total number of commands: {total_commands}\n")
            f.write(f"Number of failed commands: {errors}\n\n")
            f.write(f"{80 * "-"}")
            f.write(f"\n\n{output}")

            client.disconnect()

        if errors == 0:
            color_format.print_success(f"Successfully executed commands on host {ip}.")
        elif errors == len(commands):
            color_format.print_error(f"All commands failed. Please verify the commands in your file and try again.")
        else:
            color_format.print_warning(f"Successfully executed commands on host {ip} but {errors} error(s) found.")

    except Exception as e:
        color_format.print_error((f"Connection error with host {ip} : {str(e)}"))

    return errors


def inicio(ip_list, commands_list, mode, ip_file, export_folder, command_file):
    # SSH creds
    username = input("Username : ")
    password = input("Password : ")
    secret = input("Secret (leave blank if same as password or no need of enable) : ")
    if len(secret) == 0:
        secret = password
    print(f"{80 * "-"}")
    verbose = str(input("Verbose mode [y/N] : ")).lower()
    if not verbose:
        verbose = 'n'
    print(f"{80 * "-"}")
    color_format.print_info("Current settings :")
    print("Verbose mode : on" if verbose == "y" else "Verbose mode : off")
    print(f"IP file      : {ip_file}")
    print(f"Command file : {command_file}\n               {len(commands_list)} commands to run." if mode == "config" else f"Command      : {commands_list}")
    print(f"Export folder: {export_folder}")
    print(f"Username     : {username}")
    print(f"Password     : {password}")

    print(f"{80 * "-"}")
    color_format.print_warning("Do you want to continue with these settings? [y/N] : ", end="")
    confirmation = input().lower() or "n"
    print(f"{80 * "-"}")

    if confirmation == "y":
        # Execute commands on each @IP
        error_total = 0
        for ip in ip_list:
            print(f"Executing Commands on host {ip}...")
            error_total += execute_commands(ip, username, password, secret, commands_list, verbose, mode, export_folder)
            print("\n")
        if error_total != 0:
            print(f"{80 * "-"}\n")
            color_format.print_warning(f"{error_total} error(s) detected. See log for full detail.")
    else:
        color_format.print_warning("Aborting session...")
    print(f"{80 * "-"}")


def main():
    while True:
        print("\nChoose an IP file, one IP per line :")
        ip_file = choose_file()
        if len(ip_file) == 0:
            color_format.print_error("No IP file provided. Please provide a valid IP file.")
            sys.exit(1)
        ip_list = read_file(ip_file)
        if not ip_list:
            color_format.print_error("Empty IP file. Please provide a valid IP file.")
            sys.exit(1)

        print(f"{80 * "-"}")
        print(f"Please select export folder:")
        export_folder = choose_folder()
        export_folder = export_folder + "/" if export_folder else ""

        # Verbose mode ??
        print(f"{80 * "-"}")
        while True:
            print("Menu:")
            print("1. Show Commands Mode")
            print("2. Configurations Mode")
            print("3. Quit")
            mode = input("Enter your choice (1/2/3): ")
            print(f"{80 * "-"}")
            if mode not in ["1", "2", "3"]:
                color_format.print_warning("Invalid choice. Please enter a valid option.")
                print(f"{80 * "-"}")
            else:
                break


        if mode == "1":
            while True:
                print("Menu:")
                commands_map = {
                    "1": "show running-config",
                    "2": "show ip route",
                    "3": "show ip interface brief",
                    "4": "show interfaces",
                    "5": "show version",
                    "6": "show mac-address-table",
                    "7": "show interface status",
                    "8": "show vlan brief",
                    "9": "show cdp neighbors",
                    "10": "show tech-support",
                    "11": "Quit"
                }

                for c in commands_map:
                    print(f"{c}. {commands_map[c]}")
                choice = input(f"Enter your choice [1-{len(commands_map)}] or enter your show command : ")
                print(f"{80 * "-"}")

                if choice in commands_map:
                    if choice == list(commands_map.keys())[-1]:
                        break
                    else:
                        inicio(ip_list, commands_map[choice], "show", ip_file, export_folder, command_file="")

                elif choice.startswith("show"):
                    inicio(ip_list, choice, "show", ip_file, export_folder, command_file="")

                else:
                    color_format.print_warning("No command specified: Please select a valid option")
                    print(f"{80 * "-"}")
        elif mode == "2":
            print("Choose a Cisco IOS command file, one command per line : ")
            print(f"{80 * "-"}")
            command_file = choose_file()
            if len(command_file) == 0:
                color_format.print_error(
                    "No commands file provided. Please provide a valid CISCO IOS commands file to use the config mode.")
            else:
                commands_list = read_file(command_file)
                for command in commands_list:
                    if command.__contains__("sh") and not command.__contains__("shut"):
                        color_format.print_warning(r"One or multiple 'show' command(s) detected. Please remove them from your command file or considere using the show option")
                inicio(ip_list, commands_list, "config", ip_file, export_folder, command_file)
        elif mode == "3":
            print("Exiting program...")
            break
        else:
            color_format.print_warning("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
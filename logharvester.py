import re
from colorama import Fore

def parse_auth_log(file_path):
    try:
        with open(file_path, 'r') as f:
            for line in f:
                if "Failed password" in line:
                    match = re.search(r'Failed password for (invalid user )?(\w+) from ([\d.]+)', line)
                    if match:
                        user = match.group(2)
                        ip = match.group(3)
                        print(f"{Fore.RED}[!] Failed SSH login - User: {user}, IP: {ip}{Fore.RESET}")
    except FileNotFoundError:
        print(f"{Fore.YELLOW}[!] Log file not found: {file_path}{Fore.RESET}")

if __name__ == "__main__":
    parse_auth_log("inputs/auth.log")

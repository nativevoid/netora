import subprocess
import os
import sys

from colorama import Style, Fore

def check_connection(host):
    param = "-n" if os.name == "nt" else "-c"
    command = ["ping", param, "1", host]

    try:         
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, universal_newlines=True)

        if os.name == "nt":      
            if "Received = 1" in output:
                pass
        else:
            if "1 packets transmitted, 1 received" in output:
                pass  

    except subprocess.CalledProcessError:
        print(
            Fore.WHITE + Style.BRIGHT + "[" +
            Fore.RED + "!" +
            Fore.WHITE + Style.BRIGHT + "]" + Style.RESET_ALL +
            Fore.RED + " Error:" +
            Fore.WHITE + Style.BRIGHT + " No internet connection" + Style.RESET_ALL        
        )
        sys.exit(1)

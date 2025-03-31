import os

from colorama import Style, Fore
from src.modules.utils.connection import check_connection

BANNER = '''
                        
$$\   $$\            $$\                        
$$$\  $$ |           $$ |                       
$$$$\ $$ | $$$$$$\ $$$$$$\    $$$$$$\  $$$$$$\  
$$ $$\$$ |$$  __$$\\_$$  _|  $$  __$$\ \____$$\ 
$$ \$$$$ |$$$$$$$$ | $$ |    $$ |  \__|$$$$$$$ |
$$ |\$$$ |$$   ____| $$ |$$\ $$ |     $$  __$$ |
$$ | \$$ |\$$$$$$$\  \$$$$  |$$ |     \$$$$$$$ |
\__|  \__| \_______|  \____/ \__|      \_______|



==============================================================================================='''

def clear_terminal():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')

def display_banner():  
    print(
        Fore.GREEN +
        BANNER +
        Style.RESET_ALL + "\n", flush=True, end=''
    )

def initialize(): 
   clear_terminal()
   display_banner()  
   check_connection("8.8.8.8")

  


from colorama import Style, Fore
import os

from src.modules.utils.connection import checkConnection

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


def clearTerminal():
   if os.name == "nt":
      os.system('cls')
   else:
      os.system('clear')

def displayBanner():  
    print(Fore.GREEN + BANNER + Style.RESET_ALL + "\n", flush="True", end='')  

def initialize(): 
   clearTerminal()
   displayBanner()  
   checkConnection("8.8.8.8")

  


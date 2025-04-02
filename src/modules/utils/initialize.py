import os

from colorama import Style, Fore
from src.modules.utils.connection import check_connection

def clear_terminal():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')

def initialize(): 
   clear_terminal()  
   check_connection("8.8.8.8")

  

